sentence = input ("ჩაწერე წინადადება:").strip().split()
mydict = {}
for word in sentence:
    mydict[word] = len(word)
print(mydict)