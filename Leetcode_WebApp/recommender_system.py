import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path

current_directory = Path(__file__).resolve().parent
csv_file_path = current_directory / "preprocessed_data.csv"

# Constants
ACCEPTANCE_WEIGHT = 0.3
ENGAGEMENT_WEIGHT = 0.5
SUBMISSION_WEIGHT = 0.2
SMOOTHING_FACTOR = 100000

class TextProcessor:
    def __init__(self, text_data):
        self.text_data = text_data
        self.text_preprocessor = TfidfVectorizer(stop_words='english')

    def preprocess_text_data(self):
        self.text_data.fillna('', inplace=True)
        return self.text_preprocessor.fit_transform(self.text_data)

class PopularityCalculator:
    def __init__(self, acceptance, engagement, submission):
        self.acceptance = acceptance
        self.engagement = engagement
        self.submission = submission

    def calculate_engagement_score(self):
        total_engagement = self.acceptance.fillna(0) + self.engagement.fillna(0) + SMOOTHING_FACTOR
        max_engagement = total_engagement.max()
        return total_engagement / max_engagement

    def normalize_series(self, series):
        return (series - series.min()) / (series.max() - series.min())

    def calculate_popularity_score(self):
        return (
            self.normalize_series(self.acceptance) * ACCEPTANCE_WEIGHT +
            self.normalize_series(self.engagement) * ENGAGEMENT_WEIGHT +
            self.normalize_series(self.submission) * SUBMISSION_WEIGHT
        )

class ProblemRecommender:
    @staticmethod
    def recommend_similar_problems(df, problem_id, X_processed, n=10):
        idx = df[df['id'] == problem_id].index
        if len(idx) == 0:
            return pd.DataFrame()  # Return empty DataFrame if problem_id is not found
        idx = idx[0]
        sim_scores = cosine_similarity(X_processed[idx], X_processed).flatten()
        # sim_scores[idx] = 0  # Exclude the problem itself
        sim_indices = sim_scores.argsort()[-n:][::-1]
        return df.iloc[sim_indices]

    @staticmethod
    def recommend_top_problems(df, n=10):
        return df.sort_values(by='popularity_score', ascending=False).head(n)

def recommender_system(problem_id=1):
    df = pd.read_csv(csv_file_path)
    df['topic_tags'] = df['topic_tags'].str.replace("'", "")

    text_processor = TextProcessor(df['problem_description'])
    X_processed = text_processor.preprocess_text_data()

    popularity_calculator = PopularityCalculator(df['acceptance'], df['likes'], df['submission'])
    df['popularity_score'] = popularity_calculator.calculate_popularity_score()

    content_based_recommendations = ProblemRecommender.recommend_similar_problems(df, problem_id=problem_id, X_processed=X_processed)
    popularity_based_recommendations = ProblemRecommender.recommend_top_problems(content_based_recommendations)

    return popularity_based_recommendations[['title', 'difficulty', 'topic_tags', 'problem_URL']]
