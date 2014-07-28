from haystack import indexes

from account.models import Eestecer


class EestecerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Eestecer