#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

int main(int argc, char* argv[]) {
    if (argc < 3) {
        cout << "Usage: ./body <line_range> <filename>" << endl;
        return 1;
    }
    
    string line_range = argv[1];
    string filename = argv[2];
    
    const string command = "sed -n " + line_range + "p " + filename;
    int result = system(command.c_str());
    
    if (result == 0) {
    	cout << "------------" << endl;
        cout << "Operation Successful" << endl;
    }
    else {
        cout << "Make sure this file exists and is not corrupted" << endl;
    }
    
    return 0;
}

