import pandas as pd
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import spacy

# Download the VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

# Load spaCy's English model (make sure it's installed: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

# Initialize VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

def clean_text(text):
    """
    Clean text by encoding to UTF-8 (ignoring errors) and removing extra whitespace.
    """
    if pd.isnull(text):
        return ""
    cleaned = text.encode('utf-8', errors='ignore').decode('utf-8')
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

def extract_entities(text):
    """
    Use spaCy's NER to extract entities labeled as ORG or PRODUCT,
    which are likely to capture fragrance-related names.
    """
    doc = nlp(text)
    return [ent.text.strip() for ent in doc.ents if ent.label_ in ['ORG', 'PRODUCT']]

# -----------------------------
# Load the Combined CSV Files
# -----------------------------
# Combined Posts CSV with columns: post_id, title, body, upvotes, timestamp, url, num_comments, season
posts_df = pd.read_csv("combined_posts.csv", encoding="utf-8")

# Combined Comments CSV with columns: post_id, comment_id, comment_body, comment_score, comment_timestamp, season
comments_df = pd.read_csv("combined_comments.csv", encoding="utf-8")

# -----------------------------
# Process Posts Data
# -----------------------------
# Create 'full_text' from 'title' and 'body'
posts_df['full_text'] = (posts_df['title'].fillna('') + " " + posts_df['body'].fillna('')).apply(clean_text)
# Compute sentiment for each post
posts_df['sentiment'] = posts_df['full_text'].apply(lambda x: sid.polarity_scores(x)['compound'])
# Extract fragrance-related entities from the post text
posts_df['entities'] = posts_df['full_text'].apply(extract_entities)
posts_df['source'] = 'post'

# -----------------------------
# Process Comments Data
# -----------------------------
comments_df['cleaned_text'] = comments_df['comment_body'].apply(clean_text)
# Compute sentiment for each comment
comments_df['sentiment'] = comments_df['cleaned_text'].apply(lambda x: sid.polarity_scores(x)['compound'])
# Extract fragrance-related entities from the comment text
comments_df['entities'] = comments_df['cleaned_text'].apply(extract_entities)
comments_df['source'] = 'comment'

# -----------------------------
# Combine Posts and Comments
# -----------------------------
combined_df = pd.concat([
    posts_df[['season', 'sentiment', 'entities']],
    comments_df[['season', 'sentiment', 'entities']]
], ignore_index=True)

# -----------------------------
# Explode the Entities List
# -----------------------------
# This ensures each occurrence of an entity appears in its own row.
exploded_df = combined_df.explode('entities')

# Remove rows with empty or missing entity
exploded_df = exploded_df[exploded_df['entities'].notnull() & (exploded_df['entities'] != '')]

# -----------------------------
# Aggregate Data by Season and Entity
# -----------------------------
# Group by season and entity; count occurrences and compute average sentiment.
aggregated = exploded_df.groupby(['season', 'entities']).agg(
    count=('entities', 'size'),
    avg_sentiment=('sentiment', 'mean')
).reset_index()

# Sort the aggregated results by season and then by count descending
aggregated = aggregated.sort_values(['season', 'count'], ascending=[True, False])

# -----------------------------
# Save the Aggregated Results
# -----------------------------
aggregated.to_csv("aggregated_entities_by_season.csv", index=False, encoding='utf-8')

print("Aggregated results saved to 'aggregated_entities_by_season.csv'")
