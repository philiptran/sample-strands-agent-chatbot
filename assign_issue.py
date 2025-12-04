#!/usr/bin/env python3
"""
Script to assign the authenticated user to a GitHub issue using the GitHub API.

Usage:
    export GITHUB_TOKEN=<your_github_token>
    python3 assign_issue.py

Or:
    python3 assign_issue.py --token <your_github_token>
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.error


def get_authenticated_user(token):
    """Get the authenticated user's login."""
    url = "https://api.github.com/user"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "GitHub-Issue-Assigner"
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data.get("login")
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"Error getting authenticated user: {e.code} {e.reason}")
        print(f"Response: {error_body}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def assign_issue(owner, repo, issue_number, token, assignee):
    """Assign a user to a GitHub issue."""
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/assignees"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "GitHub-Issue-Assigner",
        "Content-Type": "application/json"
    }
    
    data = json.dumps({"assignees": [assignee]}).encode('utf-8')
    
    try:
        req = urllib.request.Request(url, data=data, headers=headers, method='POST')
        with urllib.request.urlopen(req) as response:
            response_data = json.loads(response.read().decode())
            return True, response_data
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"Error assigning issue: {e.code} {e.reason}")
        print(f"Response: {error_body}")
        return False, None
    except Exception as e:
        print(f"Error: {e}")
        return False, None


def main():
    parser = argparse.ArgumentParser(
        description="Assign the authenticated user to a GitHub issue"
    )
    parser.add_argument(
        "--token",
        help="GitHub personal access token (or use GITHUB_TOKEN env var)",
        default=None
    )
    parser.add_argument(
        "--owner",
        default="philiptran",
        help="Repository owner (default: philiptran)"
    )
    parser.add_argument(
        "--repo",
        default="sample-strands-agent-chatbot",
        help="Repository name (default: sample-strands-agent-chatbot)"
    )
    parser.add_argument(
        "--issue",
        type=int,
        default=3,
        help="Issue number (default: 3)"
    )
    
    args = parser.parse_args()
    
    # Get token from args or environment
    token = args.token or os.environ.get("GITHUB_TOKEN")
    
    if not token:
        print("Error: GitHub token is required!")
        print("Provide it via --token argument or GITHUB_TOKEN environment variable")
        sys.exit(1)
    
    print(f"Target: https://github.com/{args.owner}/{args.repo}/issues/{args.issue}")
    print()
    
    # Get authenticated user
    print("Step 1: Getting authenticated user...")
    username = get_authenticated_user(token)
    
    if not username:
        print("Failed to get authenticated user. Check your token.")
        sys.exit(1)
    
    print(f"Authenticated as: {username}")
    print()
    
    # Assign the issue
    print(f"Step 2: Assigning {username} to issue #{args.issue}...")
    success, response_data = assign_issue(
        args.owner,
        args.repo,
        args.issue,
        token,
        username
    )
    
    if success:
        print("✓ Successfully assigned to issue!")
        print()
        print("Verification:")
        if response_data and "assignees" in response_data:
            assignees = [a["login"] for a in response_data["assignees"]]
            print(f"  Current assignees: {', '.join(assignees)}")
            if username in assignees:
                print(f"  ✓ {username} is now assigned to the issue")
        print()
        print(f"View issue at: https://github.com/{args.owner}/{args.repo}/issues/{args.issue}")
    else:
        print("✗ Failed to assign to issue")
        sys.exit(1)


if __name__ == "__main__":
    main()
