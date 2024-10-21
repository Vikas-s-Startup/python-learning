from random import randint

def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))

def getRandomLowerCaseLetter():
    return getRandomCharacter('a', 'z')

def getRandomUpperCaseLetter():
    return  getRandomCharacter('A', 'Z')

def getRandomDigitCharacter():
    return getRandomCharacter('0', '9')

def getRandomASCIICharacter():
    return getRandomCharacter(chr(0), chr(127))

NUMBER_OF_CHARS = 175
CHARS_PER_LINE = 25

for i in range(NUMBER_OF_CHARS):
    print(getRandomLowerCaseLetter(), end = "")
    if (i+1) % CHARS_PER_LINE == 0:
        print()