#include <iostream>
#include <string>
using namespace std;
 void reset(int *i)  // i is just another name for the object passed to reset
 {
 i = 0;  // changes the value of the object to which i refers
 }
int main()
{ int j = 42;
 reset(&j);  // j is passed by reference; the value in j is changed
 cout << "j = " << j  << endl;  // prints j =

 }
