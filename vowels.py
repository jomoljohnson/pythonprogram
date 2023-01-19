text=input("Enter the text:")
word=["a","e","i","o","u"]
for i in text:
    j=i.split(",")
    for x in word:
        s=x.split(",")
        if j==s:
            print(s)
