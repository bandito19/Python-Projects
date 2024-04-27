from difflib import get_close_matches

def get_best_matches(user_question, questions):
    questions = [q for q in questions]
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    
    if matches:
        return matches[0]
    
    