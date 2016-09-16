#include <iostream>
#include <string>
#include <cctype>
using namespace std;

string concat(string &s1, const string &s2);
void recurDump(const string &s, string::size_type len, string::size_type index);
void recurDump2(string s);

int main () {
    string myStr1 = "Hello~";
    string myStr2 = "World";
    //string inStr;
    //cin >> inStr;
    //cout << "input str is " + inStr << endl;
    cout << myStr1 << myStr2 << endl;
    cout << myStr1 + myStr2 << endl;
    swap(myStr1, myStr2);
    cout << myStr1 + myStr2 + " haha \n" << endl;

    //cout << "lenth is " << (myStr1 + myStr2).length() << endl;
    string &rs1=myStr1;
    const string &rs2=myStr2;
    string tStr= concat(rs1, rs2);
    //tStr.clear();
    cout << "tStr=" << tStr << endl;
    cout << "myStr1, rs1=" << myStr1 << " " << rs1 << endl;
    cout << "capacity, lenth, size: " << tStr.capacity() << " " << tStr.length()<< " " << tStr.size() << endl;
    
    for (string::size_type i=0; i<tStr.length(); i++) {
        tStr[i] = toupper(tStr.at(i));
    }
    cout << tStr << endl;

    cout << "recursively dump string:" ;
    const string &t=tStr;
    //recurDump2("abcd");
    recurDump(t, t.length(), 0);
    cout << endl;
}

void recurDump2(string s){
    unsigned char tail=s.at(s.length());
    if(s.length()>=1){
        s.resize(s.length()-1);
        recurDump2(s);
    }
    cout << tail;
}

// each call prints the tail char of the string
void recurDump(const string &s, string::size_type len, string::size_type index){
    cout << s.at(index);
    if(index < len-1)
        recurDump(s, len, index+1);
}

string concat(string &rs1, const string &rs2){
    rs1="!modifieds1!";
    // rs2="!modifieds2!"; // error!
    return rs1 + rs2;
}
