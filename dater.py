import re
import corpus_assembler as ca
import wikipedia

class Dater():

    def dateCorpus(self, c):
        topic_dates = []
        for doc_title in c:
            date = self.dateDocument(doc_title)
            if date is not None:
                topic_dates.append((doc_title, date))
        return topic_dates
    
    def dateDocument(self, doc_title):
        try:
            document = wikipedia.wikipedia.page(doc_title, auto_suggest=False)
            priority_date_sources = self.priorityDateSources(document)
            return self.optimalDate(priority_date_sources)
        except:
            return None

    def priorityDateSources(self, document):
        # Priority sources for dates are:
        #   1. History section
        #   2. Document summary
        #   3. Complete text
        priority_date_sources = []
        if "History" in document.sections:
            priority_date_sources.append(document.section("History"))
        priority_date_sources.append(document.summary)
        priority_date_sources.append(document.content)    
        return priority_date_sources
    
    def optimalDate(self, source_texts):
        for text in source_texts:
            optimal_date = self.findEarliestDate(text)
            if optimal_date is not None:
                return optimal_date
        return None
    
    def findEarliestDate(self, document_text):
        terms = document_text.split()
        yearTerms = []
        for term in terms:
            matches = re.findall(r'^[12][0-9]{3}$', term)
            matches = list(filter(lambda x: len(x) == 4, matches))
            yearTerms = yearTerms + matches
        if len(yearTerms) > 0:
            years = map(lambda x: int(x), yearTerms)
            years = sorted(years)
            return years[0]
        else:
            return None
