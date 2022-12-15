#https://www.codewars.com/kata/56fa9cd6da8ca623f9001233

def elemental_forms(word):
    def rec(word):
        if not word: yield []; return
        for i in range(1, min(3, len(word)) + 1):
            key = word[:i].title()
            if key in ELEMENTS:
                for sub in rec(word[i:]):
                    yield [f'{ELEMENTS[key]} ({key})'] + sub
    return list(rec(word))