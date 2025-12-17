import os
from github_client import fetch_repos
from db import upsert_repo

TOKEN = os.getenv("GITHUB_TOKEN")

cursor = None
count = 0
LIMIT = 200   # demo limit

while count < LIMIT:
    data = fetch_repos(TOKEN, cursor)
    if not data:
        break

    repos = data["data"]["search"]["nodes"]
    for r in repos:
        upsert_repo(r["nameWithOwner"], r["stargazerCount"])
        count += 1

    page = data["data"]["search"]["pageInfo"]
    if not page["hasNextPage"]:
        break

    cursor = page["endCursor"]

print(f"Crawled {count} repositories")
