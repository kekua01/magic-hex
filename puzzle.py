import os
import math

#the initial set
pset = set()
for i in range(1, 20):
	pset.add(i)


def newset(oldset, removed):
	nset = oldset.copy()
	for i in removed:
		nset.remove(i)
	return nset

#kset, which holds all of the 3-num = 38 combos
kset = set()
for i in pset:
	leastval = 19 - i
	nset = newset(pset, (i,))
	for j in nset:
		if j >= leastval and j*2 != (38 - i) and i*2 + j != 38:
			kset.add((i, j, 38-i-j))

#returns set containing tuples of two nums, which along with init add to 38
def find_2(init, pset):
	leastval = 19 - init
	nset = set()
	for i in pset:
		if i >= leastval and i*2 != (38 - init) and init*2 + i != 38:
			nset.add((i, 38-i-init))
	return nset	

def find_3(init, pset):
	nset = set()
	for i in pset:   #nine
		for j in newset(pset, (i,)):    #five
			for k in newset(pset, (i, j)):
				if k + j + i + init == 38:
					nset.add((i, j, k))
	return nset

def find_4(init, pset):
	nset = set()
	for i in pset:   #nine
		for j in newset(pset, (i,)):    #five
			for k in newset(pset, (i, j)):
				for l in newset(pset, (i, j, k)):
					if k + j + i + init + l == 38:
						nset.add((i, j, k, l))
	return nset

def check_half(x):
	f = x[0]
	s = x[1]
	t = x[2]
	set1 = newset(pset, x)
	for i in find_2(f, set1):
		set2 = newset(set1, i)
		for j in find_3(s, set2):
			set3 = newset(set2, j)
			for k in find_4(t, set3):
				if i[1] + j[2] + k[3] == 38:
					set4 = newset(set3, k)
					for l in find_4(0, set4):
						if l[0] + k[0] + j[0] + i[0] == 38 and i[0] + j[1] + k[2] + l[3] == 38:
							set5 = newset(set4, l)
							for p in find_3(0, set5):
								if (p[2] + l[3] + k[3] == 38 and p[1] + l[2] + k[2] + j[2] == 38
									and p[0] + l[1] + k[1] + j[1] + i[1] == 38
									and p[2] + l[2] + k[1] + j[0] + f == 38
									and p[1] + l[1] + k[0] + s == 38):
									return (x, i, j, k, l, p)
	return False

c = 1
for i in kset:
	print(c)
	print(check_half(i))
	c+=1