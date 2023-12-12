import wikipedia
import dater as d
import corpus_assembler as ca
import grapher as g
import output_generator as o
import json


corpus_assembler = ca.CorpusAssembler()
dater = d.Dater()
grapher = g.Grapher()
out = o.OutputGenerator()

file1 = open('evaluation-graph-entries-topology.txt', 'r')
lines = file1.readlines()
corpus = []
for line in lines:
    term = line.split("\n")[0]
    corpus.append(term)

graphs = grapher.connectCorpus(corpus, "Topology")
out.runRelevanceMode(graphs, "Topology")