---
mode: agent
tools: ['codebase', 'search', 'findTestFiles']
description: 'Clean sensitive and private information from the project to prevent security incidents'
---

# Project Security Cleanup Task

Your task is to analyze the entire project and identify/remove sensitive information that could lead to security or privacy incidents. This is a critical security task for an educational project.

## Requirements

### 1. Scan for Sensitive Information
Analyze #codebase and identify the following sensitive data:
- API keys, tokens, passwords, secrets
- Database connection strings and credentials
- Private email addresses, phone numbers, personal information
- Internal server URLs, IP addresses, domain names
- Company-specific information, proprietary code patterns
- Real user data, customer information
- Private certificates, keys, authentication files

### 2. File Types to Focus On
Pay special attention to:
- Configuration files (`.env`, `config.js`, `settings.json`)
- Documentation files (`README.md`, `*.md`)
- Code examples and demo files
- Test files with mock data
- Log files and output samples
- Package files and dependencies list

### 3. Replacement Strategy
When removing sensitive information:
- Replace with generic placeholders (e.g., `YOUR_API_KEY`, `example.com`)
- Use realistic but fake data for demos
- Maintain code functionality while removing real credentials
- Keep educational value intact

### 4. Security Best Practices
- Check for hardcoded secrets in source code
- Verify `.gitignore` covers sensitive file patterns
- Ensure `.copilotignore` excludes private directories
- Look for accidentally committed sensitive files

## Constraints

- **DO NOT** remove educational content or break demo functionality
- **DO NOT** modify core learning examples unless they contain real sensitive data
- **PRESERVE** the project structure and learning objectives
- **MAINTAIN** code readability and educational value

## Success Criteria

1. All real API keys, passwords, and credentials are removed/replaced
2. Personal information is anonymized or removed
3. Company-specific details are generalized
4. Project remains fully functional for educational purposes
5. Security configuration files (`.gitignore`, `.copilotignore`) are properly set up

## Output Format

Provide a detailed report with:
1. **Security Issues Found**: List all sensitive information discovered
2. **Files Modified**: Show what changes were made to each file
3. **Recommended Actions**: Additional security measures to implement
4. **Verification Checklist**: Steps to ensure the cleanup was successful

Start by scanning the entire codebase and provide your findings before making any changes.