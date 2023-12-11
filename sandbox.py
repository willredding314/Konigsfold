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

corpus = corpus_assembler.assemble("Topology")
file1 = open('corpus-topology.txt', 'r')
lines = file1.readlines()

rel = 0
count = 0

for line in lines:
    count += 1
    if "- REL" in line:
        rel += 1

print(rel)
print(count)
print(rel/count)