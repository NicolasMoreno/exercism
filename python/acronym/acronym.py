def abbreviate(words):
    splittedWord = words.replace('-', ' ').replace('_', ' ').split(' ')
    acronym = ''
    for word in splittedWord:
        if (len(word) > 0):
            acronym += word[0].upper()
    return acronym
