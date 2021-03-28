import datetime
from elasticsearch_dsl import Document, Text, Float, Date

class Vocabulary(Document):
    name = Text()
    score: Float()
    created_at: Date() = datetime.now()
    updated_at: Date() = datetime.now()

    class Index:
        name = "vocabularies"
    
    def save(self, **kwargs):
        # TODO: check vocab existence
        return super().save(**kwargs)

