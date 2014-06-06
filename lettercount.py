from sys import argv

script, filename = argv

my_file = open(filename)

text = my_file.read()

letter_count = [0] * 26

for char in text:
    if (ord(char)> 64 and ord(char)<91) or (ord(char) > 96 and ord(char) < 123):
        letter_count[ord(char.lower())-97] += 1

for l in letter_count:
    print l