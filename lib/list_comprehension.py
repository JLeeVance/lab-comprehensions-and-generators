#!/usr/bin/env python3

def return_evens(num_list):
    even_return = [n for n in num_list if n % 2 == 0]
    return even_return

    

def make_exclamation(sentence_list):
    if len(sentence_list) == 0:
        return []
    else:
        excited_list = [sentence + "!" for sentence in sentence_list ]
        return excited_list