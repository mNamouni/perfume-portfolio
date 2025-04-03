------------> Perfume Analysis Query Engine <------------

A data analysis project that leverages Reddit data from the [r/fragrance](https://www.reddit.com/r/fragrance/) subreddit to build an interactive query engine. This engine allows users to input a search term (e.g., "Love") and returns insights including:

- A collection of posts and top-level comments related to the query.
- Sentiment analysis on the collected data using NLTK’s VADER.
- Extraction of fragrance-related entities (brands, products) using spaCy.
- Visualizations (bar charts, histograms) to show common entities and sentiment distributions.

The ultimate goal is to display which fragrances are most associated with a given query and whether they tend to elicit positive or negative responses.

   -> Features

- **Data Collection**: Scrapes posts and up to 20 top-level comments from the r/fragrance subreddit based on a specific query.
- **Data Cleaning & Preprocessing**: Combines and cleans text from posts and comments.
- **Sentiment Analysis**: Computes sentiment scores for both posts and comments using VADER.
- **Entity Extraction**: Uses spaCy to extract key fragrance-related entities (e.g., brands and products).
- **Visualization**: Generates visualizations to display the most common entities and sentiment distributions.
- **Interactive Query Engine (Future Work)**: Plans to develop a web interface where users can input a query and view real-time results.

  -> Requirements

- Python 3.6+
- [PRAW](https://praw.readthedocs.io/)
- [Pandas](https://pandas.pydata.org/)
- [NLTK](https://www.nltk.org/)
- [spaCy](https://spacy.io/)
- [Matplotlib](https://matplotlib.org/)

  -> Installation

You can install the required packages using pip:

```bash
pip install praw pandas nltk spacy matplotlib
python -m spacy download en_core_web_sm
