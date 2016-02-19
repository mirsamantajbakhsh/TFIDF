'''
Created on Feb 17, 2016

@author: Mir Saman Tajbakhsh
'''
import unittest
from DocumentPackage.DocumentClass import DocumentClass

class TestDocument(unittest.TestCase):

    def testDocument(self):
        self.doc1 = ['Harry', 'Potter', 'series', 'was', 'written', 'by', 'famous', 'writer', 'JKRowling']
        self.doc2 = ['JRRTalkin', 'wrote', 'famous', 'The', 'Lord', 'Of', 'The', 'Rings', 'series', 'with', 'extra', 'of']
        self.doc3 = ['I', 'love', 'Harry', 'and', 'Ron', 'and', 'Hermione']
        self.doc4 = ['wizards', 'Hobbits', 'are', 'not', 'wizards', 'but', 'are', 'stranger', 'than', 'wizards']
        
        resDoc1 = DocumentClass(self.doc1)
        resDoc2 = DocumentClass(self.doc2)
        resDoc3 = DocumentClass(self.doc3)
        resDoc4 = DocumentClass(self.doc4)
        
        #Check TF
        self.assertEqual(resDoc2.getTF('of'), 2, "Error in case sensitive")
        self.assertEqual(resDoc4.getTF('wizards'), 3, "Error in Wizards")
        
        #Check IDF
        self.assertEqual(DocumentClass.IDF['harry'], 2, "Error in IDF of harry")
        self.assertEqual(DocumentClass.IDF['wizards'], 1, "Error in IDF of wizards")
        
        #Check TF-IDF
        self.assertEqual(resDoc2.getTTIDF('of'), 2.77, "Error in TT-IDF")
        self.assertEqual(resDoc2.getTTIDF('Of'), 0, "Error in TT-IDF of term with upper case")
        self.assertEqual(resDoc2.getTTIDF('test'), 0, "Error in TT-IDF that does not exists in corpus")
        self.assertEqual(resDoc1.getTTIDF('harry'), resDoc1.getTTIDF('harry'), "Error in TT-IDF computation of two equal terms")