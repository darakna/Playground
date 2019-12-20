import sys
import math
#0 < x < 16000
#0 < y < 9000
# Save humans, destroy zombies!
def modul(nbr):
    if nbr >= 0:
        return nbr
    else:
        return -1*nbr
def distance(x1,y1,x2,y2):
    return float("%.2f" % (((x1-x2)**2)+((y1-y2)**2))**(1/2))
def dest_point(x1,x2,dist):
    if x1<x2: return int(x1+(modul(x1-x2)*modul(dist-(dist%400)))/dist)
    else: return int(x1-(modul(x1-x2)*modul(dist-(dist%400)))/dist)
# game loop
while 1:
    zombies = []
    humans = []
    x, y = [int(i) for i in input().split()]
    human_count = int(input())
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        humans.append([human_id,human_x,human_y])
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        zombies.append([zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext])
    min_dist=distance(0,0,16000,9000)
    closest_zmb = 1
    zmb_dist = []
    for j in humans:
        zmb_hum_dist = []
        for i in zombies:
            zmb_hum_dist.append(distance(j[1],j[2],i[1],i[2]))
        zmb_dist.append(zmb_hum_dist)
    zmb_hmn_pair = []
    for zmb in zmb_dist:
        zmb_hmn_pair.append([zmb.index(min(zmb)),min(zmb)])
    for zmb in zmb_hmn_pair:
        if min_dist>zmb[1]:
            closest_zmb = zmb[0]
            min_dist = zmb[1]
    #print(closest_zmb)
    #print(zmb_hmn_pair)
    #print(zmb_hmn_pair[closest_zmb])
    #print(humans)
    #print(humans[zmb_hmn_pair[closest_zmb][0]])
    #print(humans[zmb_hmn_pair[closest_zmb][0]][1])
    #print(zmb_hmn_pair[closest_zmb][1])
    print(dest_point(zombies[closest_zmb][1],humans[zmb_hmn_pair[closest_zmb][0]][1],zmb_hmn_pair[closest_zmb][1]),dest_point(zombies[closest_zmb][2],humans[zmb_hmn_pair[closest_zmb][0]][2],zmb_hmn_pair[closest_zmb][1]))



    #print(zmb_dist,zmb_hmn_pair)



            #zmb_dist.append([i[0],distance(x,y,i[1],i[2]),distance(x,y,i[3],i[4])])


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # Your destination coordinates
    #print("0 0")