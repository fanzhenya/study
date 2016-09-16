#include <iostream>
#include <cstdio>

using namespace std;

#define DISPATCH()  { goto *goto_tbl[*(isns++) -'a']; }



static void interp(const char * isns) {
    static void * goto_tbl [] = {
        &&op_nop,   // a
        &&op_nop,   // 
        &&op_nop,   // 
        &&op_nop,   // d
        &&op_e,     // 
        &&op_nop,   // 
        &&op_nop,   // 
        &&op_h,     // h
        &&op_i,     // 
        &&op_nop,   // 
        &&op_nop,   // k
        &&op_nop,   //
        &&op_nop,   // 
        &&op_n,     // 
        &&op_nop,   // o 
        &&op_nop,   // 
        &&op_nop,   // 
        &&op_nop,   // r
        &&op_s,     // 
        &&op_nop,   // 
        &&op_nop,   // u 
        &&op_nop,   //
        &&op_w,     // 
        &&op_nop,   // x
        &&op_nop,   // 
        &&op_nop,   // 
        &&op_nop,   // z
    };

    cout << ">>Interpreter Started!<<\n";
    DISPATCH();
    
op_nop: 
    DISPATCH();

op_h:
    cout << "hello";
    DISPATCH();

op_w:
    cout << "world";
    DISPATCH();

op_i:
    cout << "interpreter";
    DISPATCH();

op_s:
    cout << " ";
    DISPATCH();

op_n:
    cout << endl;
    DISPATCH();

op_e:
    cout << ">>Interpreter Exiting!<<\n";
    return;
}

int main(void){
    interp ("hswsine");
}
