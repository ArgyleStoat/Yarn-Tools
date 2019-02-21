import random

def tentacular(tents, length):
    twist = 'TWIST'
    count = 0

    while count < tents:
        tentacount = 0
        tentacle = ''

        while tentacount < length:
            tempval = random.choice(range(3))
            if tempval + tentacount >= length:
                continue
            if tempval == 0:
                tentacle += twist
                tentacle += '\n'
                tentacount += (int(tempval) + 1)
            else:
                tentacle += twist
                tentacle += '\n'
                tentacle += str(tempval)
                tentacle += '\n'
                tentacount += (int(tempval) + 1)

        print('Length: ' + '\n' + str(tentacount) + '\n' + '\n' + 'Pattern: ' + '\n' + '\n' + tentacle)
        count += 1
