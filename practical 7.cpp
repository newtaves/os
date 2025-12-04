// Write a program to copy files using system calls. 

#include <iostream>
#include <fcntl.h>     // open()
#include <unistd.h>    // read(), write(), close()
#include <cstdlib>     // exit()

using namespace std;

int main() {
    int fd1, fd2;
    char sourceFile[100], destFile[100];
    char buffer[500];
    int bytesRead;

    cout << "Enter source file name: ";
    cin >> sourceFile;

    cout << "Enter destination file name: ";
    cin >> destFile;

    // Open source file in read-only mode
    fd1 = open(sourceFile, O_RDONLY);
    if (fd1 < 0) {
        cout << "Error in opening source file!" << endl;
        exit(1);
    }

    // Create/Open destination file (write-only)
    fd2 = open(destFile, O_CREAT | O_WRONLY | O_TRUNC, 0666);
    if (fd2 < 0) {
        cout << "Error in opening/creating destination file!" << endl;
        close(fd1);
        exit(1);
    }

    // Copy contents
    while ((bytesRead = read(fd1, buffer, sizeof(buffer))) > 0) {
        if (write(fd2, buffer, bytesRead) < 0) {
            cout << "Error writing to destination file!" << endl;
            close(fd1);
            close(fd2);
            exit(1);
        }
    }

    cout << "File copied successfully!" << endl;

    // Close files
    close(fd1);
    close(fd2);

    return 0;
}
