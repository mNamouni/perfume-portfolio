📦 Seasonal Fragrance Scraper & Analyzer

This project is a Reddit-based scraping and analysis tool designed to extract, clean, and analyze seasonal fragrance data from r/fragrance. It captures both posts and comments using a loop across four seasons — Winter, Spring, Summer, Autumn — and aggregates mentions of fragrances for each, pairing them with sentiment scores to understand community perception.

🧪 Features

✅ Scrapes posts and comments using PRAW (Reddit API)

✅ Loops through all four major fragrance seasons

✅ Extracts fragrance names using basic NLP techniques

✅ Conducts sentiment analysis with VADER

✅ Aggregates results into a structured CSV with:

  • Season
  • Fragrance name
  • Frequency (mention count)
  • Average sentiment score

🗃️ Files

FragranceScraper(seasonal).py

 Main scraper that collects Reddit posts and comments related to each season. It tags the data by season and saves them into two CSV files: combined_posts.csv and combined_comments.csv.
 
Seasonalfragrance-cleaner.py

 Processes the scraped data, combining posts and comments, cleaning text, extracting fragrance mentions using simple NLP, and applying sentiment analysis with VADER. It outputs the final results grouped by season in aggregated_entities_by_season.csv.
 
📂 Output Format

The output CSV (aggregated_entities_by_season.csv) contains the following columns:

season – Winter, Spring, Summer, or Autumn
entities – Detected fragrance names
count – How many times each was mentioned
avg_sentiment – Average sentiment score per fragrance
