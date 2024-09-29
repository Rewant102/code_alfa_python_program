import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk

# Defining pairs to conversation
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1! How can I assist you today?", "Nice to meet you %1! What's on your mind?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!", "Hi! How can I help you today?",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created to assist you!", "My name doesn't matter, but I'm here to help!"]
    ],
    [
        r"how are you?",
        ["I'm just a bot, but I'm doing great! How about you?", "Doing good! Thanks for asking, how can I assist you today?"]
    ],
    [
        r"what can you do?",
        ["I can chat with you, help you find information, or just keep you company!", "I'm here to answer your questions or just talk!"]
    ],
    [
        r"tell me a joke",
        ["Why don’t scientists trust atoms? Because they make up everything!", "What did the ocean say to the shore? Nothing, it just waved!"]
    ],
    [
        r"i feel (.*)",
        ["I'm sorry to hear that you're feeling %1. Do you want to talk about it?", "It's okay to feel %1 sometimes. How can I help?"]
    ],
    [
        r"sorry (.*)",
        ["No problem at all. What can I help with?", "It's okay! We all make mistakes."]
    ],
    [
        r"(.*)weather(.*)",
        ["I'm not sure about the weather, but you can check on your phone!", "You might want to look it up on a weather app."]
    ],
    [
        r"quit",
        ["Goodbye! It was nice chatting with you. Have a great day!", "Take care! Feel free to chat with me anytime."]
    ],
    [
        r"(.*)",
        ["That sounds interesting. Tell me more!", "Could you elaborate?", "I'm curious to hear more about that."]
    ]
]

# Chatbot gui code 
class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Chatbot")

        # Set up the chat window
        self.chat_window = tk.Text(self.root, bd=1, bg="lightgray", width=50, height=8)
        self.chat_window.grid(row=0, column=0, columnspan=2)
        
        # Add a scroll bar for the chat window
        self.scrollbar = tk.Scrollbar(self.root, command=self.chat_window.yview)
        self.scrollbar.grid(row=0, column=2, sticky='ns')

        # Entry box for the user to type their messages
        self.message_entry = tk.Entry(self.root, bd=1, bg="white", width=40)
        self.message_entry.grid(row=1, column=0)

        # Send button
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1)

        # Initialize chatbot logic
        self.chat = Chat(pairs, reflections)
    
    # Function to handle sending messages
    def send_message(self):
        user_message = self.message_entry.get().strip()
        
        if user_message:
            # Display user message in the chat window
            self.chat_window.insert(tk.END, f"You: {user_message}\n")
            self.message_entry.delete(0, tk.END)
            
            # Get chatbot response
            bot_response = self.chat.respond(user_message)
            
            # Display bot response in the chat window
            self.chat_window.insert(tk.END, f"Bot: {bot_response}\n")
            
            # Scroll to the latest messages
            self.chat_window.yview(tk.END)

# Main function to run the chatbot GUI
if __name__ == "__main__":
    root = tk.Tk()
    gui = ChatbotGUI(root)
    root.mainloop()
