#!/bin/bash
# Script to assign the authenticated user to a GitHub issue using the GitHub API
#
# Usage:
#   export GITHUB_TOKEN=<your_github_token>
#   ./assign_issue.sh
#
# Or:
#   GITHUB_TOKEN=<your_github_token> ./assign_issue.sh

set -e

# Configuration
OWNER="${GITHUB_OWNER:-philiptran}"
REPO="${GITHUB_REPO:-sample-strands-agent-chatbot}"
ISSUE_NUMBER="${GITHUB_ISSUE:-3}"

# Check if token is provided
if [ -z "$GITHUB_TOKEN" ]; then
    echo "Error: GITHUB_TOKEN environment variable is required!"
    echo ""
    echo "Usage:"
    echo "  export GITHUB_TOKEN=<your_github_token>"
    echo "  ./assign_issue.sh"
    exit 1
fi

echo "Target: https://github.com/${OWNER}/${REPO}/issues/${ISSUE_NUMBER}"
echo ""

# Step 1: Get authenticated user
echo "Step 1: Getting authenticated user..."
USER_RESPONSE=$(curl -s -H "Authorization: token ${GITHUB_TOKEN}" \
    -H "Accept: application/vnd.github.v3+json" \
    -H "User-Agent: GitHub-Issue-Assigner" \
    https://api.github.com/user)

USERNAME=$(echo "$USER_RESPONSE" | grep -o '"login":"[^"]*"' | cut -d'"' -f4)

if [ -z "$USERNAME" ]; then
    echo "Error: Failed to get authenticated user"
    echo "Response: $USER_RESPONSE"
    exit 1
fi

echo "Authenticated as: $USERNAME"
echo ""

# Step 2: Assign the issue
echo "Step 2: Assigning $USERNAME to issue #${ISSUE_NUMBER}..."
ASSIGN_RESPONSE=$(curl -s -w "\n%{http_code}" \
    -X POST \
    -H "Authorization: token ${GITHUB_TOKEN}" \
    -H "Accept: application/vnd.github.v3+json" \
    -H "User-Agent: GitHub-Issue-Assigner" \
    -H "Content-Type: application/json" \
    -d "{\"assignees\":[\"${USERNAME}\"]}" \
    "https://api.github.com/repos/${OWNER}/${REPO}/issues/${ISSUE_NUMBER}/assignees")

# Extract HTTP status code (last line)
HTTP_CODE=$(echo "$ASSIGN_RESPONSE" | tail -n1)
RESPONSE_BODY=$(echo "$ASSIGN_RESPONSE" | sed '$d')

if [ "$HTTP_CODE" -eq 201 ] || [ "$HTTP_CODE" -eq 200 ]; then
    echo "✓ Successfully assigned to issue!"
    echo ""
    echo "Verification:"
    
    # Extract assignees from response
    ASSIGNEES=$(echo "$RESPONSE_BODY" | grep -o '"login":"[^"]*"' | cut -d'"' -f4 | tr '\n' ', ' | sed 's/,$//')
    
    if [ ! -z "$ASSIGNEES" ]; then
        echo "  Current assignees: $ASSIGNEES"
    fi
    
    if echo "$RESPONSE_BODY" | grep -q "\"login\":\"${USERNAME}\""; then
        echo "  ✓ $USERNAME is now assigned to the issue"
    fi
    
    echo ""
    echo "View issue at: https://github.com/${OWNER}/${REPO}/issues/${ISSUE_NUMBER}"
else
    echo "✗ Failed to assign to issue (HTTP $HTTP_CODE)"
    echo "Response: $RESPONSE_BODY"
    exit 1
fi
