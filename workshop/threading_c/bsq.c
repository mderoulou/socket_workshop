/*
** EPITECH PROJECT, 2019
** bsq
** File description:
** find bigest square
*/

//#include "my.h"
#include <stdlib.h>
#include <stdio.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <pthread.h>

char *read_files(char *filename)
{
    char buffer[1025];
    char *str;
    int size = 1;
    int total = 0;

    int fd = open(filename, O_RDONLY);
    if (fd == -1)
        return (0);
    for (int size = 1; size != 0;){
        size = read(fd, buffer, 1024);
        total += size;
    }
    close(fd);
    str = malloc(total+1);
    memset(str, 0, total+1);
    fd = open(filename, O_RDONLY);
    read(fd, str, total);
    close(fd);
    return (str);
}

int **split_line_int(char *str)
{
    int nb_line = 0;
    for (int i = 0; str[i]; i++)
        str[i] == '\n' ? nb_line++ : 0;
    int **str_t = malloc((nb_line+1)*sizeof(char *));
    str_t[nb_line] = 0;
    int line_len = 0;
    int line_nb = 0;
    for (int char_nb = 0; str[char_nb]; char_nb++)
        if (str[char_nb] == '\n'){
            str_t[line_nb] = malloc((line_len+1)*sizeof(int));
            str_t[line_nb][line_len] = 0;
            line_len = 0;
            line_nb++;
        } else
            line_len++;
    line_len = 0;
    line_nb = 0;
    for (int char_nb = 0; str[char_nb]; char_nb++)
        if (str[char_nb] == '\n'){
            line_len = 0;
            line_nb++;
        } else {
            str_t[line_nb][line_len] = (str[char_nb] == 'o' ? 1 : 2);
            line_len++;
        }
    return (str_t);
}
char **split_line_char(char *str)
{
    int nb_line = 0;
    for (int i = 0; str[i]; i++)
        str[i] == '\n' ? nb_line++ : 0;
    char **str_t = malloc((nb_line+1)*sizeof(char *));
    str_t[nb_line] = 0;
    int line_len = 0;
    int line_nb = 0;
    for (int char_nb = 0; str[char_nb]; char_nb++)
        if (str[char_nb] == '\n'){
            str_t[line_nb] = malloc((line_len+1)*sizeof(char));
            str_t[line_nb][line_len] = 0;
            line_len = 0;
            line_nb++;
        } else
            line_len++;
    line_len = 0;
    line_nb = 0;
    for (int char_nb = 0; str[char_nb]; char_nb++)
        if (str[char_nb] == '\n'){
            line_len = 0;
            line_nb++;
        } else {
            str_t[line_nb][line_len] = str[char_nb];
            line_len++;
        }
    return (str_t);
}

int *bsq(int **str_t)
{
    int *best = malloc(sizeof(int)*3);
    memset(best, 0, sizeof(int)*3);
    for (int y = 2; str_t[y]; y++){
        for (int x = 1; str_t[y][x]; x++){
            int min = 2147483647;
            if (str_t[y][x] != 1){
                str_t[y-1][x] < min ? min = str_t[y-1][x] : 0;
                str_t[y][x-1] < min ? min = str_t[y][x-1] : 0;
                str_t[y-1][x-1] < min ? min = str_t[y-1][x-1] : 0;
                str_t[y][x] = min + 1;
                min > best[2] ? best[0] = x, best[1] = y, best[2] = min : 0;
            }
        }
    }
    return (best);
}

void *main_bsq(void *file)
{
    printf("str : %s\n", (char*)file);
    int i;
    char *str = read_files((char *)file);
    char **str_t = split_line_char(str);
    int **int_t = split_line_int(str);
    free(str);
    int *best = bsq(int_t);
    for (i = 0; str_t[i] != 0; i++){
        free(int_t[i]);
    }
    free(int_t);
    for (int i = 0; i < best[2]; i++)
        for (int ii = 0; ii < best[2]; ii++)
            str_t[best[1]-ii][best[0]-i] = 'x';
    free(best);
    write(1, "solved\n", 8);
    //for (int i = 1; str_t[i]; i++)
    //    printf("%s\n", str_t[i]);
    for (i = 0; str_t[i] != 0; i++){
        free(str_t[i]);
    }
    free(str_t);
    pthread_exit (0);
    return ((void *)1);
}
