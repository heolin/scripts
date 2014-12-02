#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from scipy.spatial.distance import *

def get_standard_vector(position_vector):
    return set([v[0] for v in position_vector])

def get_standard_vectors_union(vectors):
    if len(vectors) == 1:
        return vectors[0]
    elif len(vectors) == 2:
        return vectors[0] & vectors[1]
    else:
        half = int(len(vectors) / 2)
        return get_standard_vectors_union(vectors[:half]) & get_standard_vectors_union(vectors[half:])

def get_full_vector(input_vector, size):
    result = [0 for _ in xrange(size)]
    for x in input_vector:
        result[x] = 1
    return result

def get_braycurtis_dictance(vector1, vector2):
    return braycurtis(vector1, vector2)

def get_canberra_dictance(vector1, vector2):
    return canberra(vector1, vector2)

def get_cityblock_dictance(vector1, vector2):
    return cityblock(vector1, vector2)

def get_correlation_dictance(vector1, vector2):
    return correlation(vector1, vector2)

def get_cosine_dictance(vector1, vector2):
    return cosine(vector1, vector2)

def get_euclidean_dictance(vector1, vector2):
    return euclidean(vector1, vector2)

def get_sqeuclidean_dictance(vector1, vector2):
    return sqeuclidean(vector1, vector2)

if __name__ == "__main__":
    ala = get_standard_vector([(1L, [4]), (2L, [26]), (3L, [0, 23])])
    kota = get_standard_vector([(1L, [5]), (2L, [5]), (3L, [5])])
    ma = get_standard_vector([(1L, [5]), (2L, [5]), (3L, [5])])
    vectors = [ala, ma, kota]
    print get_standard_vectors_union(vectors)
