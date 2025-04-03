### ------------> Perfume Analysis Query Engine <------------

A data analysis project that leverages Reddit data from the [r/fragrance](https://www.reddit.com/r/fragrance/) subreddit to build an interactive query engine. This engine allows users to input a search term (e.g., "Love") and returns insights including:

- A collection of posts and top-level comments related to the query.
- Sentiment analysis on the collected data using NLTK’s VADER.
- Extraction of fragrance-related entities (brands, products) using spaCy.
- Visualizations (bar charts, histograms) to show common entities and sentiment distributions.

The ultimate goal is to display which fragrances are most associated with a given query and whether they tend to elicit positive or negative responses.

#   -> Features

- **Data Collection**: Scrapes posts and up to 20 top-level comments from the r/fragrance subreddit based on a specific query.
- **Data Cleaning & Preprocessing**: Combines and cleans text from posts and comments.
- **Sentiment Analysis**: Computes sentiment scores for both posts and comments using VADER.
- **Entity Extraction**: Uses spaCy to extract key fragrance-related entities (e.g., brands and products).
- **Visualization**: Generates visualizations to display the most common entities and sentiment distributions.
- **Interactive Query Engine (Future Work)**: Plans to develop a web interface where users can input a query and view real-time results.

 #  -> Requirements

- Python 3.6+
- [PRAW](https://praw.readthedocs.io/)
- [Pandas](https://pandas.pydata.org/)
- [NLTK](https://www.nltk.org/)
- [spaCy](https://spacy.io/)
- [Matplotlib](https://matplotlib.org/)

# Setup & Usage

Clone the Repository:

      git clone https://github.com/yourusername/perfume-analysis-query-engine.git
      cd perfume-analysis-query-engine



Configure Reddit API Credentials:
Open the Python files (e.g., queryanalysis.py) and replace the placeholders for client_id, client_secret, and user_agent with your actual credentials from Reddit. You can create a Reddit app here.
Run the Analysis:
Using Jupyter Notebook:
Launch Jupyter Notebook and open Perfume_Analysis.ipynb: jupyter notebook

Run the notebook cells sequentially to execute the full pipeline.
Using a Python Script:
Alternatively, run the main script: python queryanalysis.py

## The script will collect data, perform sentiment analysis and entity extraction, and generate CSV files and visualizations.
View the Output:
CSV files with the collected posts and comments (e.g., winter_fragrance_posts.csv, winter_fragrance_comments.csv) will be saved.
The console will display average sentiment scores and common fragrance-related entities.
Visualizations (bar charts and histograms) will be generated to illustrate the analysis.
File Structure

Perfume_Analysis.ipynb – Jupyter Notebook containing the entire analysis pipeline.
queryanalysis.py – Python script that performs data collection, sentiment analysis, and entity extraction.
visualisations.py – (Optional) Python script dedicated to visualizing analysis results.
README.md – This file.
CSV files generated during the process (e.g., winter_fragrance_posts.csv, winter_fragrance_comments.csv).
Future Work

Web Interface: Build an interactive web application (using Flask, Django, or Streamlit) that allows users to input queries and view dynamic analysis results.
Enhanced Entity Extraction: Refine entity extraction by filtering out noise and possibly using a custom dictionary of fragrance-related terms.
Advanced Sentiment Analysis: Explore additional sentiment analysis methods and compare results.
Scalability Improvements: Implement caching and incremental data updates to handle larger datasets and real-time queries.
Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, please fork the repository, create a new branch, and submit a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements

PRAW for accessing Reddit's API.
NLTK and VADER for sentiment analysis.
spaCy for entity extraction.
Matplotlib for visualization.



