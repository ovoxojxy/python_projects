for i in range(99,0, -1):
    if i > 2:
        print ('{0} bottles of beer on the wall, {0} bottles of beer. Take one down pass it around, {1} bottles of beer on the wall.'.format(i, i-1))
    elif i == 2:
        print ('{0} bottles of beer on the wall, {0} bottles of beer. Take one down pass it around, {1} bottle of beer on the wall.'.format(i, i-1))
    else:
        print ('{0} bottle of beer on the wall, {0} bottle of beer. Take one down pass it around, {1} bottles of beer on the wall.'.format(i, i-1))