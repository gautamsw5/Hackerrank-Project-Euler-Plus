#include<bits/stdc++.h>
using namespace std;
int main()
{
    int N = 1000001;
    vector<int> tot;
    vector<int> arr;
    tot.assign(N, 0);
    arr.assign(N, 0);
    int i = 2;
    while(i*i<N-2*i)
    {
        int j = i+2;
        while(i*j < N)
        {
            tot[i*j]++;
            j += 2;
        }
        i+=2;
    }
    for(int i=1; i<N; i++)
    {
        arr[i] = arr[i-1];
        if(0<tot[i] && tot[i]<11)
            arr[i]++;
    }
    int t,x;
    cin>>t;
    for(int xyz=0; xyz<t; xyz++)
    {
        cin>>x;
        cout<<arr[x]<<endl;
    }
    return 0;
}
