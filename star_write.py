#choice = 'True'
name = input('Enter Constellation Name: ')

while True:
    with open(name+".txt", 'a') as c:
        sn = input('Enter star name: ')
        ra = input('Enter right ascension: ')
        dec = input('Enter declination: ')
        c.write(sn+': (')
        c.write(ra+', ')
        c.write(dec+')')
        c.write('\n')
        c.close()
        d = open(name+'.txt')
        d.read()
        d.close()
        choice2 = input('Y or n:')
        if choice2 == 'n' or choice2 == 'N':
            break
            c.read()
            c.close()
        else:
            print()
            sn = input('Enter star name: ')
            ra = input('Enter right ascension: ')
            dec = input('Enter declination: ')
            c = open(name+".txt", 'a')
            c.write(sn+': (')
            c.write(ra+', ')
            c.write(dec+')')
            c.write('\n')
            c.close()
            d = open(name+'.txt')
            d.read()
            d.close()
            choice = input("True or False: ")
            if(choice == "False"):
                break
            print()
