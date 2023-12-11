import wikipedia
import dater as d
import corpus_assembler as ca
import grapher as g
import output_generator as o


corpus_assembler = ca.CorpusAssembler()
dater = d.Dater()
grapher = g.Grapher()
out = o.OutputGenerator()

corpus = corpus_assembler.assemble("Information Theory")
print(" -- Assembled Corpus")
print(len(corpus))

#dates = dater.dateCorpus(corpus)
#print(" -- Dated Corpus")
#connections = grapher.connectCorpus(corpus, "Graph Theory")
#print(" -- Connected Corpus")
#print(connections)
