from dataclasses import dataclass
from datetime import datetime
from typing import List
from elasticsearch_dsl import Document, Text, Float, Date, Keyword
from typing import Optional
from collections import Counter


@dataclass
class VocabFeed:
    name: str
    meaning: Optional[str] = None
    frequency: Optional[int] = 0

    @staticmethod
    def from_counter(c: Counter):
        return [VocabFeed(name=voca, frequency=freq) for (voca, freq) in c.items()]

class Vocabulary(Document):
    name = Text()
    meaning = Text()
    tags = Keyword()
    score: Float()
    created_at: Date() = datetime.now()
    updated_at: Date() = datetime.now()

    class Index:
        name = "vocabularies"
    
    def save(self, **kwargs):
        # TODO: check vocab existence
        return super().save(**kwargs)

    @staticmethod
    def from_feed(feed_data: VocabFeed):
        return Vocabulary(
            name=feed_data.name,
            meaning=feed_data.meaning,
            score=feed_data.frequency
        )

class VocabularyRepository:
    def __init__(self):
        pass

    def bulk_load(self, entities: List[Vocabulary]):
        print([w.name for w in entities[:10]])
        for entity in entities:
            entity.save()

class VocabularyFacade:
    def __init__(self) -> None:
        self.voca_repository = VocabularyRepository()

    def feed(self, seed_vocas: List[VocabFeed]) -> None:
        vocas =  [Vocabulary.from_feed(f) for f in seed_vocas]
        self.voca_repository.bulk_load(vocas)
    