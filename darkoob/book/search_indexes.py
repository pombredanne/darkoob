from haystack import indexes
#from queued_search.indexes import QueuedSearchIndex
from darkoob.book.models import Book, Author


class BookIndexes(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    #publisher = indexes.CharField(model_attr='publisher')
    #language = indexes.CharField(model_attr='language')

    def get_model(self):
        return Book

class AuthorIndexes(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Author
