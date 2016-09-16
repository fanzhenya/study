#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
using namespace std;

inline void swap(char* p, char* q) {
    if (p==q)
        return;
    int t=*p;
    *p=*q;
    *q=t;
}

void qsort(char *a, int left, int right){

    printf("\n");
    //printf("%d, %d\n", left, right);
    for(int i=0; a[i]!='\0'; i++)
        if(i==left && i==right)
            printf("x");
        else if (i==left)
            printf("<");
        else if (i==right)
            printf(">");
        else
            printf(" ");
    printf("\n");

    printf("%s\n", a);
    if(left<right){
        int m=left;
        int p=left;
        int q=right;

        while(p<q){
            while(a[p] <= a[m] && p<right) p++;
            while(a[q] > a[m]) q--;
            if(p<q)
                swap(a+p, a+q);
        }
        swap(a+q, a+m);
        
        qsort(a, left, q-1);
        qsort(a, q+1, right);
    }


}



void qsort4(char a[], int left, int right) {

    if(left<right) {
        printf("%d, %d\n", left, right);
        printf(" sorting: %s\n", a);
        int p=left;
        int q=right;
        int m=right;
        while(p<q) {
            while(a[p] <= a[m] && p<right) p++;
            printf("m pq= %c, %c,%c\n",a[m] ,a[p] ,a[q] );
            while(a[q] > a[m] && q>p) q--;
            printf("m pq= %c, %c,%c\n",a[m] ,a[p] ,a[q] );
            swap(a+p, a+q);
        }
        //if(p!=q) 
            printf("m pq= %c, %c,%c\n",a[m] ,a[p] ,a[q] );
        qsort(a, left, p-1);
        qsort(a, p+1, right);
    }
}

void qsort3(char a[], int left, int right) {
    if(left<right) {
        printf("%d, %d\n", left, right);
        printf(" sorting: %s\n", a);
        char *p=a+left;
        char *m=a+right;
        for(int i=left; i<right; i++)
            if(a[i]<*m) {
                swap(a+i, p);
                p++;
            }
        swap(p, m);
        printf(" sorting: %s\n", a);
        qsort(a, left, p-a-1);
        qsort(a, p-a+1, right);
    }
}
void qsort2(char a[], int left, int right) {
    if(left<right) {
        char *p=a+left;
        char *q=a+right;
        char m=*p;

//        printf("%d, %d\n", left, right);
//        printf(" sorting: %s\n", a);
//        getchar();
        while(p < q) {
            while (p<q) {
                if (*q >= m){
                    q--;
                }
                else {
                    swap(p, q);
                    p++;
                    break;
                }
            }

            while(p<q) {
                if (*p > m){
                    swap(p, q);
                    q--;
                    break;
                }
                else {
                    p++;
                }
            }
        }
       
        //sort left array
        qsort(a, left, p-a-1);
        //sort right array
        qsort(a, q-a+1, right);
    }

}

int main() {
    //string s="yixxvdblxasdfajglkjashewpemnwpxnwzxjwjqnvlcbaeajtncae";
    string s="cebad";
    //string s;
    //cin >> s;
    char *a = new char [s.length()+1];
    strcpy(a, s.c_str());
    printf("unsorted: %s\n", a);

    getchar();
    
    qsort3(a, 0, s.length()-1);
    
    printf("  sorted: %s\n", a);
    for(unsigned int i=0; i<s.length()-1; i++)
        if(a[i] > a[i+1])
            printf("err pos:%d\n", i);


}
