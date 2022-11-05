X=[[1,2,3],
   [4,5,6],
   [7,8,9]]
Y=[[9,8,7],
   [6,5,4],
   [3,2,1]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

def add55():
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j]=X[i][j]+Y[i][j]

    for r in result:
        print(r)


def multiply55():
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j]+=X[i][k]*Y[k][j]
    for r in result:
        print(r)



def transpose55():
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[j][i]=X[i][j]
    for r in result:
        print(r)
add55()
multiply55()
transpose55()