# TFIDF
A simple TFIDF (Term Frequency - Inverse Document Index) calculator in python
You can view test folder to see examples. It is simple. You can put a simple list of terms (a document)

```python
self.doc1 = ['Harry', 'Potter', 'series', 'was', 'written', 'by', 'famous', 'author', 'JKRowling']
self.doc2 = ['JRRTalkin', 'wrote', 'famous', 'The', 'Lord', 'Of', 'The', 'Rings', 'series', 'with', 'extra', 'of']
self.doc3 = ['I', 'love', 'Harry', 'and', 'Ron', 'and', 'Hermione']
self.doc4 = ['wizards', 'Hobbits', 'are', 'not', 'wizards', 'but', 'are', 'stranger', 'than', 'wizards']
        
resDoc1 = DocumentClass(self.doc1)
resDoc2 = DocumentClass(self.doc2)
resDoc3 = DocumentClass(self.doc3)
resDoc4 = DocumentClass(self.doc4)
        
print resDoc2.getTTIDF('of')
```

will print 2.77
