# GitHub Issue Assignment Tool

## Quick Start

To assign yourself to issue #3 in this repository:

1. **Get a GitHub token** (if you don't have one):
   - Go to: https://github.com/settings/tokens
   - Generate new token with `repo` or `public_repo` scope

2. **Run the assignment script**:
   ```bash
   export GITHUB_TOKEN=your_token_here
   ./assign_issue.sh
   ```
   
   Or use Python:
   ```bash
   export GITHUB_TOKEN=your_token_here
   python3 assign_issue.py
   ```

3. **Verify the assignment**:
   Visit: https://github.com/philiptran/sample-strands-agent-chatbot/issues/3

## Files in This Repository

- **assign_issue.sh** - Bash script (recommended)
- **assign_issue.py** - Python script (alternative)
- **ASSIGN_ISSUE_INSTRUCTIONS.md** - Detailed usage guide
- **EXAMPLE_MANUAL_API_CALL.md** - Manual curl examples

## What It Does

1. Authenticates with GitHub using your token
2. Retrieves your GitHub username
3. Assigns you to issue #3 via GitHub REST API
4. Confirms successful assignment

## Need Help?

See **ASSIGN_ISSUE_INSTRUCTIONS.md** for:
- Detailed setup instructions
- Troubleshooting guide
- Configuration options
- Manual API call examples

## Target Issue

**Repository:** philiptran/sample-strands-agent-chatbot  
**Issue:** #3  
**URL:** https://github.com/philiptran/sample-strands-agent-chatbot/issues/3
