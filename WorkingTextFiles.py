from stop_words import get_stop_words
import string

path = '/Users/jenniferarnold/PycharmProjects/N-gramms-Algorithm/Papers/FederalistNo.84Hamilton.txt'
titleName = path[64:]
print(titleName)
# Make a new file
newFile = open(titleName, "w+")

text = open(path, 'r')
stop_words = set(get_stop_words('english'))

# Open file
file = open(path, 'r', errors='replace')
text = file.read()
text = text.split()



# Loop over text and append to textfile document
for line in text:
    for word in line.split():
        if word.lower() not in stop_words:
            print(word.lower())
            newFile.write(word+" ")