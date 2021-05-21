#include <iostream>

using namespace std;
int main() {
    cout << "Hello World!\n";
    
    int size;
    
    cout<<"Enter Size"<<endl;
    cin>>size;
    
    int arr[size];
    cout<<"Enter Elements"<<endl;

    
    for(int i=0;i<size;i++)
    {
        int data;
        cin>>data;
        arr[i]=data;
    }
    
    cout<<"your array"<<endl;
    for(int j:arr)
    {
        cout<<j<<endl;
    }
    
    
    
    
    
    
    
    
    
    
}