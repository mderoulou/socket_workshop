#include <pthread.h>
#include <stdio.h>

void *main_bsq(void *file);

void main_bsq_thread(char *file)
{
    main_bsq(file);
    pthread_exit (0);
}

int main(int ac, char **av)
{
    int thread_nb = 16;

    if (ac != 2) printf("bad argument\n");

    void *(*bsq_f)(void *);
    bsq_f = main_bsq;



    pthread_t *thread_tab = malloc(sizeof(void *) * (thread_nb + 1));
    thread_tab[thread_nb] = 0;
    for (int i = 0; i < thread_nb; i++)
        if (pthread_create(&thread_tab[i], 0, bsq_f, av[1]))
            printf("fail to make thread\n");

    for (int i = 0; thread_tab[i]; i++)
        pthread_join (thread_tab[i], 0);
    return (1);
}

/*
void pthread_exit (void * retval);
//destroy thread

int pthread_cancel (pthread_t thread);
annuler un thread à partir d'un autre à n'importe quel moment avec la fonction :

int pthread_join (pthread_t th, void ** thread_return);
wait a thread

//create a thread
int pthread_create (pthread_t * thread, pthread_attr_t * attr, void * (* start_routine) (void *), void * arg);
*/
