import csv

from docx import Document
from string import punctuation


def get_common_words():

    common_words = set()

    with open('common_words.csv', 'r') as common_words_file:

        reader = csv.reader(common_words_file)

        for row in reader:
            common_words.update(row)

        return common_words


def get_test_words():

    test_words = []
    word_doc = Document("test.docx")

    num_paragraphs = len(word_doc.paragraphs)

    for paragraph in range(0, num_paragraphs):
        text = word_doc.paragraphs[paragraph].text

        words = text.translate(str.maketrans('', '', punctuation)).split()
        test_words = test_words + words

    return test_words


def verify():
    pass


print(get_common_words())
print(get_test_words())
