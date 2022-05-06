#include <iostream>

int failure()
{
    int trevor = 1 + 2 + 5 + 2;
    int peepeepoopoo = 24;
    int tucker = trevor * peepeepoopoo;
    return tucker;
}
int main()
{
    int tucker = failure();
    std::cout << ("%i", tucker);
    return 0;
}