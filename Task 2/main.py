# Rule based chatbot

responses:dict = {
    "hello":"Hi!",
    "how are you":"I'm fine, thanks!",
    "bye":"Goodbye!",
}

def chat():
    chat_log = ""
    while True:
        msg = input("User: ")
        chat_log += f"User: {msg}\n"
        if msg_clean(msg) in list(responses.keys()):
            response = f"Bot: {responses.get(msg)}\n"
            print(response)
            chat_log += response
        elif msg_clean(msg) == "/print-chat":
            print(chat_log)


        if msg == "end": break

def msg_clean(msg:str):
    msg = msg.strip()
    return msg

chat()

chat()