import math
from collections import defaultdict


class SparseIndex:
    def __init__(self):
        self.docs = []
        self.term_freq = []
        self.doc_freq = defaultdict(int)

    def add(self, documents: list[str]):
        for doc in documents:
            tf = defaultdict(int)
            for word in doc.lower().split():
                tf[word] += 1
            self.term_freq.append(tf)
            self.docs.append(doc)

            for word in tf.keys():
                self.doc_freq[word] += 1

    def search(self, query: str, k=5):
        scores = []
        query_terms = query.lower().split()
        N = len(self.docs)

        for idx, tf in enumerate(self.term_freq):
            score = 0
            for term in query_terms:
                if term in tf:
                    idf = math.log((N + 1) / (self.doc_freq[term] + 1))
                    score += tf[term] * idf
            scores.append((score, idx))

        scores.sort(reverse=True)
        return [self.docs[i] for _, i in scores[:k]]
