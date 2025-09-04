#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SRT字幕翻译工具
支持将英文SRT字幕翻译为中文，使用OpenAI GPT-4o-mini
"""

import os
import sys
import json
import time
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any
import re

import pysrt
from openai import OpenAI
from dotenv import load_dotenv

# 设置日志
def setup_logging(log_dir: str) -> logging.Logger:
    """设置日志配置"""
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"translation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger(__name__)

class SRTTranslator:
    def __init__(self, api_key: str, base_url: str = None, model: str = "gpt-4o-mini"):
        """初始化翻译器"""
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        self.model = model
        self.logger = logging.getLogger(__name__)
        
    def translate_text(self, text: str, source_lang: str = "English", 
                      target_lang: str = "Chinese", style: str = "technical") -> str:
        """使用OpenAI API翻译文本"""
        try:
            # 构建提示词
            system_prompt = f"""你是一个专业的翻译助手，专门翻译技术教程内容。请将以下{source_lang}文本翻译成{target_lang}。

翻译要求：
1. 保持原文的意思和语气
2. 使用{style}风格的中文表达
3. 对于专业术语如"Excel"、"Microsoft"等保持英文
4. 确保翻译自然流畅，符合中文表达习惯
5. 对于口语化表达，翻译成相应的中文口语

请只返回翻译结果，不要包含任何解释或附加信息。"""

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": text}
                ],
                temperature=0.3,
                max_tokens=2000
            )
            
            translation = response.choices[0].message.content.strip()
            return translation
            
        except Exception as e:
            self.logger.error(f"翻译错误: {e}")
            return text  # 如果翻译失败，返回原文
    
    def save_checkpoint(self, checkpoint_dir: str, filename: str, 
                       translated_items: List[Dict], current_index: int):
        """保存翻译进度"""
        os.makedirs(checkpoint_dir, exist_ok=True)
        checkpoint_file = os.path.join(checkpoint_dir, f"{filename}_checkpoint.json")
        
        checkpoint_data = {
            "filename": filename,
            "current_index": current_index,
            "translated_items": translated_items,
            "timestamp": datetime.now().isoformat()
        }
        
        with open(checkpoint_file, 'w', encoding='utf-8') as f:
            json.dump(checkpoint_data, f, ensure_ascii=False, indent=2)
        
        self.logger.info(f"检查点已保存: {checkpoint_file}")
    
    def load_checkpoint(self, checkpoint_dir: str, filename: str) -> Dict:
        """加载翻译进度"""
        checkpoint_file = os.path.join(checkpoint_dir, f"{filename}_checkpoint.json")
        
        if os.path.exists(checkpoint_file):
            with open(checkpoint_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        return None
    
    def translate_srt_file(self, input_file: str, output_file: str, 
                          checkpoint_dir: str, batch_size: int = 5) -> bool:
        """翻译SRT字幕文件"""
        try:
            # 加载SRT文件
            subs = pysrt.open(input_file, encoding='utf-8')
            filename = os.path.splitext(os.path.basename(input_file))[0]
            
            self.logger.info(f"开始翻译文件: {input_file}")
            self.logger.info(f"总字幕条目数: {len(subs)}")
            
            # 检查是否有检查点
            checkpoint = self.load_checkpoint(checkpoint_dir, filename)
            if checkpoint:
                self.logger.info(f"发现检查点，从第 {checkpoint['current_index']} 条继续")
                translated_items = checkpoint['translated_items']
                start_index = checkpoint['current_index']
            else:
                translated_items = []
                start_index = 0
            
            # 批量翻译
            for i in range(start_index, len(subs), batch_size):
                batch_end = min(i + batch_size, len(subs))
                batch = subs[i:batch_end]
                
                self.logger.info(f"翻译批次 {i//batch_size + 1}: 第 {i+1}-{batch_end} 条")
                
                # 合并批次中的文本进行翻译
                batch_texts = []
                for sub in batch:
                    # 清理文本
                    text = sub.text.replace('\n', ' ').strip()
                    batch_texts.append(text)
                
                # 将批次文本合并为一个字符串进行翻译
                combined_text = '\n'.join([f"{idx+1}. {text}" for idx, text in enumerate(batch_texts)])
                
                # 翻译整个批次
                translated_combined = self.translate_text(combined_text)
                
                # 解析翻译结果
                translated_lines = translated_combined.split('\n')
                
                # 处理翻译结果
                for j, sub in enumerate(batch):
                    try:
                        # 查找对应的翻译行
                        prefix = f"{j+1}. "
                        translated_text = ""
                        
                        for line in translated_lines:
                            if line.strip().startswith(prefix):
                                translated_text = line.replace(prefix, '').strip()
                                break
                        
                        # 如果没找到匹配的行，使用原文
                        if not translated_text:
                            translated_text = sub.text
                        
                        # 创建翻译后的字幕项
                        translated_item = {
                            'index': sub.index,
                            'start': str(sub.start),
                            'end': str(sub.end),
                            'text': translated_text
                        }
                        translated_items.append(translated_item)
                        
                    except Exception as e:
                        self.logger.warning(f"处理第 {i+j+1} 条字幕时出错: {e}")
                        # 使用原文
                        translated_item = {
                            'index': sub.index,
                            'start': str(sub.start),
                            'end': str(sub.end),
                            'text': sub.text
                        }
                        translated_items.append(translated_item)
                
                # 保存检查点
                self.save_checkpoint(checkpoint_dir, filename, translated_items, batch_end)
                
                # 短暂延迟以避免API限制
                time.sleep(1)
            
            # 创建翻译后的SRT对象
            translated_subs = pysrt.SubRipFile()
            
            for item in translated_items:
                sub = pysrt.SubRipItem(
                    index=item['index'],
                    start=pysrt.SubRipTime.from_string(item['start']),
                    end=pysrt.SubRipTime.from_string(item['end']),
                    text=item['text']
                )
                translated_subs.append(sub)
            
            # 保存翻译后的SRT文件
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            translated_subs.save(output_file, encoding='utf-8')
            
            self.logger.info(f"翻译完成！输出文件: {output_file}")
            return True
            
        except Exception as e:
            self.logger.error(f"翻译文件时出错: {e}")
            return False

def main():
    """主函数"""
    # 设置工作目录
    project_dir = Path(__file__).parent
    
    # 加载环境变量
    load_dotenv(project_dir / '.env')
    
    # 设置日志
    logger = setup_logging(project_dir / 'logs')
    
    # 获取API配置
    api_key = os.getenv('OPENAI_API_KEY')
    base_url = os.getenv('OPENAI_BASE_URL')
    
    if not api_key:
        logger.error("请在.env文件中设置OPENAI_API_KEY")
        return
    
    # 初始化翻译器
    translator = SRTTranslator(api_key, base_url)
    
    # 设置输入输出路径
    input_dir = project_dir / 'input'
    output_dir = project_dir / 'output'
    checkpoint_dir = project_dir / 'checkpoints'
    
    # 检查输入文件
    input_file = project_dir.parent / "001 Entering Text to Create Excel Spreadsheet Titles_en.srt"
    
    if not input_file.exists():
        logger.error(f"输入文件不存在: {input_file}")
        return
    
    # 复制输入文件到input目录
    import shutil
    input_copy = input_dir / input_file.name
    shutil.copy2(input_file, input_copy)
    logger.info(f"输入文件已复制到: {input_copy}")
    
    # 设置输出文件路径
    output_file = output_dir / "001 Entering Text to Create Excel Spreadsheet Titles_zh.srt"
    
    # 开始翻译
    logger.info("开始翻译SRT字幕文件...")
    success = translator.translate_srt_file(
        str(input_copy), 
        str(output_file), 
        str(checkpoint_dir),
        batch_size=3  # 使用较小的批次大小以确保质量
    )
    
    if success:
        logger.info("翻译任务完成！")
        logger.info(f"翻译后的文件保存在: {output_file}")
    else:
        logger.error("翻译任务失败！")

if __name__ == "__main__":
    main()
