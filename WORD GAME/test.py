#!/usr/bin/python
#_*_coding:utf-8_*_
#杂杂杂：检测代码正确性
def for_(x):
	for i in range(x):
		if i == 2:
			return 'gogogo'
		else:
			return  'jiehsu'


print for_(10)


def isValidWord(word, hand, wordList):
		s = True
		newhand = hand
		for i in word:
			if i in hand:
					newhand[i] -= 1
					if newhand[i] < 0:
							s = False
							break
			else:
				s = False
				break
	
		if word.upper() in wordList and s:
			return True
		else:
			return False


def search(L, e):
	for i in L:
		if i == e:
			return True
		if i < e:
			return False
	return False
	
def search1(L, e):
	for i in range(len(L)):
		if L[i] == e:
			return True
		if L[i] < e:
			return False
	return False
l = [1,2,3,4,5,6,7,8,9]
l2 = l[-1:-10:-1]

print search(l, 5)
print search1(l2, 5)
print l2	