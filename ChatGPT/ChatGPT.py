import os
import openai
import requests
import json
import time
import secrets



def main():
    modelTarget = "gpt-4"
    #modelTarget = "gpt-3.5-turbo"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    print("Python API REPL for " + modelTarget)
    print("Enter 'exit' to quit")
    allMessages = []
    
    filename = secrets.token_hex(6)
    filename = 'chatLogs\\' + filename + '.txt'   

    try:
        os.makedirs('chatLogs')
    except OSError:
        print ("Creation of the chatLogs directory failed")
    else:
        print ("Successfully created the chaLogs directory")    


    while True:
        user_input = input("Enter your input: ")

        if user_input == "exit":
            print("Exiting...")
            break
        
        start_time = time.time()
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
        
        end_time = time.time()
        print("\nTime taken: ", end_time - start_time, " seconds.\n\n")
        print(apiMessageResponse.content)
        
        with open(filename, 'w') as f:
            for item in allMessages:
                f.write("%s\n" % item)
        

if __name__ == "__main__":
    main()