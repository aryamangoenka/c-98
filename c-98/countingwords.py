def countwords():
    test1=input("enter the file name ")
    words=0
    file=open(test1,"r")
    for line in file:
        word=line.split()
        print(word)
        words=words+len(word)
    print("no. of words ")
    print(words)
countwords()
