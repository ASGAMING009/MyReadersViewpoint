import instaloader
from collections import Counter
import time
import os
from dotenv import load_dotenv

load_dotenv()

def get_related_hashtags(base_tag, max_posts=50):
    """
    Scrapes Instagram for a base hashtag and finds other tags commonly used with it.
    """
    # Initialize Instaloader
    L = instaloader.Instaloader()

    # Load credentials from environment variables
    username = os.getenv("INSTA_USERNAME")
    password = os.getenv("INSTA_PASSWORD")
    
    if not username or not password:
        print("[Error]: Please set INSTA_USERNAME and INSTA_PASSWORD environment variables.")
        return None

    try:
        L.login(username, password)
    except Exception as e:
        print(f"[Error]: Login failed. {e}")
        return None

    print(f"--- Searching for hashtags related to #{base_tag} ---")
    print(f"Analyzing the last {max_posts} posts... (This may take a moment)")

    related_tags = []
    
    try:
        hashtag_data = instaloader.Hashtag.from_name(L.context, base_tag)

        count = 0
        for post in hashtag_data.get_posts():
            if count >= max_posts:
                break
            
            related_tags.extend([tag.lower() for tag in post.caption_hashtags if tag.lower() != base_tag.lower()])
            
            count += 1
            
            if count % 10 == 0:
                print(f"Scanned {count} posts...")
                
            time.sleep(1) 

    except Exception as e:
        print(f"\n[Error]: Could not fetch posts. Instagram might require login or is rate-limiting you.")
        print(f"System Message: {e}")
        return None

    if not related_tags:
        print(f"\n[Warning]: No related hashtags found for #{base_tag}")
        return None

    tag_counts = Counter(related_tags)

    print(f"\n--- Top 20 Hashtags for #{base_tag} Edits ---")
    print(f"{'HASHTAG':<30} | {'FREQUENCY'}")
    print("-" * 45)
    
    for tag, freq in tag_counts.most_common(20):
        print(f"#{tag:<29} | {freq}")
    
    return tag_counts

if __name__ == "__main__":
    target_tag = "wagurikaoruko" 
    get_related_hashtags(target_tag, max_posts=30)