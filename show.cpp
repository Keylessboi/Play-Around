#include <iostream>
#include <cstdlib>
using namespace std;
int main(int argc, char* argv[]) {
    if (argc < 2) {
        cout << "Usage: ./show <filename>" << endl;
        return 1;
    }
    int i = 0;
    string filename = argv[1];
    const string command = "cat " + filename;
    int result = system(command.c_str());
    if (result == 0) {
        cout << "-----------------" << endl;
        cout << "Operation Successful" << endl;
    }
    else {
        cout << "Make sure this file exists and is not corrupted" << endl;
    }
    return 0;
}
