import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# -----------------------------
# CONFIG
# -----------------------------
username = "octocat"   # change GitHub username

# -----------------------------
# Step 1: Fetch GitHub data
# -----------------------------
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)

if response.status_code != 200:
    print("API request failed")
    exit()

repos = response.json()

# -----------------------------
# Step 2: Transform data
# -----------------------------
data = []
for repo in repos:
    data.append({
        "name": repo["name"],
        "stars": repo["stargazers_count"],
        "forks": repo["forks_count"],
        "language": repo["language"],
        "created_at": repo["created_at"]
    })

df = pd.DataFrame(data)

# -----------------------------
# Step 3: Analysis
# -----------------------------
print("\n=== REPOSITORY DATA ===")
print(df)

print("\n=== SUMMARY ===")
print("Total Repos:", len(df))
print("Total Stars:", df["stars"].sum())

if not df.empty:
    top_repo = df.loc[df["stars"].idxmax(), "name"]
    print("Most Starred Repo:", top_repo)

# -----------------------------
# Step 4: Visualization
# -----------------------------
plt.figure(figsize=(10, 5))
plt.bar(df["name"], df["stars"])

plt.title(f"{username} GitHub Repo Stars")
plt.xlabel("Repository")
plt.ylabel("Stars")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# -----------------------------
# Step 5: Save report
# -----------------------------
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

file_name = f"github_report_{username}_{timestamp}.csv"
df.to_csv(file_name, index=False)

print(f"\nReport saved: {file_name}")