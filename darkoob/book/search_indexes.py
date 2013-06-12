from haystack import indexes
#from queued_search.indexes import QueuedSearchIndex
from darkoob.book.models import Book, Author, Publisher


class BookIndexes(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='authors', faceted=True)
    rendered = indexes.CharField(use_template=True, indexed=False)

    def get_model(self):
        return Book

class AuthorIndexes(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    rendered = indexes.CharField(use_template=True, indexed=False)

    def get_model(self):
        return Author

class PublisherIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    rendered = indexes.CharField(use_template=True, indexed=False)

    def get_model(self):
        return Publisher
