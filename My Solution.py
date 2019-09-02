from time import process_time as pt
from collections import defaultdict as dd
import os
os.chdir#BLOCKED PATH FOR PRIVACY
lines = open('.\Advent.txt').read().splitlines()

#We're gonna be referencing this extended alphabet
Alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA', 'BB','CC','DD','EE','FF','GG','HH','II','JJ','KK','LL','MM','NN','OO','PP','QQ','RR','SS','TT','UU','VV','WW','XX','YY','ZZ']

#Finds the max x and y coordinate in the module and adds 1 to it
xr = int(sorted(lines, key = lambda x: int(x.split(', ')[0]), reverse = True)[0].split(', ')[0])+1
yr = int(sorted(lines, key = lambda x: int(x.split(', ')[1]), reverse = True)[0].split(', ')[1])+1

#Filling out the whole map with dots
map = {}
for y in range(yr):
    for x in range(xr):
        map[x,y] = '.'

#Turns the string inputs into a tuple. We are only calling this to reference lines in a for loop below
def makeTup(x):
    test3 = x.split(', ')
    for i in range(len(test3)):
        test3[i] = int(test3[i])
    return tuple(test3)

base = {}

#Setting the coordinates indicated to their letters instead of dots. Also making a dictionary letters as key and coords as value (not super important, takes no time)
for i in range(len(lines)):
    #print(makeTup(lines[i]))
    map[makeTup(lines[i])] = Alpha[i]
    base[Alpha[i]] = makeTup(lines[i])

count = dd(int)
mini = {}
mapO = map.copy()

#This checks every dot on the grid and sees what it's closest to. For whatever reason, even after simplifying it, this is the part that takes  up the most time. Even though the sorted function in the other program should be taking a lot of time
for i in map:
    if map[i] == '.':
        letter = 0
        mini = 0
        for c in base:
            tempx = abs(base[c][0]-i[0])
            tempy = abs(base[c][1]-i[1])
            result = (tempx+tempy)
            if result == mini:
                letter = '.'
            elif result < mini or mini == 0:
                mini = result
                letter = c
        map[i] = letter.lower()
        if letter != '.':
            count[letter] = count[letter] + 1
    else:
        pass

#Part of the prompt of this fake map we are filling out involves bases radiating outwards. But we are not supposed to count letters that radiate to the edge of the map, as they are
#considered infinite. So this block deletes infinite letters from the overall count
for i in map:
    if i[0] in [xr-1, 0] or i[1] in [yr-1, 0]:
        try:
            del count[map[i].upper()]
        except:
            pass

#Now, since we were counting every letter as it was added, we just sort the list by largest, and print that number
print('part 1 answer is', count[sorted(count, key = count.get, reverse = True)[0]]+1)
print('Part 1 of program was up forProgram was up for', pt(), 'seconds')
