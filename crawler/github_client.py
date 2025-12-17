import requests
import time

GITHUB_API = "https://api.github.com/graphql"

def fetch_repos(token, cursor=None):
    query = """
    query ($cursor: String) {
      search(query: "stars:>1", type: REPOSITORY, first: 20, after: $cursor) {
        pageInfo {
          hasNextPage
          endCursor
        }
        nodes {
          ... on Repository {
            nameWithOwner
            stargazerCount
          }
        }
      }
    }
    """

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(
        GITHUB_API,
        json={"query": query, "variables": {"cursor": cursor}},
        headers=headers
    )

    if response.status_code != 200:
        time.sleep(5)
        return None

    return response.json()
