"""
Задача с прошлого курса
"""

import re
def isRUS(text):
	return bool(re.search('[а-яА-Я]', text))
en = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP',	4:'FHVWY', 5:'K', 8:'JX', 10:'QZ'}
ru = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ',	4:'ЙЫ',	5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ'}
word = input("Введите слово для оценки стоимости: ").upper()
if isRUS(word):
	print(sum([k for i in word for k, v in ru.items() if i in v]))
else:
	print(sum([k for i in word for k, v in en.items() if i in v]))