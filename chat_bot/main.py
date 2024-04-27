from difflib import get_close_matches

def get_best_matches(user_question, questions):
    questions = [q for q in questions]
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    
    if matches:
        return matches[0]
    

def chat_bot(knowledge):
    while True:
        user_input = input("You: ")

        best_match = get_best_matches(user_input, knowledge)

        if answer := knowledge.get(best_match):
            print(f'Bot: {answer}')
        else:
            print("Bot: I don't understand.")



