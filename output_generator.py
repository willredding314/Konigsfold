import wikipedia
import json

class OutputGenerator():

    def runRelevanceMode(self, connections, topic):
        topicLinks = wikipedia.page(topic).links
        added_items = []
        outputTrees = {}
        for link in topicLinks:
            if link not in added_items and link in connections.keys():
                added_items.append(link)
                outputTrees[link] = self.produceTree(connections, link, added_items)
        self.writeTrees(outputTrees)
        self.printTrees(outputTrees)

    def produceTree(self, connections, topic, added_items):
        outputTree = {}
        links = connections.get(topic)
        if links is not None:
            for link in connections.get(topic):
                if link not in added_items:
                    added_items.append(link)
                    outputTree[link] = self.produceTree(connections, link, added_items)
        return outputTree        

    def writeTrees(self, outputTrees):
        jsonOut = json.dumps(outputTrees)
        with open("relevance-trees-topology.txt", "w") as file:
            file.write(jsonOut)

    def printTrees(self, outputTrees):
        jsonOut = json.dumps(outputTrees)
        print(jsonOut)

    def runLPMode(self, dates, connections):
        results = []
        sortedDates = sorted(dates, key=lambda x: x[1])
        print(sortedDates)
        for link in [x[0] for x in sortedDates]:
            if link not in results and len(connections[link]) != 0:
                results.append(link)
                self.addPathways(link, connections, results)
        self.display(results)
        self.write(results, "evaluation-learning-path-topology")

    def addPathways(self, topic, connections, results):
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
    
    def write(self, results, file):
        with open(file + ".txt", "w") as f:
            for result in results:
                f.write(result + "\n")