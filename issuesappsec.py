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
    parser.add_argument("-b", "--body", required=False)
    parser.add_argument("-g", "--github_url", required=True)
    parser.add_argument("-v", "--vulnerability_name", required=True)  # New argument
    parser.add_argument("-p", "--project", required=True)  # New argument
    args = parser.parse_args()

    token = os.getenv("issue_token")
    repo = "Karthiktests/tester"  # Hardcode the repo here
    title = args.issue_number
    body = args.comments + "\n\n" + args.github_url + "\n\nVulnerability Name: " + args.vulnerability_name + "\n\nProject: " + args.project  # Include new arguments in body
    assignee = args.github_id
    create_issue(token, repo, title, body, assignee)

if __name__ == "__main__":
    main()