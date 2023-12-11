import wikipedia

class OutputGenerator():

    def runRelevanceMode(self, connections, topic):
        topicLinks = wikipedia.page(topic).links
        


    def runLPMode(self, dates, connections):
        results = []
        sortedDates = sorted(dates, key=lambda x: x[1])
        for link in [x[0] for x in sortedDates]:
            if link not in results and len(connections[link]) != 0:
                results.append(link)
                self.addPathways(link, connections, results)
        self.display(results)

    def addPathways(self, topic, connections, results):
        print("Results are of size: " + str(len(results)))
        outLinks = connections.get(topic)
        if outLinks is not None:
            for outLink in outLinks:
                if outLink not in results:
                    results.append(outLink)
                    self.addPathways(outLink, connections, results)

    def runTimeMode(self, dates, timeArg):
        timeArg1 = timeArg.split("-")[0]
        timeArg2 = timeArg.split("-")[1]
        results = []
        if timeArg1 == "before":
            results = list(filter(lambda x: x[1] < int(timeArg2), dates))
        elif timeArg1 == "before":
            results = list(filter(lambda x: x[1] > int(timeArg2), dates))
        else:
            filteredBefore = list(filter(lambda x: x[1] < int(timeArg2), dates))
            results = list(filter(lambda x: x[1] > int(timeArg1), filteredBefore))
        results = sorted(results, key=lambda x: x[1])
        results = [x[0] for x in dates]    
        self.display(results)

    def display(self, results):
        print("Here's your learning path: \n")
        for idx, result in enumerate(results):
            print(str(idx) + ". " + result)