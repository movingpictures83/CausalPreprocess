import pandas as pd
import os

import PyIO
import PyPluMA
class CausalPreprocessPlugin:
    def input(self, inputfile):
        self.parameters = PyIO.readParameters(inputfile)

    def run(self):
        pass

    def output(self, outputfile):
       mimosafile = open(PyPluMA.prefix()+"/"+self.parameters["mimosafile"], 'r')
       taxaToKeepBasedOnMIMOSA = mimosafile.readline().strip().split(',')
       top50file = open(PyPluMA.prefix()+"/"+self.parameters["top50file"], 'r')
       top50AbundanceTaxa = top50file.readline().strip().split(',')
       taxaToKeepBasedOnMIMOSA = [x.lower() for x in taxaToKeepBasedOnMIMOSA]
       top50AbundanceTaxa = [x.lower() for x in top50AbundanceTaxa]
       unionTaxa = set(taxaToKeepBasedOnMIMOSA).union(top50AbundanceTaxa)
       #taxaToKeepBasedOnMIMOSA = PyIO.readSequential(PyPluMA.prefix()+"/"+parameters["mimosa.txt"])
       #top50AbundanceTaxa = PyIO.readSequential(PyPluMA.prefix()+"/"+parameters["top50.txt"])

       for file in os.listdir(PyPluMA.prefix()+"/"+self.parameters["inputdir"]):
        if file.endswith(".tsv") and not file.startswith("filtered"):
            d = pd.read_csv(PyPluMA.prefix()+"/"+self.parameters["inputdir"]+"/"+file,sep="\t")
            d.columns = map(str.lower, d.columns)

            colsToKeep =  ["subjectid$id", "week sample obtained$clinical"] +  list(unionTaxa.intersection(d.columns))

            df = d[colsToKeep]
            print(df)

            df.to_csv((outputfile+"/filtered_"+file), encoding='utf-8',sep="\t",index=False)



