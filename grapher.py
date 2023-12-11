import wikipedia

class Grapher():

    MAX_SEARCH_LEVEL = 3

    def connectCorpus(self, corpus, topic):
        outlinks = {}
        for idx, doc in enumerate(corpus):
            try:
                page = wikipedia.page(doc, auto_suggest=False)
                outlinks[doc] = list(filter(lambda x: x in corpus, page.links))
            except:
                pass
        return outlinks