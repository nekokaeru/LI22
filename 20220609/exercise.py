first = []
second = []
with open('word_sample.txt') as f:
    for l in f:
        splitted = l.split()
        first.append(splitted[0])
        second.append(splitted[1].split(','))