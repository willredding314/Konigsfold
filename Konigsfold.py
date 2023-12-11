import corpus_assembler as ca
import dater as d
import grapher as g
import output_generator as o

instructions = """
Welcome to Konigsfold, where you can find learning paths on any academic topic. 

Usages:

TIMEMODE [Topic] [yearStart-yearEnd]/[before/after-[year]]
    - get Wikipedia titles for subtopics in the field, based on year of discovery

RELEVANCEMODE [Topic] 
    - get Wikipedia titles for topics in the field, in time order but grouped based on relevant subtopics

"""

def run():
    query = input(instructions).split()
    mode = query[0]
    topic = query[1]
    args = query[2:]

    corpus_assembler = ca.CorpusAssembler()
    dater = d.Dater()
    grapher = g.Grapher()
    out = o.OutputGenerator()

    corpus = corpus_assembler.assemble(topic)
    print(" -- Assembled Corpus")
    dates = dater.dateCorpus(corpus)
    print(" -- Dated Corpus")
    connections = grapher.connectCorpus(corpus, topic)
    print(" -- Connected Corpus")

    if mode == "TIMEMODE":
        out.runTimeMode(dates, args[0])  
    if mode == "RELEVANCEMODE":
        out.runRelevanceMode(dates, connections)

run()        