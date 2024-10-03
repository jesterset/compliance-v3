from app.constants.constants import COMPLIANCE_RULES_WITH_PLACEHOLDERS
from app.utils.data_utils import generate_data_with_labels, train_topic_classifier

# Generate a dataset of 1000 queries with compliance rule labels
training_queries_with_labels = generate_data_with_labels(COMPLIANCE_RULES_WITH_PLACEHOLDERS, num_samples=10)

clf, vectorizer = train_topic_classifier(training_queries_with_labels)
