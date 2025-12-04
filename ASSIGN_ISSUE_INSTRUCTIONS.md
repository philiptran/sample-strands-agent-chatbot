# GitHub Issue Assignment Instructions

This directory contains scripts to assign the authenticated user to issue #3 in the philiptran/sample-strands-agent-chatbot repository using the GitHub API.

## Prerequisites

You need a GitHub Personal Access Token with the following permissions:
- `repo` scope (full control of private repositories) or at minimum
- `public_repo` scope (for public repositories)

### Creating a GitHub Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a descriptive name (e.g., "Issue Assignment")
4. Select scopes: `repo` (or `public_repo` for public repos only)
5. Click "Generate token"
6. Copy the token (you won't be able to see it again!)

## Usage

### Option 1: Using the Bash Script (Recommended)

```bash
# Export your GitHub token
export GITHUB_TOKEN=your_github_token_here

# Run the script
cd /projects/sandbox/sample-strands-agent-chatbot
./assign_issue.sh
```

Or in one line:
```bash
GITHUB_TOKEN=your_github_token_here ./assign_issue.sh
```

### Option 2: Using the Python Script

```bash
# Export your GitHub token
export GITHUB_TOKEN=your_github_token_here

# Run the script
cd /projects/sandbox/sample-strands-agent-chatbot
python3 assign_issue.py
```

Or with command-line argument:
```bash
python3 assign_issue.py --token your_github_token_here
```

### Customizing Parameters

Both scripts support customization:

**Bash script (via environment variables):**
```bash
export GITHUB_TOKEN=your_token
export GITHUB_OWNER=philiptran
export GITHUB_REPO=sample-strands-agent-chatbot
export GITHUB_ISSUE=3
./assign_issue.sh
```

**Python script (via command-line arguments):**
```bash
python3 assign_issue.py \
  --token your_token \
  --owner philiptran \
  --repo sample-strands-agent-chatbot \
  --issue 3
```

## What the Scripts Do

1. **Authenticate**: Verify the GitHub token and retrieve the authenticated user's username
2. **Assign**: Make a POST request to GitHub's API to add the authenticated user as an assignee to the specified issue
3. **Verify**: Confirm that the assignment was successful by checking the API response

## Expected Output

```
Target: https://github.com/philiptran/sample-strands-agent-chatbot/issues/3

Step 1: Getting authenticated user...
Authenticated as: your-username

Step 2: Assigning your-username to issue #3...
✓ Successfully assigned to issue!

Verification:
  Current assignees: your-username
  ✓ your-username is now assigned to the issue

View issue at: https://github.com/philiptran/sample-strands-agent-chatbot/issues/3
```

## Troubleshooting

### "Failed to get authenticated user"
- Check that your token is valid and not expired
- Ensure the token has the correct permissions (repo or public_repo scope)

### "Failed to assign to issue (HTTP 404)"
- Verify that the issue number exists
- Check that the repository owner and name are correct
- Ensure your token has access to the repository

### "Failed to assign to issue (HTTP 403)"
- You may not have permission to assign users to this issue
- Check that the repository is public or that your token has access to private repos

## API Reference

- GitHub REST API Documentation: https://docs.github.com/en/rest
- Add assignees endpoint: `POST /repos/{owner}/{repo}/issues/{issue_number}/assignees`
