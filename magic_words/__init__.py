import itertools
from string import ascii_lowercase
from simplecrypt import decrypt


N = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
SPECIAL = 18
MEANINGFUL = 75
SCORES = dict(zip(ascii_lowercase, N))
VOWELS = ('a', 'e', 'i', 'o', 'u')
KEY = input('What\'s the key? ')
MAGIC_WORDS = decrypt(
    KEY,
    (b'sc\x00\x02@\xab\x0f\xcf\xa4\x87\xada{\xf9\xa3\xce\xdbQ\xca\xaa\x12H\x11\x9cy\xbc\xa2\xc7'
     b'\x0b\x03\x08\x97\x03\xdev.\xa0\xbcYuh\x89Y\x918\x10\xa3\xad\x15d)\x97qIoVj\xed\xd5\xa9'
     b'\xf9t!jAB\xed\x1bI\xc5\xbe-p*e')
).decode()


def words_in_dictionary():
    with open('/usr/share/dict/words', 'r') as f:
        dictionary = f.readlines()
    return set(w.rstrip() for w in dictionary)


def substrings(s):
    for i in range(2, len(s) + 1):
        for p in itertools.permutations(s, i):
            yield ''.join(p)


def all_possible_words():
    all_words = set(substrings(MAGIC_WORDS)) & words_in_dictionary()
    return sorted(all_words, key=lambda w: (len(w), w))


def value_of(w):
    score = 0
    for c in w:
        score += SCORES[c]
    return score


def you_do_not_yammer_over_the(question):
    if (not question.startswith(VOWELS)
            and (value_of(question) == SPECIAL or value_of(question) == MEANINGFUL)
            and not question == 'yammer'):
        return question


def ask(words):
    question = ' '.join(sorted(words))
    print(question + '?')


def main():
    question = set()
    for magical_word in all_possible_words():
        if you_do_not_yammer_over_the(magical_word):
            question.add(magical_word)
    ask(question)


if __name__ == '__main__':
    main()
