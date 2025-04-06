📦 Seasonal Fragrance Scraper & Analyzer

This project is a Reddit-based scraping and analysis tool designed to extract, clean, and analyze seasonal fragrance data from r/fragrance. It captures both posts and comments using a loop across four seasons — Winter, Spring, Summer, Autumn — and aggregates mentions of fragrances for each, pairing them with sentiment scores to understand community perception.

🧪 Features
✅ Scrapes posts and comments using PRAW (Reddit API)
✅ Loops through all four major fragrance seasons
✅ Extracts fragrance names using basic NLP techniques
✅ Conducts sentiment analysis with VADER
✅ Aggregates results into a structured CSV with:
Season
Fragrance name
Frequency (mention count)
Average sentiment score
🗃️ Files
FragranceScraper(seasonal).py – Main scraper that collects seasonal fragrance mentions from Reddit posts and comments.
clean_aggregate_sentiment.py (to be added) – Cleans the scraped text, extracts entities (fragrance names), calculates sentiment, and saves seasonal fragrance insights into a CSV.
📂 Output Format
The final output file, aggregated_entities_by_season.csv, contains:
