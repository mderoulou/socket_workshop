/*
** EPITECH PROJECT, 2019
** my_compute_power_it
** File description:
** hello
*/

#include <SFML/Graphics.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "../my.h"
#include "screen.h"

framebuffer_t *draw(void)
{
    static int window_x = 1024;
    static int window_y = 1024;
    static sfSprite* sprite = 0; !sprite ? sprite = sfSprite_create() : 0;
    static sfTexture* texture = 0; !texture ?  texture = sfTexture_create(window_x, window_y) : 0;
    static framebuffer_t *fb = 0 ; !fb ? fb = framebuffer_create(window_x, window_y) : 0;
    static sfVideoMode mode = {1024, 1024, 32};
    static sfRenderWindow *window = 0; !window ? window = sfRenderWindow_create(mode, "pass", sfClose, 0) : 0;

    static char first = 0;
    if (!first){
        sfRenderWindow_setFramerateLimit(window, 60);
        sfSprite_setTexture(sprite, texture, sfTrue);
        first = 1;
    }
    sfTexture_updateFromPixels(texture, fb->pixels, window_x, window_y, 0, 0);
    sfRenderWindow_clear(window, sfBlack);
    sfRenderWindow_drawSprite(window, sprite, 0);
    sfRenderWindow_display(window);
    return (fb);
}
