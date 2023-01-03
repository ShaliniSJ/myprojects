
#include <iostream>
#include <ctime>

using namespace std;
const int maxs = 5;
int stack[maxs] ;
int top = -1;
void push(int num){
    if (top == maxs -1 ){
        printf("overflow");
        return;
    }
    top ++;
    stack[top] = num;
}
void display(){
    if (top == -1)
    printf("stack is empty nothing to show");
    else{
        for (int a = top; a>=0 ;a --){
        cout << stack[a]<<endl;
        }
    } 
}

main(){
    push(10);
    push(11);
    push(12);
    push(13);
    push(14);

    display();
}
