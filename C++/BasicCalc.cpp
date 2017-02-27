#include <iostream>

using namespace std;

int main()
{
	int a;
	int b;
	int c;
	int sum;
	int difference;
	int product;
	int quotient;
	int remainder;
	
			while(cin){
	cout << "Enter a Number \n";
	cin >> a;
	cout<< "Enter another number \n";
	cin >> b;
	cout<<"Enter the number of the opperation you wish to perform \n add(1), subtract(2), multiply(3), or divide(4) \n";
	cin >> c;
	
	sum = a + b;
	difference = a - b;
	product = a * b;
	quotient = a / b;
	remainder = a % b;
	
	switch(c){
	case 1:
	cout << "the sum of the numbers is " << sum << endl;
	break;
	
	case 2:
	cout << "the difference of the numbers is " << difference << endl;
	break;
	
	case 3:
	cout << "the product of the numbers is " << product << endl;
	break;
	
	case 4:
	cout << "the quotient of the numbers is " << quotient 
	<< " with a remainder of " << remainder << endl;
	break;
	}
}
	return 0;
}
