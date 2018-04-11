import pandas as pd

data = pd.read_csv('urban_dictionary.csv')
data = data[['definition','word','tags']]



def hachtags_processing(x):
	'''
	This function removes hashtags and all special characters
	'''
	text = x.split(' ')
	new_text = []
	for texte in text:
		texte = ''.join(e for e in texte if e.isalnum())
		texte = texte[1:]
		new_text.append(texte)
		final_text = ' '.join(e for e in new_text)
	return final_text


data['tags'] = data.tags.apply(hachtags_processing)


full_dictionnary = ''
for index, item in data.iterrows():
	full_dictionnary = ' '.join([full_dictionnary,item[0],item[1],item[2]])

out_file = open("new_big.txt",'w')
with open("big.txt", "r") as in_file:
    buf = in_file.readlines()
    for line in buf:
        if line == "Retrieved from \"http //en wiktionary org/wiki/Wiktionary Frequency_lists/PG/ / / \"\n":
            line = '\n' + full_dictionnary + '\n' + line
        out_file.write(line)



# def hachtag_removal(x):
# 	x = 

print(full_dictionnary)