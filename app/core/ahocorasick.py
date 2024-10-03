import string
import ahocorasick

def build_aho_corasick_automaton_from_labels(labeled_data):
    automaton = ahocorasick.Automaton()

    for query, topic in labeled_data:
        tokens = query.lower().translate(str.maketrans('', '', string.punctuation)).split()  # Tokenize the query

        # Add each token to the automaton with the associated topic (label)
        for token in tokens:
            automaton.add_word(token, (topic, token))

    automaton.make_automaton()  # Finalize the automaton
    return automaton

# Function to detect non-compliance using the Aho-Corasick automaton
def detect_non_compliance_aho_corasick(automaton, query):
    detected_rules = {}
    query_lower = query.lower().translate(str.maketrans('', '', string.punctuation))

    for end_index, (rule, term) in automaton.iter(query_lower):
        if rule not in detected_rules:
            detected_rules[rule] = []
        detected_rules[rule].append(term)

    return detected_rules if detected_rules else None