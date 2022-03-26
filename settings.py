import random
import numpy as np

level_map_vertical = []
def f(x):
    return int(18+np.sin(x)+np.random.normal(scale=0.2, size=1))
for i in range(1,64):
    x = f(i)

    stringer = ''
    for i in range(1,37):
        if x==i:
            stringer+="X"*(37-i)
            i+=(37-i)
        else:stringer+="_"
    print(stringer)
    level_map_vertical.append(stringer)
#level_map = level_map_vertical
'''level_map=[]
stringer_horizontal=''
for j in level_map_vertical:
    for k in j:
        stringer_horizontal+=k
print(stringer_horizontal)
level_map.append[(stringer)'''
stringer_new=''
level_map=[]
for i in range(1,36):
    for x in level_map_vertical:
        stringer_new+=x[i]

    level_map.append(stringer_new)
    stringer_new=''






'''
stringer = ''
for i in range(35):
    for j in range(64):
        if i < 12:
            stringer = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        else:
            landornot = random.randint(0,10)
            if landornot > 5:
                stringer+='X'
            else:
                stringer+=" "
    
    #print(stringer)
    level_map.append(stringer) 
    stringer=''
level_map.append('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print(level_map)

level_map = [
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
tile_size = 10
screen_width = 640
screen_height = len(level_map)*tile_size
