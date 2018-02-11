def count(sequence, item):
	total = 0 #the number of times the word is repeated
	if type(sequence) == list:
		for element in sequence:
			if element == item:
				total+=1
	print('The number of matches are: ', total)

#actual code
from nltk.tokenize import wordpunct_tokenize
string = "Hey bad body. you are bad bad bad. good bye bad"
tok = wordpunct_tokenize(string)
count(tok, 'bad')
