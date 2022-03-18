import random


level_map = []
stringer = ''
for i in range(9):
    for j in range(30):
        if i < 3:
            stringer = '                              '
        else:
            landornot = random.randint(0,10)
            if landornot > 5:
                stringer+='X'
            else:
                stringer+=" "
    
    #print(stringer)
    level_map.append(stringer) 
    stringer=''
level_map.append('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print(level_map)

'''level_map = [
     '                             X',
     '                             X',
     '                             X',
     '                             X',
     'XXXX                     XXXXX',
     'XXXXXXXXX           XXXXXXXXXX',
     'XXXXXXX               XXXXXXXX',
     'XXXXXXXXXXXXX   XXXXXXXXXXXXXX',
     'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]'''
print(level_map)
tile_size = 30
screen_width = 900
screen_height = len(level_map)*tile_size
