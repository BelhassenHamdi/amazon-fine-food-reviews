import pandas as pd
import numpy as np
import re
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
from nltk.tokenize import word_tokenize
from collections import Counter
from autocorrect import spell


# Inoticed that there are some HTML murkups in text so we need to get rid of 
# them toward getting 
# clean data for tokenization
def cleanhtml(raw_html):
	'''
	cleanhtml removes HTML markups from the text
	'''
	cleanr = re.compile('<.*?_>')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext

def text_tokenizer(example_sent):
	'''
	tokenizer gets as input the text data and outputs a tokenized data
	'''
	tokenz = tokenizer.tokenize(example_sent)
	toke = [word for word in tokenz if word.isalpha()]
	return toke


def viterbi_segment(text_i):
    probs, lasts = [1.0], [0]
    for i in range(1, len(text_i) + 1):
        prob_k, k = max((probs[j] * word_prob(text_i[j:i]), j)
                        for j in range(max(0, i - max_word_length), i))
        probs.append(prob_k)
        lasts.append(k)
    words = []
    i = len(text_i)
    while 0 < i:
        words.append(text_i[lasts[i]:i])
        i = lasts[i]
    words.reverse()
    return words, probs[-1]

def word_prob(word): return dictionary[word] / total
def words(text_i): return re.findall('[a-z]+', text_i.lower()) 

dictionary = Counter(words(open('new_big.txt').read()))
max_word_length = max(map(len, dictionary))
total = float(sum(dictionary.values()))

def word_vocab_proc(text):
	vocab = cleanhtml(text)
	vocab = vocab.lower()
	return text_tokenizer(vocab)

data_path = "."
data_file = "Reviews.csv"

data = pd.read_csv(data_path+"/"+data_file)

data = data[['Summary','Text']]
data.dropna(inplace=True)

word_vocab = []
for index, row in data.iterrows():
	word_vocab += word_vocab_proc(row[0])
	word_vocab += word_vocab_proc(row[1])

# word_vocab = set(word_vocab)
# word_vocab = list(word_vocab)
final_word_string = ' '.join(word for word in word_vocab)


with open("word_count.txt","w") as file:
	file.write(final_word_string)
# print("vocab length: ", len(word_vocab))

# verified_vocab = []
# for word in word_vocab:
# 	word = spell(word) 
# 	word2 = viterbi_segment(word)
# 	if word2[1] > 10^-7:
# 		for _word in word2[0]:
# 			verified_vocab.append(_word)
# 	else :
# 		verified_vocab.append(word)
# # for word in word_vocab:
# # 	word1 = spell(word) 
# # 	if word != word1:
# # 		verified_vocab.append(word1)
# # 	else:
# # 		word2 = viterbi_segment(word)
# # 		if word2[1] > 10^-7:
# # 			for _word in word2[0]:
# # 				verified_vocab.append(_word)
# # 		else:
# # 			verified_vocab.append(word)

# print(verified_vocab)

def sentence_splitter(x):
	return x.split('. | , | ;')