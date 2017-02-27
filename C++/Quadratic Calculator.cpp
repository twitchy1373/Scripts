#include <iostream>
#include <complex>
#include <cmath>
#include <math.h>
//#include <fstream>


using namespace std;

		
int main()
{
	//ifstream roottable("SQUAREROOTTABLE.ods");
	
    std::complex<double> a;
    std::complex<double> b;
    std::complex<double> c;
     std::complex<double> p;
    std::complex<double> n;
				//double root;
				//double value;
   
    while(cin){
    cout << "Enter your A value \n";
    cin >> a;
    cout << "Enter your B value \n";
    cin >> b;
    cout << "Enter your C value \n";
    cin >> c;

    std::complex<double> x = sqrt(pow(b,2)- 4.0*a*c);
    std::cout << "The answers are "
    
    << (-b + x)/(2.0*a)<<"i" <<endl;
		
		
		
	cout << "and " << (-b - x)/(2.0*a)<<"i" <<endl;
       
       p =(-b + x)/(2.0*a);
       
       n = (-b - x)/(2.0*a);
   
       
       
		/*while(roottable >> root >> value){
		    
		    p =(-b + x)/(2.0*a);
       
			n = (-b - x)/(2.0*a);
			
			 
		   if(p == value){
		   cout << "the root is " << root << endl;
		   
	   }
		   
		   if(n == value ){
			   cout << root << endl;
		   }*/
		   
	
    }         
  return 0;            
}
//}
