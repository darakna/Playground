__author__ = 'darakna'
# Homework 2, Problem 1  slicing and indexing challenges

pi = [3,1,4,1,5,9]
e = [2,7,1]
# Example problem (problem 0):  Creating the list [2,5,9] from pi and e
answer0 = [ e[0] ] + pi[-2:]
answer1 = e[1:2]+pi[1:2]
answer2 = [pi[-1],pi[1],pi[1]]
answer3 = pi[1:]
answer4 = sorted(pi+e)[2:7]
print (answer0)
print(e[1:2]+pi[1:2])
# starting strings for Homework 1
h = 'harvey'
m = 'mudd'
c = 'college'
answer5=h[0]+h[-2]+h[-1]*2+c[1]+m[1]
answer6=c[:4]+m[1:3]+c[-1]
answer7=h[1:]+m[1:]
answer8=h[:3]+m[-1]+c[-1]+h[:3]*3
answer81=h[:3]*4
answer82=answer81[:3]+m[-1]+c[-1]+answer81[3:]
answer9=c[3:6]+c[1]+m[0]+h[-1]
answer91=answer9+answer9[1:4]
answer10=c[0]+c[3:5]+h[1:3]+c[0]+h[1]+c[2:4]