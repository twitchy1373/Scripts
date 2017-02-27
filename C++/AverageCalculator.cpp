#include <iostream>

using namespace std;

int main()
{
		int number;
		int numberTotal = 0;
		int super = 0;
		
		cout << "Enter a number or -1 to quit" << endl;
		cin >>number;
		
		while(number != -1){
			numberTotal = numberTotal + number;
			super++;
			cout << "Enter a number or -1 to quit" << endl;
			cin >> number;
		}
		cout <<"Numbers entered: " << super << endl;
		cout << "Average: " << numbertotal/super;
return 0;	
}
