f= open("song.txt", "r")
text = f.read()
texts = text.split()
count = {}

for text in texts :
    if text in count:
        count[text]+=1
    else:
        count[text]=1

for text in count:
    if count[text] == 1:
        print(text)

countUnique = sum(1 for text in count if count[text]==1)

print(f"Ukupan broj jedinstvenih rijeci: {countUnique}")
