import random

import numpy as np

level_map_vertical = []
def f(x):
    return int(18+np.sin(x)+np.random.normal(scale=0.2, size=1))
for i in range(1,129):
    x = f(i)

    stringer = ''
    for i in range(1,37):
        if x==i:
            stringer+="X"*(37-i)
            break
        else:stringer+="_"
    #print(stringer)
    level_map_vertical.append(stringer)
#print(level_map_vertical)
#level_map = level_map_vertical

playerspawncoords = random.randint(1,16)
playerspawn = level_map_vertical[playerspawncoords]
spawn_column=playerspawn.split('X',2)
#print("playerspwan ",playerspawn)
playered_line=''
spawn_column[1]='P'
spawn_column[2]+='X'
#print("breh ",spawn_column)
for i in spawn_column:
    playered_line+=i
#print(lengd)
level_map_vertical[playerspawncoords]=playered_line
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
'''

'''
level_map = [
     '                             X',
     '                             X',
     '                             X',
     ' P                           X',
     'XXXX                     XXXXX',
     'XXXXXXXXX           XXXXXXXXXX',
     'XXXXXXX               XXXXXXXX',
     'XXXXXXXXXXXXX   XXXXXXXXXXXXXX',
     'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',]'''

#print(level_map)
tile_size = 10
#screen_width = len(level_map[0])*tile_size
screen_width = 640
screen_height = len(level_map)*tile_size
