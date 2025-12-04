/*
Write a program(using fork () and/or exec () commands) where parent and child 
execute: 
same program, different code. 

*/

#include <iostream>
#include <sys/types.h>
#include <unistd.h>
using namespace std;

int main() {
    pid_t pid = fork();

    if (pid<0) {
        cout<<"Error"<<endl;
    } else if(pid==0) {
        cout << "Child Process Continues........ " << endl;
        cout << "Child Process: PID = " << getpid() << endl;
        cout << "Child's Parent Process: PID = " << getppid() << endl;
        cout << "Child's Process Ends" << endl;
    } else {
        cout << "Parent Process Continues........ " << endl;
        cout << "Parent's Process: PID = " << getpid() << endl;
        cout << "Parent's Parent Process: PID = " << getppid() << endl;
        cout << "Parent's Process Ends" << endl;
    }

}