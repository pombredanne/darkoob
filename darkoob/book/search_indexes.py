from haystack import indexes
from darkoob.book.models import Book, Author


class BookIndexes(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    publisher = indexes.CharField(model_attr='publisher')
    language = indexes.CharField(model_attr='language')

    def get_model(self):
        return Book
