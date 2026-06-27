# Mini Project: GitHub Repository Analyzer (with Virtual Environment)

We will build a project using:

* `requests` → API call
* `pandas` → data handling
* `matplotlib` → visualization
* `datetime` → timestamps (built-in)

---

# Step 1: Create Project Folder

```bash
mkdir github-repo-analyzer
cd github-repo-analyzer
```

---

# Step 2: Create Virtual Environment

## Create venv

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows (CMD)

```bash
venv\Scripts\activate
```

### Windows (PowerShell)

```bash
venv\Scripts\Activate.ps1
```

---

## You will know it's active when:

```bash
(venv) your-terminal-prompt
```

---

# Step 3: Install Required Libraries

```bash
pip install requests pandas matplotlib
```

(Optional)

```bash
pip freeze > requirements.txt
```

---

# Step 4: Create Python File

```bash
touch main.py
```

---

# Step 5: Write the Code (main.py)

```python id="ghproj01"
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
```

---

# ▶ Step 6: Run the Project

```bash
python main.py
```

---

# Step 7: Save Dependencies (Best Practice)

```bash
pip freeze > requirements.txt
```

Now your project can be shared and recreated easily.

---

# Final Project Structure

```
github-repo-analyzer/
│
├── venv/
├── main.py
├── requirements.txt
└── github_report_octocat_2026-06-27_....csv
```

---

# What You Learn from This Setup

## Virtual Environment

* Isolates project dependencies
* Prevents version conflicts

## requests

* API integration (real-world skill)

## pandas

* Data transformation & analysis

## matplotlib

* Visualization

## datetime

* Report timestamping
