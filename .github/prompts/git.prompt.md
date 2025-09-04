---
mode: agent
tools: ['codebase', 'terminal', 'findTestFiles']
description: 'Automated git workflow with project security cleanup before commit'
---

# Automated Git Workflow with Security Cleanup

Your task is to perform a complete git workflow that includes project security cleanup before committing code. This ensures no sensitive information is accidentally committed to the repository.

## Workflow Overview

1. **Pre-commit Security Scan** - Use clean-project.prompt.md to identify and fix security issues
2. **Code Quality Check** - Run tests and linting
3. **Git Operations** - Add, commit, and optionally push changes
4. **Verification** - Ensure everything was processed correctly

## Step 1: Project Security Cleanup

First, execute the security cleanup process by following the instructions in `clean-project.prompt.md`:

1. Scan #codebase for sensitive information:
   - API keys, tokens, passwords, secrets
   - Database connection strings
   - Personal information (emails, phone numbers)
   - Internal URLs, IP addresses
   - Company-specific data

2. Review and clean sensitive files:
   - Configuration files (`.env`, `config.js`)
   - Documentation with real credentials
   - Test files with actual data
   - Log files and outputs

3. Ensure security configuration:
   - Verify `.gitignore` covers sensitive patterns
   - Check `.copilotignore` excludes private data
   - Confirm no hardcoded secrets in source code

## Step 2: Code Quality Checks

Run quality checks before committing:

```bash
# Run tests to ensure functionality
npm test

# Check code style and format
npm run lint

# Auto-fix style issues if possible
npm run fix
```

## Step 3: Git Operations

Perform git operations with proper commit messages:

```bash
# Check git status
git status

# Stage all changes
git add .

# Create meaningful commit message
git commit -m "feat: [brief description]

- [specific change 1]
- [specific change 2]
- Security: cleaned sensitive information
- Tests: verified functionality"

# Optionally push to remote (ask user first)
git push origin [current-branch]
```

## Commit Message Guidelines

Follow conventional commit format:
- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks
- `security:` - Security improvements

## Interactive Prompts

Ask the user for confirmation at key steps:

1. **After Security Scan**: "Found [X] potential security issues. Proceed with cleanup? (y/n)"
2. **Before Commit**: "Ready to commit [X] files with message: '[message]'. Continue? (y/n)"
3. **Push Decision**: "Commit successful. Push to remote repository? (y/n)"

## Error Handling

If any step fails:
- **Test Failures**: Show failed tests, ask if user wants to commit anyway
- **Lint Errors**: Show errors, attempt auto-fix, or ask user to fix manually
- **Security Issues**: Provide specific recommendations for each issue found
- **Git Errors**: Explain the issue and suggest solutions

## Output Format

Provide a structured summary:

```markdown
## 🔍 Security Scan Results
- [X] issues found and resolved
- [List of specific changes made]

## ✅ Code Quality Check
- Tests: [PASSED/FAILED] ([X] tests run)
- Linting: [PASSED/FAILED] ([X] issues found/fixed)

## 📝 Git Operations
- Files staged: [X]
- Commit message: "[message]"
- Commit hash: [hash]
- Push status: [SUCCESS/SKIPPED/FAILED]

## 🎯 Summary
[Brief overview of what was accomplished]
```

## Special Considerations

### For Educational Projects
- Preserve learning examples while removing real credentials
- Replace with generic placeholders (YOUR_API_KEY, example.com)
- Maintain code functionality for demo purposes

### For Production Code
- Be more strict about security issues
- Require manual review of sensitive changes
- Create separate commits for security fixes

### Team Collaboration
- Use clear, descriptive commit messages
- Include issue/ticket numbers if applicable
- Consider creating pull requests for major changes

## Pre-execution Checklist

Before running this workflow, verify:
- [ ] Current working directory is a git repository
- [ ] User has proper git configuration (name, email)
- [ ] No uncommitted critical changes that might be lost
- [ ] Clean-project.prompt.md is available and accessible

## Success Criteria

A successful run should:
- ✅ Complete security scan with no sensitive data in git
- ✅ Pass all code quality checks (or get user approval for failures)  
- ✅ Create a meaningful commit with proper message format
- ✅ Maintain project functionality and educational value
- ✅ Provide clear feedback on all operations performed

Start by asking the user if they want to proceed with the full automated workflow, or if they prefer to run individual steps interactively.
