##Import the relevant libraries for this project
import pandas as pd
import numpy as np
import string

##Open the AFINN-1111 Sentiment File
##It's important to note this is not a csv file, but more of a tsv, but you can still
##use pandas just need to sep = '/t'
finn_data = pd.read_csv('E:\Data Science Project\AFINN1111 Project\AFINN-111.txt', sep = "\t", header=None)
finn_data.columns = ["key", "score"]

## the file is opened appropriately, but we will create dictionary with AFINN file
## First, seperate into names & scores for the file
names = []
scores = []

## Next, will parse through the original file and will add them both to the appropriate lists
for n in finn_data['key']:
    names.append(n)
for m in finn_data['score']:
    scores.append(m)

## Now, combine the lists together to create the dictionary
finn_scores = dict(zip(names, scores))

## This function is used to preprocess the text for comparison inbetween the user input & AFINN 111.
## First, the text will eliminate any possible stopwords which might be irrelevant to the comparison
## should remove punctuation from words. Finally, will result in a list of words from user input
def preprocess_text(text):
	stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
	relevant_words = []
	lower_text = text.lower()
	remove_punc = lower_text.strip(string.punctuation)
	split_words = remove_punc.split()
	for words in split_words:
		if words not in stop_words:
			relevant_words.append(words)
	return relevant_words

## This function will perform the anlysis comparing the list of words from the preprocess function to the AFINN 111 list.
## This function will create a score and will assess whether the score is positive or negative
## if the value of the score is 0 then it is possibly inferred that the analysis has been inconclusive
## This can be from the lack of words that compare to scores within the AFINN 111 list, or this can be because 
## the scores may cancel each other out.
def sentiment_analysis(word_list):
	score = 0
	positive = "This sentence / word seems to be a positive one"
	negative = "This sentence / word seems to be a negative one"
	for words in word_list:
		if words in finn_scores:
			score += finn_scores[words]
	if score > 0:
		return positive
	elif score < 0:
		return negative
	else:
		return "AFINN cannot assess input sentiment from its list"

if __name__ == '__main__':
	print("Input text for sentiment analysis: ")
	user_input = input()
	bag_of_words = preprocess_text(user_input)
	sentiment = sentiment_analysis(bag_of_words)
	print(sentiment)