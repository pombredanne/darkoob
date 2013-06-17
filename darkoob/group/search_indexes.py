from haystack import indexes
from darkoob.group.models import Group

class GroupIndexes(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    group_name_auto = indexes.NgramField(model_attr='name')
    rendered = indexes.CharField(use_template=True, indexed=False)

    def get_model(self):
        return Group

