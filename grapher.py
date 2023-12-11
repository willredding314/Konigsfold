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
    
    def connectCorpusAtLevel(self, outlinks, connectedCorpus, topic, level):
        if (level == 1):
            print("Running " + topic)
        try:
            for link in outlinks[topic]:
                if outlinks.get(link) is not None:
                    print("HIT")
                    connectedCorpus[topic] = connectedCorpus[topic] + [link]
                    if (level < self.MAX_SEARCH_LEVEL):
                        self.connectCorpusAtLevel(outlinks, connectedCorpus, link, level + 1)
        except:
            pass