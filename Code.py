from PIL import Image

BG = Image.open("bg.jpg") #opening an empty white sheet
sizeOfSheet = BG.width
gap, _ = 50, 20
allowedChars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.-?() 1234567890'


def writee(char):
    global gap, _
    if char == '\n':
        pass
    else:
        char.lower()
        cases = Image.open("%s.jpg" % char)
        BG.paste(cases, (gap, _))
        size = cases.width
        gap += size
        del cases


def letterwrite(word):
    global gap, _
    if gap > sizeOfSheet - 95 * (len(word)):
        gap = 0
        _ += 200
    for letter in word:
        if letter in allowedChars:
            if letter.islower():
                pass
            elif letter.isupper():
                letter = letter.lower()
                letter += 'upper'
            elif letter == '.':
                letter = 'fullstop'
            elif letter == '!':
                letter = 'exclamation'
            elif letter == '?':
                letter = 'question'
            elif letter == ',':
                letter = 'comma'
            elif letter == '(':
                letter = 'braketopen'
            elif letter == ')':
                letter = 'braketclose'
            elif letter == '-':
                letter = 'hiphen'
            writee(letter)
"""            elif letter == '<':
                letter = 'lessthan'
            elif letter == '>':
                letter = 'greaterthan'
            elif letter == '/':
                letter = 'slash'
            elif letter == '*':
                letter = 'asterisk'
            elif letter == '%':
                letter = 'percentile'
            elif letter == '_':
                letter == 'underscore'
            elif letter == '=':
                letter = 'equalto'
            elif letter == '#':
                letter = 'hastag'
            elif letter == '@':
                letter = 'atsign'
"""
            

def worddd(Input):
    wordlist = Input.split(' ')
    for i in wordlist:
        letterwrite(i)
        writee('space')


if __name__ == '__main__':
    try:
        with open('new.txt', 'r') as file: #input file
            data = file.read().replace('\n', '')
        l = len(data)
        nn = len(data) // 600
        chunks, chunk_size = len(data), len(data) // (nn + 1)
        p = [data[i:i + chunk_size] for i in range(0, chunks, chunk_size)]

        for i in range(0, len(p)):
            worddd(p[i])
            writee('\n')
            BG.save('%doutt.jpg' % i)
            BG1 = Image.open("bg.jpg")
            BG = BG1
            gap = 0
            _ = 0
    except ValueError as E:
        print("{}\nTry again".format(E))

from fpdf import FPDF
from PIL import Image

imagelist = []
for i in range(0, len(p)):
    imagelist.append('%doutt.jpg' % i)
cover = Image.open(imagelist[0])
width, height = cover.size
pdf = FPDF(unit="pt", format=[width, height])
for i in range(0, len(imagelist)):
    pdf.add_page()
    pdf.image(imagelist[i], 0, 0)
pdf.output("newww.pdf", "F")
