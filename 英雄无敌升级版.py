mapmsg = '#########'

worldmap = ['#', '#', '#', '#', '#', '#', '#', '#', '#']
instruction = ''' Control your hero:|'a' for left | 'd' for right |'''

print("welcome")

name = input("input your name:")
hp = 100
ad = 100
ap = 0

if not name:
    name = 'player1'

usermsg = {'name': name, 'hp': hp, 'ap': ap, 'ad': ad}

print("HI!", usermsg['name'], 'You hp is:', usermsg['hp'], 'You ap is:', usermsg['ap'], 'You ad is:', usermsg['ad'])

point = 0
while 1:
    worldmap[point] = "*"
    print('you are here', "".join(worldmap))
    userinput = input('go or quit:')

    if userinput == 'd' and point < 8:
        worldmap[point] = '#'
        point += 1
    elif userinput == 'a' and point > 0:
        worldmap[point] = '#'
        point -= 1
    elif userinput == 'quit':
        print("goodbye!!!")
        break
    else:
        print(instruction)