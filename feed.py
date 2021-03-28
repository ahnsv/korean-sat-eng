from connection import create_es_connection
import string
import sys
from collections import Counter

from documents.vocab import VocabFeed, VocabularyFacade

IGNORE_TOKENS = ['the', 'of', 'to', 'and', 'a', 'in', 'is', 'that', 'as', 'are', 'was', 'on', 'at', 'not', 'for', 'be', 'it', 'we', 'or', 'his', 'an', 'you', 'this', 'by', 'can', 'our', 'i', 'have', 'their', 'from', 'one', 'they', 'there', 'with', 'but', 'people', 'human', '\\xe2\\x80\\x95', 'had', 'my', 'what', 'do', 'more', 'your', 'many', 'he', 'its', 'all', 'could', 'online', 'use', 'has', '(', ')', 'also', 'who', 'most', 'than', 'if', 'some']


def _cleanse(block: str):
    table = str.maketrans('', '', string.punctuation) 
    words = str(block).lower().translate(table).split(' ')
    return [w for w in words if w not in IGNORE_TOKENS and not w.isdigit()]


def _feed_csv(filename: str) -> None:
    word_counter = Counter()

    with open(file=filename, mode='r') as f:
        for block in f:
            words = _cleanse(block=block)
            for word in words:
                word_counter[word] += 1
    
    feed_data = VocabFeed.from_counter(word_counter)
    voca_facade = VocabularyFacade()
    voca_facade.feed(feed_data)


def main(argv):
    if not argv:
        return 
    create_es_connection()
    for file in argv:
        _feed_csv(file)

if __name__ == '__main__':
    main(sys.argv[1:])
