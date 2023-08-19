import os
import openai
import requests
import json

def main():
    modelTarget = "gpt-3.5-turbo"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    print("Python API REPL for " + modelTarget)
    print("Enter 'exit' to quit")
    allMessages = []
    
    while True:
        user_input = input("Enter your input: ")

        if user_input == "exit":
            print("Exiting...")
            break
        
        moderationResults = openai.Moderation.create(user_input)
        
        messageIsFlagged = moderationResults.results[0].flagged

        if messageIsFlagged:
            print(moderationResults)
            print("Message flagged by the moderation endpoint and not sent to api")
            continue
        
        userMessage = {"role" : "user", "content": user_input}
        allMessages.append(userMessage)
        
        chat_completion = openai.ChatCompletion.create(model=modelTarget, messages=allMessages)
        #print("Raw API Response:", chat_completion)
        
        apiMessageResponse = chat_completion.choices[0].message
        
        allMessages.append(apiMessageResponse)
        
        print(apiMessageResponse.content)
        

if __name__ == "__main__":
    main()