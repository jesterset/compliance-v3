import random
import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from app.constants.constants import COMPLIANCE_RULES_WITH_PLACEHOLDERS

# Function to generate labeled data (queries and labels)
def generate_data_with_labels(templates, num_samples=100):
    queries_and_labels = set()  # Use a set to store unique (query, topic) pairs
    while len(queries_and_labels) < num_samples:
        topic = random.choice(list(templates.keys()))  # Select topic as label
        template = random.choice(templates[topic])  # Select query template
        query = template.format(
            company=random.choice(["Tesla", "Apple", "Amazon", "Google", "Microsoft", "Goldman Sachs", "Pfizer", "JP Morgan", "ExxonMobil", "Chevron", "Meta", "Coca-Cola"]),
            time_period=random.choice(["next quarter", "next fiscal year", "this month", "the next 5 years"]),
            sector=random.choice(["automotive", "tech", "financial", "energy", "pharmaceutical", "consumer goods"]),
            market_conditions=random.choice(["rising inflation", "global instability", "market volatility"]),
            event=random.choice(["merger", "acquisition", "earnings report", "restructuring"]),
            document=random.choice(["report", "contract", "whitepaper", "presentation"]),
            action=random.choice(["skyrocket", "double", "decrease", "triple"]),
            price=random.choice(["$1000", "$1500", "2000", "fifty"]),
            location=random.choice(["New York", "London", "Tokyo", "Paris"]),
            country=random.choice(["the United States", "France", "Germany", "Japan"]),
            years=random.randint(1, 20),
            information_type=random.choice(["confidential", "insider", "non-public"]),
            regulatory_body=random.choice(["SEC", "FTC", "FCA", "EU Commission"]),
            confidentiality=random.choice(["confidential", "non-public", "privileged"]),
            insider=random.choice(["insider", "internal", "secret"]),
            merger_acquisition=random.choice(["merger", "acquisition"]),
            contracts=random.choice(["contracts", "agreements"]),
            no_risk=random.choice(["no risk", "little risk"]),
            risk_free=random.choice(["risk-free", "guaranteed"]),
            high_return=random.choice(["high returns", "massive gains"]),
            promise=random.choice(["promise", "guarantee"]),
            gains=random.choice(["massive gains", "great returns"]),
            no_downside=random.choice(["no downside", "no risk"])
        )

        # Add query and its corresponding topic as a tuple to the set
        queries_and_labels.add((query, topic))

    # Return the unique set of queries as a list
    return list(queries_and_labels)


# Build the Aho-Corasick automaton using the generated data
# automaton = build_aho_corasick_automaton_from_labels(training_queries_with_labels)

# Function to classify a query's topic using a trained model (logistic regression)
def classify_topic(query, clf, vectorizer):
    X_query = vectorizer.transform([query])
    predicted_topic = clf.predict(X_query)
    return predicted_topic[0]

# Train a simple logistic regression model for topic classification
def train_topic_classifier(queries_with_labels):
    queries = [item[0] for item in queries_with_labels]
    labels = [item[1] for item in queries_with_labels]

    # Vectorize the queries
    vectorizer = TfidfVectorizer()
    X_train = vectorizer.fit_transform(queries)

    # Train the logistic regression classifier
    clf = LogisticRegression().fit(X_train, labels)
    return clf, vectorizer

# Train the classifier