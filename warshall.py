class Graph(object):
    def __init__(self,size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    def addEdge(self,v1,v2):
        if v1==v2:
            print("same vertex %d and %d" %(v1,v2))
            return
        self.adjMatrix[v1][v2]=0

    def removeEdge(self,v1,v2):
        if self.adjMatrix[v1][v2]== 0:
            print("no edge batween %d and %d"%(v1,v2))
            return
        self.adjMatrix

    def containsEdge(self,v1,v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def __len__(self):
        return self.size


    def toString(self):
        for row in self.adjMatrix:
            print(''.join([str(val) for val in row]))

    def get_adjMatrix(self):
        return self.adjMatrix

def main():
        g = Graph(5)
        g.addEdge(0,2);
        g.addEdge(4,0);
        g.addEdge(1,3);
        g.addEdge(3,1);
        g.addEdge(2,4);
        g.addEdge(2,1);
        g.toString()
        S=g.get_adjMatrix();
        path_matrix=warshall(S)
def warshall(A):
    p=[]
    n=len(A)
    p = [[0] * n for i in range(n)]

    for i in range(0,n):
        for j in range(0,n):
            p[i][j] = A[i][j]

    for k in range(0,n):
        for i in range(0,n):
            p[i][j] = p[i][j] or (p[i][k] and p[k][j])
    return p
if __name__ == '__main__':
    main()
