#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int a[] = {28777, 25455, 17236, 18043, 12598, 24418, 26996, 29535, 26990, 29556, 13108, 25695, 28518, 24376, 24368, 13411, 12343, 13872, 25725};
    for(int i = 0; i < 19; i++)
    {
        for(int j = 0; j <= 126; j++)
        {
            if((a[i]-(j<<8)) <= 126 && (a[i]-(j<<8)) >=0)
            {
                cout << char(j) << char(a[i]-(j<<8));
            }
        }
    }
}