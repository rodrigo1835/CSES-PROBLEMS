#include<bits/stdc++.h>
using namespace std;
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
 
    vector<int> vet;
    int n,nums,a;
    long long int contador;
    a,contador = 0;
 
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> nums;
        vet.push_back(nums);
    }
    
    for(int j: vet){
        if(j < a){
            while(j < a){
                j++;
                contador++;
            }
 
        }
        a = j;
        
    }
 
    cout << contador;
    return 0;
}
