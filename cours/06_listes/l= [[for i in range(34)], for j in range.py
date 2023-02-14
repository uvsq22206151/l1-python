l= [[0 for i in range(34)] for j in range(23)]
l[0][0]=1
print(l)

for i in range(15):
    for j in range(19):
        l[2+j][2*i+2]=2

for i in range(15):
    for k in range(8):
        l[2*k+2][2*i+3]=2

def uneEtape():
    for i in range(23):
        for j in range(34):
            if l[i][j]==1:
                if j==33:
                    l[i][j]==0
                elif (i<=1 and l[i][j+1]==0):
                   l[i][j]==0
                   l[i][j+1]==1
                elif(i>1 and l[i-1][j]==0):
                    l[1][j]=0
                    l[1-i][j]=1  

def yaqqn():
    for i in range(23):
        for j in range(34):
            if l[i][j]==1:
                return True
    return False

cpt=0
while yaqqn():
    uneEtape()
    cpt+=1
    print(cpt)                            

