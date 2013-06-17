from haystack import indexes
#from queued_search.indexes import QueuedSearchIndex
from darkoob.book.models import Book, Author, Publisher


class BookIndexes(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    book_title_auto = indexes.NgramField(model_attr='title')
    book_tags_auto = indexes.NgramField(model_attr='tags')
    author = indexes.CharField(model_attr='authors', faceted=True)
    rendered = indexes.CharField(use_template=True, indexed=False)

    def get_model(self):
        return Book

class AuthorIndexes(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    autor_name_auto = indexes.NgramField(model_attr='name')
    rendered = indexes.CharField(use_template=True, indexed=False)

    def get_model(self):
        return Author

class PublisherIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    publisher_name_auto = indexes.NgramField(model_attr='name')
    rendered = indexes.CharField(use_template=True, indexed=False)

    def get_model(self):
        return Publisher
