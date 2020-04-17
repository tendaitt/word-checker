import csv

common_words = set()

with open('common_words.csv', 'r') as common_words_file:

    reader = csv.reader(common_words_file)

    for row in reader:
        common_words.update(row)

for word in common_words:
    print(word)
