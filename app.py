import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def FindDef(word):

        if word.lower() in data:
            content=data[word.lower()]
            for i in content:
                print(i)
        elif word.title() in data:
            content=data[word.title()]
            for i in content:
                print(i)
        elif word.upper() in data:
            content=data[word.upper()]
            for i in content:
                print(i)
        elif len(get_close_matches(word, data.keys())) > 0:
            yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
            if yn == "Y":
                for i in data[get_close_matches(word, data.keys())[0]]:
                    print(i)
            elif yn == "N":
                print("The word doesn't exist. Please double check it.")
            else:
                print("We didn't understand your entry.")
        else:
            print("No results found. Please Check the Entered Word Again.!")

word=input("\nEnter A Word :-")
FindDef(word)
