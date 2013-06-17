from haystack import indexes
from darkoob.social.models import UserProfile, School

class UserProfileIndexes(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    userprofile_user_auto = indexes.NgramField(model_attr='user')
    rendered = indexes.CharField(use_template=True, indexed=False)

    def get_model(self):
        return UserProfile


class SchoolIndexes(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    school_name_auto = indexes.NgramField(model_attr='name')
    rendered = indexes.CharField(use_template=True, indexed=False)
    
    def get_model(self):
        return School
