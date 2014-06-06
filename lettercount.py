from sys import argv

script, filename = argv

my_file = open(filename)

text = my_file.read()

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letter_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for char in text:
    if char.lower() in letters:
        index = letters.index(char.lower())
        letter_count[index] += 1

for l in letter_count:        
    print l