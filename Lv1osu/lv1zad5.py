with open("SMSSpamCollection.txt", "r") as f:
    masseges = f.readlines()

ham = 0
spam = 0
usklicnik = 0
ham_words= 0
spam_words = 0

for massage in masseges : 
    part = massage.strip().split("\t")
    if len(part) == 2:
        x = part[0]
        y = part[1]
        count_words = len(y.split())

        if x == "ham":
            ham_words += count_words    
            ham += 1
        else:
            spam_words += count_words
            spam+=1
            if(y.endswith("!")):
                usklicnik+=1

print(f"Prosjecan broj rijeci u ham: {ham_words/ham}")
print(f"Prosjecan broj rijeci u spam: {spam_words/spam}")
print(f"Spam poruke koje zavrsavaju s ! : {usklicnik}")


        