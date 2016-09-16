#include <iostream>
#include <string>
#include <cstring>

using namespace std;

string concat(string  s1, string s2){
    return s1 + " " + s2;
}


int main (){
    string myStr1 = "hello";
    string myStr2 = "world";
    std::cout << myStr1 << " " << myStr2 << endl;
    string myStr;
    //myStr = concat(myStr1, myStr2);
    myStr = concat(myStr1, myStr2);

    
    cout << myStr << endl;

}

