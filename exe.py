from itertools import count


fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line>split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for k, v in counts.items():
    newtup = (v, k)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
for v, k in lst[:10]:
    print(k, v)

#Esse programa irá contas a quantidade de vezes que uma palavra aparece, e rankear o top 10 das palavras.
