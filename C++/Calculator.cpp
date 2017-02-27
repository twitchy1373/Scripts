#include <iostream>
#include <complex>
#include <cmath>
#include <math.h>


using namespace std;

		int Quadratic();
		
		int Basic();
		
		int Average();
int main()
{
	int selector;
		while (cin){
	cout << ("Welcome to the Calculator Program \n");
	cout << ("Please press 1 for a Basic Calculator \n"); 
	cout << ("Please press 2 for a Quadratic Calculator \n");
	cout << ("Please press 3 for an Average Calculator \n");
	cin >> (selector);
	
		
		
		switch(selector){
			
		case 1:
			Basic();
			break;
			
		case 2:
			Quadratic();
			break;
			
		case 3:
			Average();
			break;	
			
			
		default: cout << "Invalid input" << endl;	
		}
	
	}


return 0;
}

	int Quadratic()
	{
		
		
	std::complex<double> a;
    std::complex<double> b;
    std::complex<double> c;
    
				
   
    
    cout << "Enter your A value \n";
    cin >> a;
    cout << "Enter your B value \n";
    cin >> b;
    cout << "Enter your C value \n";
    cin >> c;

    std::complex<double> x = sqrt(pow(b,2)- 4.0*a*c);
    
    std::cout << "The answers are "
    
    << (-b + x)/(2.0*a)<<"i" <<endl;
		
		
		
	cout << "and " << (-b - x)/(2.0*a)<<"i \n" <<endl;
       

     
     return 0;
 }
		
		int Basic()
		{
			
	double a;
	double b;
	int c;
	double sum;
	double difference;
	double product;
	double quotient;
	
	
			
	cout << "Enter a Number \n";
	cin >> a;
	cout<< "Enter another number \n";
	cin >> b;
	cout<<"Enter the number of the opperation you wish to perform \n add(1)"
	", subtract(2), multiply(3), or divide(4) \n";
	cin >> c;
	
	sum = a + b;
	difference = a - b;
	product = a * b;
	quotient = a / b;
	
	
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
	cout << "the quotient of the numbers is " << quotient << endl;
	break;
	
	default: cout << "Invalid input" << endl;
}
	return 0;

}
	int Average()
{
		int number;
		int numbertotal = 0;
		int super = 0;
			
			
		cout << "Enter a number or -1 to quit" << endl;
		cin >>number;
		
		while(number != -1){
			numbertotal = numbertotal + number;
			super++;
			cout << "Enter a number or -1 to quit" << endl;
			cin >> number;
		}
		cout <<"Numbers entered: \n" << super << endl;
		cout << "Average:  \n" << numbertotal/super;
		
return 0;	
}

