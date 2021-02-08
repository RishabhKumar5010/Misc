#include <iostream>

using namespace std;


int main()
{

int arr[] = {2,7,4,9,11,10,8,12,10,5,10}; 
int size = 11;

int k = 6;
int kmax;
int max;
for (int i=0;i<k;)
{
	max = 0;
	for (int j =0; j<size; j++)
		{
		if (i!=0)
		{
			if (arr[j]>max && arr[j]<kmax)
				max = arr[j];
		}
		else if(arr[j]>max)
			{
			max = arr[j];
			}
		}
	kmax = max;
	for(int m =0;m<size;m++)
	    if(arr[m]==kmax)
	        i++;
}
cout<<"\n\nThe "<<k<<"th largest element is : "<<kmax<<"\n\n";

return 0;
}
