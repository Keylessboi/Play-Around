/* A little example program for Nicholas*/
#include "calc_func.hpp"
#include <iostream>
using namespace std;
int main() {
int equation;
cout << "enter your equation\n";
cin >> equation;
cout << calculate(equation);
}