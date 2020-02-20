# Author: Wentao Ma

# TF-IDF Algorithm (Text Analysis/Text Processing)
# TF: Term Frequency
# IDF: Inverse Document Frequency

import math

class TF_IDF:
    def tf_idf(self, word, document1, corpus):
        '''
        :param word: the word that we are analyzing
        :param document1: the string document
        :param corpus: the total number of documents
        :return:
        '''

        total_number_document = len(corpus)
        tf = len(word) / len(document1)
        idf = math.log(total_number_document, len(word))

        result = 0
        self.caculator(tf, idf, result)
        return result

    def caculator(self, a, b, result):
        result = a * b



