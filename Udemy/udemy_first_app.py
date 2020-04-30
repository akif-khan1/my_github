import json
from difflib import get_close_matches
                                                                            # >>> SequenceMatcher(None, "rain", "rainn").ratio()
data = json.load(open('D:/Python/Udemy/data.json'))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0 :
        yn = input("Did you mean %s instead? Enter Y if yes or N if No: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "Word doesn't exist, please double check it!"
        else:
            return "Sorry! Unable to process the text."
    else:
        return "Word doesn't exist, please double check it!"


# word = input('enter a word to translate!\n     ""')

# output = (translate(word))

# if type(output) == list:
#     print ("\n".join(output))
#     # for item in output:       # I used join method instead of iterate with for loop #
#     #     print(item)
# else:
#     print (output)


while True:
    word = input('enter a word to translate!\n')
    output = (translate(word))
    if word == '\end':
        break
    elif type(output) == list:
        print ("\n".join(output))
    else:
        print(output)