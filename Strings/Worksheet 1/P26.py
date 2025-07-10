#Find the Location of a Word in a String

def find_word_position(text, word):
    position = text.find(word)
    if position != -1:
        print("Position:", position)
    else:
        print("Word not found")


sentence = "welcome to python"
search_word = "python"
find_word_position(sentence, search_word)
