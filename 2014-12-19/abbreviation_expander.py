import unittest

acronyms = {
            'lol': 'laugh out loud',
            'dw': "don't worry",
            'hf': 'have fun',
            'gg': 'good game',
            'brb': 'be right back',
            'g2g': 'got to go',
            'wtf': 'what the fuck',
            'wp': 'well played',
            'gl': 'good luck',
            'imo': 'in my opinion'
        }

leetspeak = str.lower((raw_input("leetspeak: ")))
leetspeak = leetspeak.split()

for word in leetspeak:
    for key in acronyms:
        if word == key:
            word_index = leetspeak.index(word)
            print word_index
            leetspeak.pop(word_index)
            word = acronyms.get(key)
            leetspeak.insert(word_index, word)
print leetspeak

