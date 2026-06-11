# 🎬 Movie Recommender System

A content-based Movie Recommender System built using Python, Pandas, Scikit-Learn, and Streamlit.

🚀 Live Demo

Live Application: https://movie-recommender-system-production-633b.up.railway.app

Try the deployed application directly from the link above.

## Features

- Recommend movies similar to a selected movie
- Uses movie metadata such as genres, cast, crew, keywords, and overview
- Simple and interactive user interface
- Fast recommendation generation using cosine similarity

## Dataset

This project uses the following datasets:

- `tmdb_movies.csv`
- `tmdb_credits.csv`

Dataset Source:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

## Project Structure

```
Movie-Recommender-System/
│
├── app.py
├── requirements.txt
├── movie.pkl
├── movie_dict.pkl
├── tmdb_movies.csv
├── tmdb_credits.csv
├── movie_recommender_system.ipynb
├── README.md
└── .gitignore
```

## Important Note

The file `similarity.pkl` is **not included in this repository** because it is approximately 180 MB in size and exceeds GitHub's file size limit.

To run the project locally, you must generate `similarity.pkl` yourself by executing the notebook:

```
movie_recommender_system.ipynb
```

This notebook preprocesses the dataset and creates:

- `movie.pkl`
- `movie_dict.pkl`
- `similarity.pkl`

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Movie-Recommender-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Pickle

## Future Improvements

- Add movie posters using TMDB API
- Improve recommendation quality
- Deploy the application online
- Add filtering by genre, language, and rating

## Author

Aradhya Patel
