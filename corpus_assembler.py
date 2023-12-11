import wikipedia

class CorpusAssembler():

    def assemble(self, topic_name):
        coreTopicPage = wikipedia.page(topic_name)
        outlinks = coreTopicPage.links
        return self.gather_from_topic_lists(outlinks)

    def gather_from_topic_lists(self, links):
        subtopic_links = set()
        for link in links:
            if "List of" in link and "topic" in link:
                outlinks = wikipedia.page(link).links
                outlinks = list(filter(lambda x: self.suitableCorpusValue(x), outlinks))
                subtopic_links.update(outlinks)
            else:
                if self.suitableCorpusValue(link):
                    subtopic_links.add(link)
        return subtopic_links

    def suitableCorpusValue(self, doc_title):
        return len(doc_title) > 2 and "List of " not in doc_title
