#include <iostream>

using namespace std;

static void interp(const char * isns) {
    cout << ">>Interpreter Started!<<\n";
    while(1){
        switch(*(isns++)){
            case 'h':
                cout << "hello";
                break;

            case 'w':
                cout << "world";
                break;

            case 's':
                cout << " ";
                break;

            case 'n':
                cout << endl;
                break;

            case 'e':
                cout << "\n>>Interpreter Exiting!<<\n";
                return;

            default:
                 cout << "Unkonwn instruction: ";
                break;
            
        }
    }

}

int main(void){
    interp ("hswne");
}
