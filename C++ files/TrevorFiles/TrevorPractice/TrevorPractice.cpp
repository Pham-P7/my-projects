#include <iostream>

int birth()
{
    return 4;
}
int x()
{
    int y = 24;
    return y;
}
int failure(int trevor, int peepeepoopoo)
{
    int tucker = trevor * peepeepoopoo;
    return tucker;
}
int main()
{
    int z = x();
    int i = birth();
    int T = failure(i, z);
    std::cout << ("%i", T);
    return 0;
}