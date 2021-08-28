import json
import difflib
data = json.load(open("data.json"))
def fetch(word):
    if word in data:
        return data[word]
    elif len(difflib.get_close_matches(word,data.keys()))>0:
        response= input(f"Did you mean {difflib.get_close_matches(word,data.keys())[0]} instead? Enter Y is YES and N if NO\n")
        if response== 'y' or 'Y':
            return data[difflib.get_close_matches(word,data.keys())[0]]
        elif response == 'n' or 'N':
            return "Word does not Exist..RECHECK "
        else:
            return "We didn't understand. Please recheck Response\n"
    elif len(difflib.get_close_matches(word,data.keys()))==0:
        return "Word does not Exist..RECHECK "
word=input("Enter word\n")
word=word.lower()
fetched=fetch(word)
if(type(fetched)==list):
    for item in fetched:
        print(item)
else:
    print(fetched)
