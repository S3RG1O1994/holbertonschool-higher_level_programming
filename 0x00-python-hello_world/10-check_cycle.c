#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - find loops in the linked list
 * @list: pointer to head of list
 * Return: 1 if exists loop or 0 if not exists loop
 */
int check_cycle(listint_t *list)
{
        listint_t *first_list = list;
        listint_t *second_list = list;

        if (!list->next || !list)
                return (0);
        first_list = first_list->next;
        second_list = second_list->next->next;
        while (first_list && second_list && second_list->next)
        {
                if (first_list == second_list)
                        return (1);
                first_list = first_list->next;
                second_list = second_list->next->next;
                second_list->next;
        }
        return (0);
}
