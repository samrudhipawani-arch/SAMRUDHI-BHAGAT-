def chatbot():
    print("Chatbot: Hi! Type 'bye' to exit.")
    
    while True:
        user = input("You: ").lower()

        if "hello" in user:
            print("Chatbot: Hello! How are you?")
        elif "time" in user:
            from datetime import datetime
            print("Chatbot: Current time is:", datetime.now().strftime("%H:%M:%S"))
        elif "name" in user:
            print("Chatbot: I'm MiniBot!")
        elif "bye" in user:
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: I don't understand that yet.")

chatbot()
