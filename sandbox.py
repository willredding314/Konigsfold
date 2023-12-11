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

file1 = open('evaluation-dates-topology.txt', 'r')
lines = file1.readlines()

for line in lines:
    terms = line.split(":")
    term = terms[0]
    date = dater.dateDocument(term)
    print(term + " " + str(date))