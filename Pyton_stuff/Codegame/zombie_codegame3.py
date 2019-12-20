import sys
import math

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
    winner_human = 0
    winer_zombie = 0
    for human in humans:
        for zombie in zombies:
            if distance(human[1],human[2],zombie[1],zombie[2]) < min_dist:
                min_dist=distance(human[1],human[2],zombie[1],zombie[2])
                winner_human = humans.index(human)
                winner_zombie = zombies.index(zombie)
    if distance(x,y,
        dest_point(zombies[winner_zombie][1],humans[winner_human][1],
                                          distance(zombies[winner_zombie][1],zombies[winner_zombie][2],humans[winner_human][1],humans[winner_human][2])),
                                dest_point(zombies[winner_zombie][2],humans[winner_human][2],
                                          distance(zombies[winner_zombie][1],zombies[winner_zombie][2],humans[winner_human][1],humans[winner_human][2]))
                               )>1599:

        try:
            print (dest_point(zombies[winner_zombie][3],humans[winner_human][1],
                                          distance(zombies[winner_zombie][3],zombies[winner_zombie][4],humans[winner_human][1],humans[winner_human][2])),
                                dest_point(zombies[winner_zombie][4],humans[winner_human][2],
                                          distance(zombies[winner_zombie][3],zombies[winner_zombie][4],humans[winner_human][1],humans[winner_human][2])))
        except:
            print (dest_point(zombies[winner_zombie][1],humans[winner_human][1],
                                          distance(zombies[winner_zombie][1],zombies[winner_zombie][2],humans[winner_human][1],humans[winner_human][2])),
                                dest_point(zombies[winner_zombie][2],humans[winner_human][2],
                                          distance(zombies[winner_zombie][1],zombies[winner_zombie][2],humans[winner_human][1],humans[winner_human][2])))
    else:
        print (zombies[winner_zombie][1],zombies[winner_zombie][2])

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # Your destination coordinates
