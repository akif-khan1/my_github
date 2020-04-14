import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    return data[w]

word = input('enter a word to translate!\n     ""')

print (translate(word))