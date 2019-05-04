def is_pangram(sentence):
    frequency = [0] * 26
    for sentenceChar in sentence.lower():
        asciiValue = ord(sentenceChar)
        if (asciiValue >= 97 and asciiValue <= 122):
            frequency[ asciiValue - 97] += 1
    checkingPangram = list(filter( lambda x: x == 0, frequency))
    return len(checkingPangram) == 0