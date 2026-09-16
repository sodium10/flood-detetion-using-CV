#include<bits/stdc++.h>
#define NULL_VALUE -999999
#define INF 999999

using namespace std;

//******************Graph class starts here**************************
class Graph
{
	int nVertices, nEdges ;
	bool directed ;
	//int **matrix ;//adjacency matrix to store the graph
	int *matrix[101];

public:
	Graph(bool dir){
	    nVertices = 0 ;
        nEdges = 0 ;
        //matrix = 0 ;
        directed = dir ;
	}

	void setnVertices(int n){
	    nVertices = n ;
        //allocate space for the matrix

        for(int i=0;i<nVertices;i++){
            matrix[i]=(int*) malloc(nVertices*sizeof(int));
            for(int j=0;j<nVertices;j++){
                matrix[i][j]=0;
            }
        }
	}

	void addEdge(int u, int v){
	    if(u<0 || u>=nVertices || v<0 || v>=nVertices) return;
        matrix[u][v] = 1;
        nEdges++;
        if(!directed) matrix[v][u] = 1;
	}

	void removeEdge(int u, int v){
	    if(u<0 || u>=nVertices || v<0 || v>=nVertices) return;
        matrix[u][v] = 0;
        if(!directed) matrix[v][u] = 0;
	}

    void printGraph(){
        printf("\nNumber of vertices: %d, Number of edges: %d\n", nVertices, nEdges);
        for(int i=0;i<nVertices;i++)
        {
            for(int j=0; j<nVertices;j++)
            {
                printf("%d ", matrix[i][j]);
            }
            printf("\n");
        }
    }

    ///Write your defined function here

    ~Graph(){
	    //delete[] matrix ;
	    for(int i=0;i<nVertices;i++){
            free(matrix[i]);
	    }
	}
};

//**********************Graph class ends here******************************


//******main function to test your code*************************
int main(void)
{
    int n;
    bool dir=false;
    Graph g(dir);

    g.setnVertices(5);

    g.addEdge(0,1);
    g.addEdge(0,2);
    g.addEdge(1,2);
    g.addEdge(1,3);
    g.addEdge(2,4);
    g.addEdge(3,4);

    g.printGraph();

    ///Call your defined function here using g.

    return 0;
}
