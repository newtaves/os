/*
Write a program to report behaviour of Linux kernel including information on 
configured memory, amount of free and used memory. (Memory information) 

*/

#include <iostream>
#include <sys/utsname.h>
#include <sys/sysinfo.h>
using namespace std;


int main(){
    struct sysinfo s1;
    int i = sysinfo(&s1);
    if (i==0) {
        cout<<"Total RAM: "<<s1.totalram<<endl;
        cout<<"Availablle RAM: "<<s1.freeram<<endl;
        cout<<"Used RAM: "<<s1.totalram-s1.freeram<<endl;
    } else 
        cout<<"Error:"<<endl;
    
    
    return 0;
}