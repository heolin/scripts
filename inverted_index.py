#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import re
import math

SEPARATORS = " ,.!?\'\"\(\)\[\]\}\{"

def tokenize(line):
    return re.findall("[^"+SEPARATORS+"]+", line)[:-1]

class InvertedIndex(object):

    documents = {}
    terms = {}
    terms_index = {}
    terms_ids = {}
    documents_terms = {}


    def __init__(self):
        pass


    def append_document(self, document):
        self.documents[document] = doc_id = len(self.documents)
        self.documents_terms[doc_id] = {}

        tokens = tokenize(document)
        for tok_id in xrange(len(tokens)):
            token = tokens[tok_id]
            if token not in self.terms:
                self.terms[token] = len(self.terms)
                self.terms_ids[self.terms[token]] = token
            term = self.terms[token]

            if term not in self.terms_index:
                self.terms_index[term] = []
            self.terms_index[term].append((doc_id, tok_id))

            if term not in self.documents_terms[doc_id]:
                self.documents_terms[doc_id][term] = 0
            self.documents_terms[doc_id][term] += 1
        return doc_id


    def term_frequency(self, doc_id, term):
        nij = self.documents_terms[doc_id][term]
        sum_nkj = 0
        for doc in self.documents.values():
            if term in self.documents_terms[doc]:
                print doc
                self.documents_terms[doc][term]
                sum_nkj += self.documents_terms[doc][term]
        print sum_nkj
        return float(nij)/float(sum_nkj)


    def inverse_document_frequency(self, term):
        doc_count = len(self.documents)
        term_docs = len(self.terms_index[term])
        return math.log(float(doc_count)/float(term_docs))


def main():
    index = InvertedIndex()
    for line in sys.stdin:
        index.append_document(line[:-1])
    for x in xrange(500):
        for y in index.documents_terms[x]:
            print index.term_frequency(x, index.documents_terms[x][y])
        print "-----------------------------------"
if __name__ == "__main__":
    main()
