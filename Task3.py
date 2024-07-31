import random
import re

class Chatbot:
    def __init__(self):
        self.responses = {
            'hi' : [
                "Hey there, human! 👋",
                "Hello! ",
                "Hi! What's up? 🤪",
            ],
            'how are you': [
                "I'm a bunch of code, but I feel great! How about you? 😊",
                "Just a bit binary today, thanks for asking! How are you? 🤖",
                "Doing well, considering I'm stuck in a computer. 😅",
            ],
            'your name': [
                "I'm called FunnyBot, your humor companion! 😄",
                "I'm the chatbot with the best jokes, but you can call me FunnyBot. 🎭",
                "Name's FunnyBot, laughter's my game! 😆",
            ],
            'what can you do': [
                "I can chat, crack jokes, and maybe make you smile! 😁",
                "I'm here to chat and spread some laughs. Want to hear a joke? 😂",
                "I'm pretty good at being funny and not much else! Wanna chat? 🤓",
            ],
            'ok show some': [
                "Why did the scarecrow win an award? Because he was outstanding in his field! 😂",
                "Why don't scientists trust atoms? Because they make up everything! 😜",
                "I'm reading a book about anti-gravity. It's impossible to put down! 📚",
            ],
            'default': [
                "I'm not sure how to respond to that, but here's a joke: Why did the chicken join a band? Because it had the drumsticks! 🥁",
                "Hmm, I'm just a simple bot, can you rephrase that? Meanwhile, here's a fun fact: I have no idea what day it is! 🤷‍♂️",
                "I didn't get that, but did you know? I never forget a punchline! 😉",
            ],
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        for key in self.responses:
            if re.search(key, user_input):
                return random.choice(self.responses[key])
        return random.choice(self.responses['default'])

    def start_chat(self):
        print("ChatBot: Hello! I'm ChatBot, your companion. Type 'exit' to end the chat.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("ChatBot: Goodbye! Have a great day! 😊")
                break
            response = self.get_response(user_input)
            print(f"ChatBot: {response}")

if __name__ == "__main__":
    bot = Chatbot()
    bot.start_chat()
