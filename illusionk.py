#read file
#remove spaces and newlines
#cut into 64 bit chunks

#take one line write to list
#take next line write to other list

#in first list convert 0 to k, 1 to p
#insert comma between each item
#in second list convert 0 to p, 1 to k

#recombine lists
#add wrong row formatting

#save to new file
import sys
print(sys.argv)

handle = open(input("What file do you want to use? "), "r")
finish = input("What filename would you like to save to? ")
stlength = len(range(int(input("How many stitches would you like in a row? ")))) - 1

contents = handle.read()
cbin = ""

for i in contents:
  cbin += bin(ord(i))[2:].zfill(8)

countone = 0
counttwo = 0
wlist = False

listone = ""
listtwo = ""

for i in cbin:

    if wlist:
        listtwo += i
        if counttwo < stlength:
            listtwo += " "
            counttwo += 1
        else:
            listtwo += "\n"
            counttwo = 0
            wlist = not wlist

    else:
        listone += i
        if countone < stlength:
            listone += " "
            countone += 1
        else:
            listone += "\n"
            countone = 0
            wlist = not wlist



lone = listone.replace("0", "k").replace("1", "p").splitlines()
ltwo = listtwo.replace("0", "p").replace("1", "k").splitlines()

clist = ""
aline = "k " * (stlength + 1)

for i in range(len(lone)):
    clist += aline
    clist += "\n"
    clist += lone[i]
    clist += "\n"
    if i < len(ltwo):
        clist += aline
        clist += "\n"
        clist += ltwo[i]
        clist += "\n"


fileone = open(finish, "w")
fileone.write(clist)
fileone.close()
