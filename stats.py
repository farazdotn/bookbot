import re

def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    DaDict = {}
    for char in text.lower():
        if char.isalpha():
            if char in DaDict:
                DaDict[char] += 1
            else:
                DaDict[char] = 1
    return DaDict

def sort_order(mah_dict):
    def by_count(dih):
        return dih[1]
    sorted_by_count = sorted(mah_dict.items(), key=by_count, reverse=True)
    return dict(sorted_by_count)

