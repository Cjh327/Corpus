# -*- coding: utf-8 -*-

import os

class CorpusObject(list):

    def __init__(self):
        self.categories = []

class Corpus(object):
    
    def __init__(self):
        pass
    
    def read_corpus(self, file_name):
        """
        Read and return the data from a corpus json file.
        """
        import io
        import yaml
    
        with io.open(file_name, encoding='utf-8') as data_file:
            data = yaml.load(data_file)
        return data
    
    #读取指定文件
    def load_corpus(self, file_path):
        corpus = CorpusObject()
        corpus_data = self.read_corpus(file_path)
        
        conversations = corpus_data.get('conversations', [])
        corpus.categories = corpus_data.get('categories', [])
        corpus.extend(conversations)
        
        return corpus
    
    #读取指定文件夹中的所有文件
    def load_corpora(self, file_dir):
        """
        Return the data contained within a specified corpus.
        """
        corpora = []
        file_paths = os.listdir(file_dir)
        os.chdir(file_dir)
        
        for file_path in file_paths:
            corpus = self.load_corpus(file_path)            
            corpora.append(corpus)
        
        return corpora

if __name__ == '__main__':
    corpus = Corpus()
    corpus_data = corpus.load_corpus("data\\faq.yml")
    print(corpus_data)
    print(len(corpus_data))
#    corpora = corpus.load_corpora("data")
#    print(corpora)
#    print(len(corpora))