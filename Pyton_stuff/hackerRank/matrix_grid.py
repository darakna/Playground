def draw_matrix(sample):
    print("Sample output %i" % sample)
    index_y = 0
    for y in range(sample*2 -1):
        index_x = 0
        climb = 0
        q = 0
        max_alt_x = 0
        for x in range(sample*2 - 1):
            if index_y < sample:
                q = 1
                if index_x == index_y:
                    max_alt_x = (sample*2 - 2) - index_x
            else:
                q = 2
                if index_x + index_y == (sample*2 - 2):
                    max_alt_x = index_y

            if index_x == 0:
                climb = 0
            elif index_x <= index_y and q == 1 or index_x + index_y <= (sample*2 - 2) and q == 2:
                climb += 1
            elif index_x > max_alt_x:
                climb -= 1
            #
            #    climb -= 1
            print(sample - climb, end=" ")
            #print(sample - climb, "[[%i,%i],%i,%i,%i]" % (index_y, index_x, max_alt_x,climb, q), end=" ")
            index_x += 1
        index_y += 1
        print("")

draw_matrix(2)
draw_matrix(5)
draw_matrix(7)
draw_matrix(9)
#draw_matrix(11)