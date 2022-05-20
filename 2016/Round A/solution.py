t = int(input())
tc = 0
while t>0:
    n = int(input())
    greatest = -1
    for i in range(0, n):
        name = input()
        count = len(set(name.replace(" ", "")))
        if count > greatest or (count == greatest and name < ans):
            greatest = count
            ans=name
        
    tc+=1
    print ('case #' +str(tc)+': '+str(ans))
    t-=1
