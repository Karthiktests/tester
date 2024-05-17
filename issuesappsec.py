# issuesappsec.
# importpy
import requests
import sys
import argparse
import os
import json

def create_issue(token, repo, title, body, assignee):
    url = f"https://api.github.com/repos/{repo}/issues"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {
        "title": title,
        "body": body,
        "assignee": assignee,
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Successfully created Issue")
    else:
        print(f"Could not create Issue, status code: {response.status_code}")
        print(response.text)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--issue_number", required=True)
    parser.add_argument("-j", "--comments", required=True)
    parser.add_argument("-l", "--github_id", required=True)
    parser.add_argument("-b", "--body", required=True)
    parser.add_argument("-g", "--githuburl", required=false)
    args = parser.parse_args()

    token = os.getenv("issue_token")
    repo = "Karthiktests/tester"  # Hardcode the repo here
    title = args.issue_number
    body = args.comments + "\n\n" + args.githuburl
    assignee = args.github_id
    create_issue(token, repo, title, body, assignee)

if __name__ == "__main__":
    main()