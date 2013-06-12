from haystack import indexes
from darkoob.social.models import UserProfile, School

class UserProfileIndexes(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    rendered = indexes.CharField(use_template=True, indexed=False)

    def get_model(self):
        return UserProfile


class SchoolIndexes(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    rendered = indexes.CharField(use_template=True, indexed=False)
    
    def get_model(self):
        return School
