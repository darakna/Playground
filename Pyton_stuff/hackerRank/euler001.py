def fmulti(numb):
    n = numb
    limit3 = int((n-1)/3)
    limit5 = int((n-1)/5)
    limit15 = int((n-1)/15)
    multisum = (limit3 * (limit3+1) / 2 * 3) + (limit5 * (limit5+1) / 2 * 5) - (limit15 * (limit15+1) / 2 * 15)
    print(int(multisum), "{:}".format(multisum))
    print("{:}".format(multisum))
    return(multisum)

n = int(16)
limit3 = int((n-1)/3)
limit5 = int((n-1)/5)
print(limit3, limit5)
multisum = (limit3 * (limit3+1) / 2 * 3) + (limit5 * (limit5+1) / 2 * 5)
print(multisum)
count = 3
m3 = 0
while (count<n):
    m3+=count
    #print(count)
    count+=3
    
count = 5
m5=0
while (count<n):
    m5+=count
    #print(count)
    count+=5
m15=0
count = 15
while (count<n):
    m15+=count
    #print(count)
    count+=15
    
print(m3,m5,m3+m5,m15,m3+m5-m15)
fmulti(n)
