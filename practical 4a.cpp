/*
Write a program(using fork () and/or exec () commands) where parent and child 
execute: 
i.same program, same code. 

*/

#include <iostream>
#include <sys/types.h>
#include <unistd.h>
using namespace std;


int main() {
    pid_t pid = fork();

    if (pid < 0) {
        cerr << "Fork failed!" << endl;
        return 1;
    } else {
        cout << "Child Process: PID = " << getpid() << endl;
        cout << "Child's Parent Process: PID = " << getppid() << endl;
    }

    return 0;
}