import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

# Define pairs of patterns and responses
patterns_and_responses = [
    (r"hi|hello|hey", ["Hello!", "Hey there!", "Hi!"]),
    (r"how are you?", ["I'm doing great, thank you!", "I'm fine, how about you?"]),
    (r"what is your name?", ["I am  arena chatbot to help you.", "I'm a bot"]),
    (r"quit", ["Goodbye!", "See you later!"]),
    (r"(.*)", ["Sorry, I don't understand that.", "Can you rephrase your question?"])
]

# Create the chatbot with the patterns and reflections (for basic pronoun replacements)
chatbot = Chat(patterns_and_responses, reflections)

# Start the chatbot conversation


def chat():
    print("Hi! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Bot:", response)
        if user_input.lower() == 'quit':
            break

# Start chatting


if __name__ == "__main__":
    chat()
