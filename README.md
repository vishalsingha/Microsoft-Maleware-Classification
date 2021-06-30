## Microsoft-Maleware-Classification

### Dataset : 
   **Source** : [Dataset](https://www.kaggle.com/c/malware-classification/data) 
   
   
   **Discription** : Dataset consist of .asm and .bytes files which are generated by PC on installing any software. Corresponding to each .asm and .bytes files (i.e for each software) there are labels. So we have to classify the every given set of .asm and .bytes files into one of the 9 Classes.
   
   
## Approch used : 

* Feature extraction for Bytes files : 
        Since the  bytes files contains only hexadecimal number system values. So I used bag of words for Bag of words for feature extraction.
* Feature extraction for .asm files : 
        I again used custom Bag of word fo feature extaction. First I cleaned the content of .asm files on the basis of literature than implemented feature extraction over it. 
        
Model : 
  All the machine learning models were trid for the classification task on .bytes and .asm files seperatly and later combining them to see the results.
  
## What I learnt from this task?

* Handiling such a large amount of compressed data (500 GB nearly) with the limited resources for processing.
* Using custom implementation when the data don't fit into ram.
* Using parallel programming to inhance the speed for feature extraction.

## What's more to do??
* Using bigram feature extractor for .bytes files.
* Improving feature extraction for .asm files by using domain knowledge.
   
   
   
   
