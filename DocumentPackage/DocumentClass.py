'''
Created on Feb 16, 2016

@author: Mir Saman Tajbakhsh
'''
import itertools
from collections import defaultdict
import numpy

class DocumentClass:
    'A document without purification'
    #TODO: Add purification
    
    #IDF
    NumberOfDocuments = 0
    IDF = defaultdict(int)

    def __init__(self, document):
        #Add a document to corpus
        
        #Increment document numbers as new one added
        DocumentClass.NumberOfDocuments += 1
        
        #DocumentPackage is a list
        self.doc = document
        self.analyzedoc()
        
    def analyzedoc(self):
        #self.tf = {g[0]: len(list(g[1])) for g in itertools.groupby(self.doc)}
        self.tf = {}
        tempDoc = [x.lower() for x in self.doc]
        for k,g in itertools.groupby(sorted(tempDoc)):
            self.tf[k] = len(list(g))
            self.IDF[k] += 1
    
    def printdoc(self):
        print self.doc;
    
    def getTF(self, word):
        try:
            return self.tf.get(word)
        except Exception:
            return 0
    
    def getIDF(self, word):
        try:
            return numpy.log(DocumentClass.NumberOfDocuments / DocumentClass.IDF[word]);
        except Exception:
            return 0;
    
    def getTTIDF(self, word):
        try:
            return self.getTF(word) * self.getIDF(word)
        except Exception:
            return 0