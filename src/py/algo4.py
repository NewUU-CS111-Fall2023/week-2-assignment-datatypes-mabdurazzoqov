def checkWord(sentence, word):
    words = sentence.split()
    for i in range(len(words)):
        if words[i] == word:
            return True, i

    return False
