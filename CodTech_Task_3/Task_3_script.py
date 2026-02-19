import spacy
import random

# Load English model
nlp = spacy.load("en_core_web_sm")

# Predefined responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!"],
    "goodbye": ["Goodbye!", "See you later!", "Bye!"],
    "name": ["I am Sample AI chatbot built using spaCy","I am Sample AI chatbot","My name is Sample"],
    "intelligent": ["I am pretty intelligent to answer a specified questions. I am still learning","I will definitly answer to your basic questions. Sorry if I could't, because I am still learning"],
    "age" : ["Can't tell you the exact age of mine. But I not apart from your generation."] 

}

# Sample patterns
patterns = {
    "greeting": ["hello", "hi", "hey"],
    "goodbye": ["bye", "goodbye", "see you"],
    "name": ["your name", "who are you"],
    "intelligent": ["how much intelligent are you","How much knowledge do you have"],
    "age" : ["what is your age","your age","how old are you"]
}

def get_intent(user_input):
    doc = nlp(user_input)
    
    for intent, pattern_list in patterns.items():
        for pattern in pattern_list:
            if pattern in user_input.lower():
                return intent
    return None

print("AI Chatbot sample is running! Type 'quit' to exit.")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        print("Bot:", random.choice(responses["goodbye"]))
        break
    
    intent = get_intent(user_input)
    
    if intent:
        print("Bot:", random.choice(responses[intent]))
    else:
        print("Bot: Sorry, I don't understand that.")