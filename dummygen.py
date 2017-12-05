import random as r
import string

file_names = open("n1.txt", "r")
file_surnames = open('names.txt', 'r')

#Nested list
#Each list inside these lists has a letter just for identification purposes
#After the names are inserted in the list, these letters are removed

list_names = [
	['a'], 
	['b'], 
	['c'], 
	['d'], 
	['e'], 
	['f'],
	['g'],
	['h'],
	['i'],
	['j'], 
	['k'],
	['l'],
	['m'],
	['n'],
	['o'],
	['p'],
	['q'],
	['r'],
	['s'],
	['t'],
	['u'],
	['v'],
	['w'],
	['x'],
	['y'],
	['z']
]

list_surnames = [ 
	['a'], 
	['b'], 
	['c'], 
	['d'], 
	['e'], 
	['f'],
	['g'],
	['h'],
	['i'],
	['j'], 
	['k'],
	['l'],
	['m'],
	['n'],
	['o'],
	['p'],
	['q'],
	['r'],
	['s'],
	['t'],
	['u'],
	['v'],
	['w'],
	['x'],
	['y'],
	['z']
]

for line in file_names:
	for i in string.ascii_uppercase:
		if(line.strip().startswith(i)):
			i = i.lower()
			#list_names[i].append(line.strip().lower().capitalize())
			list_names[[n for n in range(0, len(list_names)) if list_names[n][0] == i][0]].append(line.strip().lower().capitalize())

#Close the file_names
file_names.close()

for line in file_surnames:
	for i in string.ascii_lowercase:
		if(line.strip().startswith(i.upper())):
			list_surnames[[n for n in range(0, len(list_surnames)) if list_surnames[n][0] == i][0]].append(line.strip().lower().capitalize())

#Close the file_surnames
file_surnames.close()

for i in list_names:
    i.pop(0)
for i in list_surnames:
    i.pop(0)

nomes = [list_names[x][y]+' '+list_surnames[j][k] 
		for x in range(0, len(list_names)) 
		for y in range(0, len(list_names[x])) 
		for j in range(0, len(list_surnames)) 
		for k in range(0, len(list_surnames[j])) 
		if list_names[x][y] != list_surnames[j][k]]

#Now we store the names in a txt file
arq = open("nomes_result.txt", "w")

for n in nomes:
    arq.write(n + "\n")

arq.close()

print(len(nomes))
