#include "include/my.h"

int my_strcmp_void(void *data)
{
    int *data2 = data;
    return (data2[1] - data2[0]);
}

void main(int ac, char **av)
{
    btr_t *btr = btr_init(2, my_strcmp_void);
    btr_insert(btr, 100);
}
