#include <iostream>
using namespace std;

int main()
{
  int myarray[3] = {9,19,29};

  for (int i=0; i<3; ++i)
    ++myarray[i];

  for (int elem : myarray)
    cout << elem << '\n';
}