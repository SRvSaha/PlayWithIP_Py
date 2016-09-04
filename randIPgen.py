#random IP generator...

from random import randrange

for i in range (0, 10000): #increase th range if you want more...

    blockOne = randrange(0, 255, 1)
    blockTwo = randrange(0, 255, 1)
    blockThree = randrange(0, 255, 1)
    blockFour = randrange(0, 255, 1)

    ip =  str(blockOne) + '.' + str(blockTwo) + '.' + str(blockThree) + '.' + str(blockFour)
    f = open('iplist.txt','a+')
    f.write(ip+'\n')
    f.close()


