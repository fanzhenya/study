#include <stdio.h>
#include <pthread.h>

__thread long tls;

void * thread_run(void * arg){
    long tid=(long)arg;
    tls = tid * 100 + tid*10 + tid;
    printf("Thread %ld has tls = %ld\n", tid, tls);
}
void main(){
    pthread_t threads[4];
    int i;
    
    for(i=0; i<4; i++) {
        pthread_create(&threads[i], NULL, thread_run, (void *)i);
    }
    
    for(i=0; i<4; i++) {
        pthread_join(threads[i], NULL);
    }

    thread_run(9);
    pthread_exit(NULL);

}
