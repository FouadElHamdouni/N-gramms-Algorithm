from stop_words import get_stop_words

text = open('/Users/jenniferarnold/Corpus/debates1970/1970ALB.txt', 'r')
stop_words = set(get_stop_words('english'))

for line in text:
    for word in line.split():
        if word.lower() not in stop_words:
            print(word)



