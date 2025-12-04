# Manual GitHub API Call Example

If you prefer to make the API call manually without using the provided scripts, here's how:

## Step 1: Get Your Username

```bash
curl -H "Authorization: token YOUR_GITHUB_TOKEN" \
     -H "Accept: application/vnd.github.v3+json" \
     https://api.github.com/user | grep '"login"'
```

## Step 2: Assign Yourself to the Issue

Replace `YOUR_GITHUB_TOKEN` and `YOUR_USERNAME` with your actual values:

```bash
curl -X POST \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Content-Type: application/json" \
  -d '{"assignees":["YOUR_USERNAME"]}' \
  https://api.github.com/repos/philiptran/sample-strands-agent-chatbot/issues/3/assignees
```

## Step 3: Verify the Assignment

Check the issue page:
https://github.com/philiptran/sample-strands-agent-chatbot/issues/3

Or use the API:

```bash
curl -H "Authorization: token YOUR_GITHUB_TOKEN" \
     -H "Accept: application/vnd.github.v3+json" \
     https://api.github.com/repos/philiptran/sample-strands-agent-chatbot/issues/3 | grep assignees -A 10
```

## Complete One-Liner Example

```bash
# Set your token
export GITHUB_TOKEN="your_github_token_here"

# Get username and assign in one go
USERNAME=$(curl -s -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user | grep -o '"login":"[^"]*"' | cut -d'"' -f4) && \
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Content-Type: application/json" \
  -d "{\"assignees\":[\"$USERNAME\"]}" \
  https://api.github.com/repos/philiptran/sample-strands-agent-chatbot/issues/3/assignees && \
echo "✓ Assigned $USERNAME to issue #3"
```
