#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

const int MAX_THREADS = 5;

typedef struct {
    long tid;
    char name[20];
    unsigned int age;
} tls_t;

static pthread_mutex_t lock;
static pthread_key_t key_tls;
static pthread_once_t once = PTHREAD_ONCE_INIT;

static void make_key(){
    pthread_key_create(&key_tls, NULL);
}

static void * thread_setup_tls(long tid) {
    pthread_once(&once, make_key);
    tls_t *tls;

    tls = pthread_getspecific(key_tls);
    if( tls==NULL ){
        tls = (tls_t *)malloc(sizeof(tls_t));
        pthread_setspecific(key_tls, (void *)tls);
    }
    tls->tid = tid;
    sprintf(tls->name, "thread #%ld", tid);
    tls->age = 100;
    return tls;
}

static void dump_thread_tls(tls_t * tls) {
    pthread_mutex_lock(&lock);

    printf("  Dumping thread TLS %p:\n", tls);
    if(tls!=NULL) {
        printf("    tid  = %ld\n", tls->tid);
        printf("    name = %s\n", tls->name);
        printf("    age  = %d\n", tls->age);
    } else
        printf("    !EMPTY!\n");

    pthread_mutex_unlock(&lock);
}

void* run(void * arg){
    long tid = (long)arg;
    tls_t *tls = NULL;
    printf("  Thread %ld start\n", tid);

    // even threads got their tls
    if (tid%2 == 0) {
        printf("  Thread %ld setting up tls\n", tid);
        tls = thread_setup_tls(tid);
    }
    sleep(1);
    
    tls = pthread_getspecific(key_tls);
    dump_thread_tls(tls);

    printf("  Thread %ld exit\n", tid);
    pthread_exit((void *)tid);
}

int main(){

    printf("Main Thread start\n");

    pthread_t threads[MAX_THREADS];

    int rc;
    int i;
    
    pthread_mutex_init(&lock, NULL);

    pthread_attr_t thread_attr;
    pthread_attr_init(&thread_attr);
    pthread_attr_setdetachstate(&thread_attr, PTHREAD_CREATE_JOINABLE);

    for (i=0; i<MAX_THREADS; i++){
        rc = pthread_create(&threads[i], &thread_attr, run, (void *)(long)i);
        if (rc) {
            printf("Error: pthread_create rc=%d\n", rc);
            exit(-1);
        }
    }

    printf("Thread main: created threads\n");

    void * status;
    for (i=0; i<MAX_THREADS; i++) {
        rc = pthread_join(threads[i], &status);
        if (rc) {
            printf("Error: pthread_join rc=%d\n", rc);
            exit(-1);
        }
        printf("Thread main: joined thread: %ld\n", (long) status);
    }
    
    pthread_attr_destroy(&thread_attr);
    pthread_mutex_destroy(&lock);

    printf("Thread main exit\n");
    pthread_exit(NULL);
}
