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

#allows preferences for files and row length via commanline argument
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("infile", nargs = '?', default = None, help = "Enter is the text file you want to open.")
parser.add_argument("outfile", nargs = '?', default = None, help = "Enter the filename you wish to save to.")
parser.add_argument("rowlen", nargs = '?', default = None, help="Enter your desired number of stitches per row.", type=int)

args = parser.parse_args()

#prompts user for data if args not given
if args.infile is None:
    handle = open(input("What file do you want to use? "), "r")
else:
    handle = open(args.infile, "r")

if args.outfile is None:
    finish = input("What filename would you like to save to? ")
else:
    finish = args.outfile

if args.rowlen is None:
    stlength = len(range(int(input("How many stitches would you like in a row? ")))) - 1
else:
    stlength = len(range(args.rowlen)) - 1

#converts text doc to binary format
contents = handle.read()
cbin = ""

for i in contents:
  cbin += bin(ord(i))[2:].zfill(8)

#set up for dividing data into usable rows
countone = 0
counttwo = 0
wlist = False

listone = ""
listtwo = ""

#churns through every item in cbin, assigns to either listone or listtwo, light formatting
#checks is wlist is true or false to determine which list to write to
#appends i to chosen list
#checks item count against max row length
#adds either space or new line depending on count, adds 1 to counter or rests depending on count, toggles wlist
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


#replaces 1s and 0s in pattern with stitch types
#splits up lists by making each line 1 item
lone = listone.replace("0", "k").replace("1", "p").splitlines()
ltwo = listtwo.replace("0", "p").replace("1", "k").splitlines()

#sets up list for final pattern, defines blank space for final pattern
clist = ""
aline = "k " * (stlength + 1)

#alternates between listone and listtwo to append to final pattern with blank lines in between
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

#saves final pattern to new file
fileone = open(finish, "w")
fileone.write(clist)
fileone.close()
