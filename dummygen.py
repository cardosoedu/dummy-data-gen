import random as r
import string
import datetime

names_file = "names_teste1.txt"
surnames_file = "surnames_teste1.txt"

def list_from_file(filename, listname):
	for line in filename:
		if line.strip() != '':
			listname.append(line.strip().lower().capitalize())
	return listname

def listofnames(listnames, listsurnames):
	return sorted([listnames[x]+' '+listsurnames[y] for x in range(0, len(listnames)) for y in range(0, len(listsurnames)) if listnames[x] != listsurnames[y]])

def random_names(listname, max_names, listresult):
	rand = r.sample(range(0, len(listname)), max_names)
	for n in range(0, max_names):
		listresult.append(listname[rand[n]])
	return listresult

def gen_dateofbirth():
	dstart = datetime.date(1940, 1, 1)
	ddif = (datetime.date(2000, 1,1 )-dstart).days
	drand = r.randint(0, ddif)
	return dstart+datetime.timedelta(days=drand)

def gen_email(name):
	providers = ['@gmail.com', '@hotmail.com', '@outlook.com', '@yahoo.com', '@bol.com']
	namesplit = name.lower().split()
	decider = r.randint(0, 10)	
	randprov = providers[r.randint(0, len(providers)-1)]
	if decider > 8:
		return namesplit[0]+"_"+namesplit[1]+randprov
	elif 5 <= decider <= 8:
		return namesplit[1]+"_"+namesplit[0]+randprov
	elif 3 <= decider <= 5:
		return name.replace(" ", "").lower()+str(r.randint(100, 999))+randprov
	else:
		return name.replace(" ", "").lower()+randprov

def makeDict(listnames):
	dic = {}
	for name in listnames:
		email = gen_email(name)
		birth = gen_dateofbirth()
		dic[name] = [email, birth]
	return dic

def dictToCSV(dic, filename):
	strcsv = ''
	templist = []
	for key, val in dic.items():
		strcsv += key+','+val[0]+','+str(val[1])+"\n"
	strcsv = strcsv[:-1]
	if filename:
		fileio = open(filename, "w")
		for line in strcsv:
			fileio.write(line)
		fileio.close()
	return strcsv

if __name__ == '__main__':
	file_names = open(names_file, "r")
	file_surnames = open(surnames_file, "r")

	list_names = list_from_file(file_names, [])
	list_surnames = list_from_file(file_surnames, [])

	file_names.close()
	file_surnames.close()
	
	names = listofnames(list_names, list_surnames)
	dicnames = makeDict(names)
	csv = dictToCSV(dicnames, 'csv.txt')