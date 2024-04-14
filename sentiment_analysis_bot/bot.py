from dataclasses import dataclass
from textblob import TextBlob


@dataclass
class Mood:
    emoji: str
    sentiment: float


def get_mood(input_text, *, sensetivity):

    plolarity = TextBlob(input_text).sentiment.polarity

    friendly_thershold = sensetivity
    hostile_thershold = -sensetivity

    if plolarity >= friendly_thershold:
        return Mood("😊", plolarity)
    elif plolarity <= hostile_thershold:
        return Mood("😣", plolarity)
    else:
        return Mood("😐", plolarity)
    

def run_bot():
    print("Bot: Enter some text to perform sentiment analysis: ")
    while True:
        user_input = input("Text: ")    
        mood = get_mood(user_input, sensetivity=0.3)
        print(f'Bot: {mood.emoji} {mood.sentiment}')


if __name__=='__main__':
    run_bot()   