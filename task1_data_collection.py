import requests
import time
import json
from datetime import datetime
import os

# Step 1: Categories and keywords
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}


# Step 2: Function to assign category
def get_category(title):
    title = title.lower()
    for category, keywords in categories.items():
        for word in keywords:
            if word in title:
                return category
    return None


# Step 3: Fetch top story IDs
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
headers = {"User-Agent": "TrendPulse/1.0"}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Failed to fetch story IDs")
    exit()

story_ids = response.json()[:500]

# Step 4: Collect data
data = []
category_count = {key: 0 for key in categories}

for story_id in story_ids:
    item_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"

    try:
        res = requests.get(item_url, headers=headers)
        story = res.json()

        if story is None or "title" not in story:
            continue

        category = get_category(story["title"])

        if category and category_count[category] < 25:
            category_count[category] += 1

            data.append({
                "post_id": story.get("id"),
                "title": story.get("title"),
                "category": category,
                "score": story.get("score", 0),
                "num_comments": story.get("descendants", 0),
                "author": story.get("by"),
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

        # stop when enough data
        if sum(category_count.values()) >= 125:
            break

    except:
        print("Error fetching story")
        continue

# Step 5: Save JSON
if not os.path.exists("data"):
    os.makedirs("data")

filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w") as f:
    json.dump(data, f, indent=4)

print(f"Collected {len(data)} stories. Saved to {filename}")

