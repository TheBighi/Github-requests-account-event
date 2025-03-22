import requests

i = 0

account = input("Which github account activity would u like to look at?: ")
print("")

r = requests.get(f'https://api.github.com/users/{account}/events')
r.json()

events = r.json()

for event in events:
    i += 1
    if i <= 3:
        login = event["actor"]["login"]
        repo_name = event["repo"]["name"]
        commits = event["payload"].get("commits", [])
        commit_message = commits[0]["message"] if commits else "No commits found"
        print(f"Account name: {login}")
        print(f"Repo Name: {repo_name}")
        print(f"Commit Message: {commit_message}")
        print("-----------------")
    else:
        break