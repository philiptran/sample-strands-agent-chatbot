# Quick Reference - GitHub Issue Assignment

## One-Line Commands

### Using Bash Script
```bash
export GITHUB_TOKEN=your_token && cd /projects/sandbox/sample-strands-agent-chatbot && ./assign_issue.sh
```

### Using Python Script
```bash
export GITHUB_TOKEN=your_token && cd /projects/sandbox/sample-strands-agent-chatbot && python3 assign_issue.py
```

### Manual curl (One-Liner)
```bash
export GITHUB_TOKEN=your_token && USERNAME=$(curl -s -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user | grep -o '"login":"[^"]*"' | cut -d'"' -f4) && curl -X POST -H "Authorization: token $GITHUB_TOKEN" -H "Accept: application/vnd.github.v3+json" -H "Content-Type: application/json" -d "{\"assignees\":[\"$USERNAME\"]}" https://api.github.com/repos/philiptran/sample-strands-agent-chatbot/issues/3/assignees
```

## File Overview

| File | Purpose | Size |
|------|---------|------|
| assign_issue.sh | Bash script to assign user | 2.6K |
| assign_issue.py | Python script to assign user | 4.4K |
| GITHUB_ISSUE_ASSIGNMENT_README.md | Quick start guide | 1.4K |
| ASSIGN_ISSUE_INSTRUCTIONS.md | Full usage guide | 3.3K |
| EXAMPLE_MANUAL_API_CALL.md | Manual curl examples | 1.7K |

## API Endpoints

1. **Get User**: `GET https://api.github.com/user`
2. **Assign**: `POST https://api.github.com/repos/philiptran/sample-strands-agent-chatbot/issues/3/assignees`

## Required Token Permissions

- `repo` (full repository access) OR
- `public_repo` (public repositories only)

## Get Token

https://github.com/settings/tokens

## Target Issue

https://github.com/philiptran/sample-strands-agent-chatbot/issues/3

## Verification

After running the script, check:
1. Script output shows "✓ Successfully assigned to issue!"
2. Visit issue URL to confirm assignment
3. Your username should appear in the "Assignees" section
