#include<bits/stdc++.h>
using namespace std;

vector <int> v[1000];
bool vis[1000];

void BFS(int src)
{
    vis[src] = true;

    queue <int> q;
    q.push(src);

    while(q.empty() == false)
    {
        int par = q.front();
        q.pop();

        cout << par << " ";

        for(int child : v[par])
        {
            if(vis[child] == false)
            {
                vis[child] = true;
                q.push(child);
            } 
        }
    }
}

// void DFS(int src)
// {
//     vis[src] = true;

//     cout << src << " ";

//     for(int child : v[src])
//     {
//         if(vis[child] == false)
//         {
//             DFS(child);
//         }
//     }
// }

int main()
{
    int n;
    cin >> n;

    int mat[n][n];

    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            cin >> mat[i][j];
        }
    }

    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(mat[i][j] == 1)
            {
                v[i].push_back(j);   
            }
        }
    }

    /*
    


    */

    for(int i=0;i<1000;i++)
    {
        vis[i] = false;
    }

    int src;
    cin >> src;

    DFS(src);



    return 0;
}