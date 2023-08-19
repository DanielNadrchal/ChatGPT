
#https://platform.openai.com/docs/libraries

import os
import openai
import requests
import json


#chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
#print(chat_completion)




#def send_request(input_data):
#    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": input_data}])
#  
#    return chat_completion

def main():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    print("Python API REPL")
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
            print("Message flagged and not sent to api")
            continue
        
        #print(moderationResults)
        userMessage = {"role" : "user", "content": user_input}
        allMessages.append(userMessage)
        
        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=allMessages)
        print("Raw API Response:", chat_completion)
        
        apiMessageResponse = chat_completion.choices[0].message
        
        allMessages.append(apiMessageResponse)
        
        print(apiMessageResponse.content)
        

if __name__ == "__main__":
    main()