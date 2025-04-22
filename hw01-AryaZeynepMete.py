"""
Assignment 1 - Code template for AIN442/BBM497

@author: İsmail Furkan Atasoy
"""
#Arya Zeynep Mete
import re
import codecs
from collections import defaultdict

def initialVocabulary():
    
    # You can use this function to create the initial vocabulary.
    
    return list("abcçdefgğhıijklmnoöprsştuüvyzwxq"+
                "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZWXQ"+
                "0123456789"+" "+
                "!'^#+$%&/{([)]=}*?\\_-<>|.:´,;`@€¨~\"é")

def initialize_tokenized_corpus(corpus):
    # initialize the tokenized corpus by splitting the input corpus into words
    # and add space and _ characters
    return [[' '] + list(word) + ['_'] for word in corpus.split()]

def get_stats(tokenized_corpus):
    # computes the frequency of all bigrams in the tokenized corpus
    pairs = defaultdict(int)
    for word in tokenized_corpus:
        for i in range(len(word) - 1):
            pairs[(word[i+1], word[i])] += 1
    return pairs

def merge_pair(pair, tokenized_corpus):
    # merges the most frequent pair in the tokenized corpus
    new_tokenized_corpus = []
    for word in tokenized_corpus:
        new_word = []
        i = 0
        while i < len(word):
            if i < len(word) - 1 and (word[i], word[i+1]) == pair:
                new_word.append(word[i] + word[i+1])  # merge the pair
                i += 2
            else:
                new_word.append(word[i])
                i += 1
        new_tokenized_corpus.append(new_word)
    return new_tokenized_corpus

def bpeCorpus(corpus, maxMergeCount=10):
    # token learner function that processes the input corpus and performs BPE merges

    if (maxMergeCount==0):
        merges = []
        vocabulary = initialVocabulary()
        tokenized_corpus = initialize_tokenized_corpus(corpus)
        return merges, vocabulary, tokenized_corpus


    # initialize the tokenized corpus
    tokenized_corpus = initialize_tokenized_corpus(corpus)
    
    # initialize the vocabulary with the initial set of characters
    vocabulary = initialVocabulary()
    
    # store the merges in the order they are performed
    merges = []
    
    # perform merge operations up to maxMergeCount times
    for _ in range(maxMergeCount):
        # get the frequency of all bigrams
        stats = get_stats(tokenized_corpus)
        
        # function to reverse the pairs 
        def reverse_stats(stats):
            reversed_stats = defaultdict(int)
            for pair, count in stats.items():
                reversed_pair = (pair[1], pair[0])
                reversed_stats[reversed_pair] = count
            return reversed_stats

        # reverse the stats
        reversed_stats = reverse_stats(stats)
        stats = reversed_stats
 
        if not stats:
            break  # no more merges 

        # convert the dic to a list of items to keep track of their order
        stats_items = list(stats.items())
        # find the most frequent pair, prioritizing frequency first, then the order in which they appear
        most_frequent_pair = max(stats_items, key=lambda x: (x[1], -stats_items.index(x)))[0]
        
        # add the merge 
        merges.append((most_frequent_pair, stats[most_frequent_pair]))
        
        # update the tokenized corpus by merging the most frequent pair
        tokenized_corpus = merge_pair(most_frequent_pair, tokenized_corpus)
        
        # add the new token
        new_token = most_frequent_pair[0] + most_frequent_pair[1]
        if new_token not in vocabulary:
            vocabulary.append(new_token)
    
    return merges, vocabulary, tokenized_corpus


def bpeFN(fileName, maxMergeCount=10):

    # TO DO
    # You can refer to Example 4 and 5 for more details.

    # reads the corpus from a file and calls bpeCorpus.
    with codecs.open(fileName, 'r', encoding='utf-8') as file:
        corpus = file.read()
    return bpeCorpus(corpus, maxMergeCount)

    return  # Should return (Merges, Vocabulary, TokenizedCorpus)

def bpeTokenize(str, merges):

    # TO DO
    # You can refer to Example 6, 7 and 8 for more details.

    # initialize the tokenized string by splitting it into chars
    tokenized_str = [[' '] + list(word) + ['_'] for word in str.split()]
    
    # apply the merges in the order they were learned
    for pair, _ in merges:
        new_tokenized_str = []
        for word in tokenized_str:
            new_word = []
            i = 0
            while i < len(word):
                if i < len(word) - 1 and (word[i], word[i+1]) == pair:
                    new_word.append(word[i] + word[i+1])  # merge the pair
                    i += 2
                else:
                    new_word.append(word[i])
                    i += 1
            new_tokenized_str.append(new_word)
        tokenized_str = new_tokenized_str

    return tokenized_str # Should return the tokenized string as a list

def bpeFNToFile(infn, maxMergeCount=10, outfn="output.txt"):
    
    # Please don't change this function. 
    # After completing all the functions above, call this function with the sample input "hw01_bilgisayar.txt".
    # The content of your output files must match the sample outputs exactly.
    # You can refer to "Example Output Files" section in the assignment document for more details.
    
    (Merges,Vocabulary,TokenizedCorpus)=bpeFN(infn, maxMergeCount)
    
    outfile = open(outfn,"w",encoding='utf-8')
    outfile.write("Merges:\n")
    outfile.write(str(Merges))
    outfile.write("\n\nVocabulary:\n")
    outfile.write(str(Vocabulary))
    outfile.write("\n\nTokenizedCorpus:\n")
    outfile.write(str(TokenizedCorpus))
    outfile.close()

#bpeFNToFile("hw01_bilgisayar.txt", maxMergeCount=1000, outfn="output.txt")