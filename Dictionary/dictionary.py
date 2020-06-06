# This code is written by Utkarsh Yadav. 

import json
from difflib import get_close_matches

data = json.load(open("raw_data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print(" Hey User !! Did you mean %s instead \n" %get_close_matches(word, data.keys())[0])
        decide = input("\n Press 'y' for Yes or 'n' for No : ")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return("\n Hey User !! You can try again with different word.\n")
        else:
            return("\n Hey User !! You have entered wrong input please input just 'y' or 'n'\n")
    else:
        print("\n Sorry !! We could not find this word in our dictionary.")



word = input("\n\n\n Hey User !! Enter the word you want to search :")
print("\n Your Search results are shown below :\n")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

print("\n\n\n\n")
