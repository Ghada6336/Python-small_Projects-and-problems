from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')


def get_meanings(word):
    synsets = wordnet.synsets(word)
    if not synsets:
        return None
    meanings = {}
    for synset in synsets:
        pos = synset.pos()
        definition = synset.definition()
        if pos in meanings:
            meanings[pos].append(definition)
        else:
            meanings[pos] = [definition]
    return meanings


while True:
    word = input("Enter your word: ")
    if word == "":
        break

    meanings = get_meanings(word)
    if meanings:
        print(meanings)
    else:
        print("No meaning found for the word:", word)
