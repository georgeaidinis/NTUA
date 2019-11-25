# -*- coding: utf-8 -*-

from nltk.tokenize.regexp import regexp_tokenize
import itertools



"""
------------------------------------------------------BHMA 1------------------------------------------------------------------------

To bima1 exei ginei ektos tou arxeiou autou, ta corpora pou sillexthikan einai ta 2 proteinomena kai synenwthikan se ena megalo, to 
arxeio corpora.txt.
"""



"""
------------------------------------------------------BHMA 2------------------------------------------------------------------------
"""


"""Reads a string and returns it. Returns string."""
def identity_preprocess(stringaki):
	return stringaki



"""Takes 2 arguments, one being the filepath and the second
being the name of the method that reads the string, defaulting
to the above method, 'identity_preprocess'. Returns a list of
strings, that are the whole text of the file."""
def read_from_file(filepath, myfunc = identity_preprocess):
	lines = []
	with open(filepath) as file:
		for line in file:
			lines.append(myfunc(line))
	return lines



"""Takes a text and splits it between whitespaces or \n. Returns
a list of strings"""
def tokenize(text):
	text = text.split()
	return text



"""Uses the imported library from nltk to return a list of strings
created by using regular expressions. It is one of the fastest 
tokenizers."""
def Tokenize(text):
	return regexp_tokenize(text, pattern = '\s+', gaps = True)



"""Takes one string and returns a string that has only lowercase
letters, that means exluding any non-alphanumeric sumbols, numbers
punctuation."""
def clean_text(text):
	#replace new line and carriage return
	text = text.replace("\n", " ").replace("\r", " ")
	#replace the numbers, symbols and punctuation with space
	punc_list = '~`!@#$£½%^&*()_+-—“”’‘\'=}{|:à"?>æ<âç,œ./è;é][}' + '1234567890'
	t = str.maketrans(dict.fromkeys(punc_list, " "))
	text = text.translate(t)
	#make everything lowercase
	text = text.lower()
	return text



"""Takes a list of lists and returns a list. Elements are kept in
order."""
def flatten(l):
	return list(itertools.chain(*l))


"""
------------------------------------------------------BHMA 3------------------------------------------------------------------------
"""


"""Takes a list of strings (tokens) and reduces it to only unique
elements. (gets rid of the duplicates). Returns a list of strings
that are unique and sorted."""
def unique_tokens(tokens):
	lexicon = list(set(tokens))
	lexicon.sort()
	return lexicon



"""Takes a string and returns a list of the characters 
that were used to make the strings."""
def split_word(word):
	return [char for char in word]



"""Takes a list of strings as an input and returns a list of chars.
The characters that are returned are used to make the elements of 
the input strings, but they are returned duplicate-free and sorted."""
def alphabet(words):
	chars = []
	for word in words:
		chars.append(split_word(word))
	alpbt = list(set(flatten(chars)))
	alpbt.sort()
	return alpbt



"""
------------------------------------------------------BHMA 4------------------------------------------------------------------------
"""


"""Takes an alphabet (list of chars) and assigns each character 
an index. Index 0 is <epsilon> (ε). Returns a list that has n+1 
tuples, each tuple being the character with its assigned index."""
def alphabet_indexing(alphabet):
	indexed_alphabet = []
	indexed_alphabet.append(("<epsilon>", 0))
	i = 1;
	for letter in alphabet:
		indexed_alphabet.append((letter, i))
		i+=1
	return indexed_alphabet



"""Takes two arguments. The first is an  alphabet and the 
second is the name of the file to write the output. The 
method takes the indexed alphabet and writes it to a file 
with the name given"""
def symbols_file(alphabet, filename = "chars.syms"):
	ind_alph = alphabet_indexing(alphabet)
	f = open(filename, "w+")
	for pair in ind_alph:
		f.write(pair[0] + "\t\t" + str(pair[1]) + "\n")



"""
------------------------------------------------------BHMA 5------------------------------------------------------------------------
"""


"""This function computes the Levenshtein distance between two 
chars s,t. It uses the algorithm mentioned in the instructions
of the lab, and is horribly inefficient. Takes two arguments, both
chars and returns an integer that is the levenshtein distance of
the two strings."""
def my_levenshtein(s,t):
	#same characters, no edit => Levenshtein cost 0
	if (s==t):
		return 0
	#<epsilon> with some other character or any character with <epsilon>
	#either insertion or deletion => Levenshtein cost 1
	elif (s=='<epsilon' and t!='<epsilon>') or (s!='<epsilon' and t=='<epsilon>'):
		return 1
	#two different chars, substiturion => Levenshtein cost 1
	else:
		return 1



"""This function computes the Levenshtein distance between two 
strings s,t. It uses the iterative algorithm, that creates a 
2d matrix of the characters of the strings, along with the 
values it needs to compute the sum of the weights of the insert
/delete/substitute logic. It is a much faster algorithm than the
recursive one. The method takes 3 arguments, string s, string t
and a tuple of 3 integeres that are the cost of deletion, insertion
and substitution respectively. Defaults to (1,1,1) (equal cost).
I have taken the code for this method from:
https://www.python-course.eu/levenshtein_distance.php 
Another method could have been the method given in
the python package python-Levenshtein (0.12.0) that uses python to 
instruct C to compute the afforementioned array, with much faster 
execution times."""
def iterative_levenshtein(s, t, costs=(1, 1, 1)):
    """ 
        iterative_levenshtein(s, t) -> ldist
        ldist is the Levenshtein distance between the strings 
        s and t.
        For all i and j, dist[i,j] will contain the Levenshtein 
        distance between the first i characters of s and the 
        first j characters of t
        
        costs: a tuple or a list with three integers (d, i, s)
               where d defines the costs for a deletion
                     i defines the costs for an insertion and
                     s defines the costs for a substitution
    """
    rows = len(s)+1
    cols = len(t)+1
    deletes, inserts, substitutes = costs
    
    dist = [[0 for x in range(cols)] for x in range(rows)]
    # source prefixes can be transformed into empty strings 
    # by deletions:
    for row in range(1, rows):
        dist[row][0] = row * deletes
    # target prefixes can be created from an empty source string
    # by inserting the characters
    for col in range(1, cols):
        dist[0][col] = col * inserts
        
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                cost = substitutes
            dist[row][col] = min(dist[row-1][col] + deletes,
                                 dist[row][col-1] + inserts,
                                 dist[row-1][col-1] + cost) # substitution
    """for r in range(rows):
        print(dist[r])
    """ 
    return dist[row][col]



"""
------------------------------------------------------BHMA 6------------------------------------------------------------------------
"""


"""blah blah"""
def new_func():
	pass


def main():
	lines = read_from_file("corpora.txt")
	text = []
	for line in lines:
		text.append(Tokenize(clean_text(line)))
	text = flatten(text)
	Lexicon = unique_tokens(text)
	Alphabet = alphabet(Lexicon)
	symbols_file(Alphabet)
	print(iterative_levenshtein("George", "Elena"))
	
if __name__ == '__main__':
		main()	
