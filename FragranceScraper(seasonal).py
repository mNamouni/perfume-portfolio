import praw
import pandas as pd
import time
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import spacy
from collections import Counter
import matplotlib.pyplot as plt

# Setup: Download NLTK data and load spaCy model
nltk.download('vader_lexicon')
nlp = spacy.load("en_core_web_sm")
sid = SentimentIntensityAnalyzer()

# Configure Reddit API credentials (replace with your actual credentials)
reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent=""
)

# Define parameters
seasons = ["Winter", "Summer", "Spring", "Autumn"]
subreddit_name = "fragrance"
post_limit = 250
comment_limit = 50

all_posts_data = []
all_comments_data = []

# Loop through each season
for season in seasons:
    print(f"Collecting data for {season}...")
    posts_data = []
    comments_data = []
    
    # Use the season as the query (you can adjust the query format if needed)
    query = season
    
    for submission in reddit.subreddit(subreddit_name).search(query, limit=post_limit, sort="relevance"):
        # Collect post details
        post_details = {
            'post_id': submission.id,
            'title': submission.title,
            'body': submission.selftext,
            'upvotes': submission.score,
            'timestamp': submission.created_utc,
            'url': submission.url,
            'num_comments': submission.num_comments,
            'season': season  # Tag the post with the season
        }
        posts_data.append(post_details)
        
        # Get top-level comments (ignoring nested replies)
        submission.comments.replace_more(limit=0)
        count = 0
        for comment in submission.comments:
            if comment.parent_id.startswith("t3_"):
                comments_data.append({
                    'post_id': submission.id,
                    'comment_id': comment.id,
                    'comment_body': comment.body,
                    'comment_score': comment.score,
                    'comment_timestamp': comment.created_utc,
                    'season': season  # Tag the comment with the season
                })
                count += 1
                if count >= comment_limit:
                    break
        time.sleep(2)  # Respect API rate limits
    
    # Convert to DataFrames for this season and append to lists
    season_posts_df = pd.DataFrame(posts_data)
    season_comments_df = pd.DataFrame(comments_data)
    all_posts_data.append(season_posts_df)
    all_comments_data.append(season_comments_df)

# Combine data from all seasons into single DataFrames
combined_posts_df = pd.concat(all_posts_data, ignore_index=True)
combined_comments_df = pd.concat(all_comments_data, ignore_index=True)

# Save the combined data to CSV files if desired
combined_posts_df.to_csv("combined_posts.csv", index=False)
combined_comments_df.to_csv("combined_comments.csv", index=False)

print("Data collection complete. Combined data saved to CSV.")

# (Optional) Continue with further processing such as sentiment analysis and entity extraction.
