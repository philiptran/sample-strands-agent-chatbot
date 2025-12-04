# GitHub API Call Reference for Issue Assignment

## Task Summary
Assign the authenticated user to issue #3 in philiptran/sample-strands-agent-chatbot

## API Endpoint Details

### 1. Get Authenticated User
**Endpoint:** `GET https://api.github.com/user`

**Headers:**
```
Authorization: token <GITHUB_TOKEN>
Accept: application/vnd.github.v3+json
User-Agent: GitHub-Issue-Assigner
```

**Response Example:**
```json
{
  "login": "username",
  "id": 12345,
  "name": "User Name",
  ...
}
```

### 2. Add Assignees to Issue
**Endpoint:** `POST https://api.github.com/repos/philiptran/sample-strands-agent-chatbot/issues/3/assignees`

**Headers:**
```
Authorization: token <GITHUB_TOKEN>
Accept: application/vnd.github.v3+json
User-Agent: GitHub-Issue-Assigner
Content-Type: application/json
```

**Request Body:**
```json
{
  "assignees": ["username"]
}
```

**Response Example (Success - 201 Created):**
```json
{
  "id": 123456789,
  "number": 3,
  "title": "Issue Title",
  "assignees": [
    {
      "login": "username",
      "id": 12345,
      ...
    }
  ],
  ...
}
```

## Implementation Files

1. **assign_issue.sh** - Bash script using curl
2. **assign_issue.py** - Python script using urllib
3. **ASSIGN_ISSUE_INSTRUCTIONS.md** - Complete usage documentation

## Verification

The scripts verify successful assignment by:
1. Checking the HTTP response code (200 or 201)
2. Parsing the response to confirm the user is in the assignees list
3. Displaying the issue URL for manual verification

## Security Notes

- GitHub token is passed via environment variable or command-line argument
- Scripts never log or persist the token
- Token requires `repo` or `public_repo` scope
