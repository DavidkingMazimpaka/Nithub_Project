# Sentiment Analysis System- Nithub Project

## Project Overview

This project is a sentiment analysis system that scrapes sentences from news articles, annotates them based on their sentiments, and deploys the trained model as a REST API using Flask. It also includes model optimization and A/B testing functionalities.

## Features

1. **Scraping:** Scrapes 200 sentences from an English news source.
2. **Annotation:** Annotates sentences based on their sentiments (positive, neutral, negative) using VADER.
3. **REST API:** Deploys the sentiment analysis model as a REST API using Flask.
4. **Model Optimization:** Optimizes the model for inference speed using a lighter architecture.
5. **A/B Testing:** Implements A/B testing to compare the performance of the recommendation system against a baseline model.

## Installation

### Prerequisites

- Python 3.10.11
- Virtualenv

### Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/nithyb_project.git
   cd nithyb_project
   ```

2. **Create a Virtual Environment:**
   ```sh
   python3.10 -m venv myenv
   ```

3. **Activate the Virtual Environment:**
   - On Windows:
     ```sh
     myenv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```sh
     source myenv/bin/activate
     ```

4. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

5. **Download NLTK VADER Lexicon:**
   ```sh
   python download_nltk_data.py
   ```

## Usage

### Scrape and Annotate Sentences

To scrape and annotate sentences, run the `scrapp_annotate.py` script:

```sh
python scrapp_annotate.py
```

### Run the FastAPI App

To start the FastAPI app for sentiment prediction, run:

```sh
python app.py or uvicorn app:app --reload
```

The app will be available at `http://127.0.0.1:8000`.

### Run A/B Testing

To start the FastAPI app for A/B testing, run:

```sh
python ab_testing.py
```

The app will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Predict Sentiment

- **URL:** `/predict`
- **Method:** `POST`
- **Data Params:** `{ "url": "<news_url>" }`
- **Success Response:**
  - **Code:** 200
  - **Content:** `[{ "sentence": "<sentence>", "sentiment": "<sentiment>" }, ...]`

### Example Request

```sh
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"url":"<news_article_url>"}'
```

## File Structure

```
.
├── scrapp_annotate.py
├── app.py
├── optimize_model.py
├── ab_testing.py
├── download_nltk_data.py
├── requirements.txt
└── README.md
```

## Authors

KingDavid Mazimpaka - [KingDavid Mazimpaka](https://github.com/DavidkingMazimpaka)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.


This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [NLTK](https://www.nltk.org/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Flask](https://flask.palletsprojects.com/)
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
