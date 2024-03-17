import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define the branch names you want to compare with
branch_names = ["IT", "Electrical"]

def get_branch_similarity(branch):
    """
    Calculate similarity between the given branch and predefined branch names.
    Returns the branch name with the highest similarity.
    """
    max_similarity = -1
    selected_branch = None
    for predefined_branch in branch_names:
        similarity = nlp(branch).similarity(nlp(predefined_branch))
        if similarity > max_similarity:
            max_similarity = similarity
            selected_branch = predefined_branch
    return selected_branch
