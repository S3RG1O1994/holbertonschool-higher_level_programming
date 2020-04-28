#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */

int check_cycle(listint_t *list)
{
        listint_t *first_list = list;
        listint_t *second_list = list;

        if (!list->next || !list)
                return(0);

        first_list = first_list->next;
        second_list = second_list->next->next;

        while(first_list && second_list)
        {
                if (first_list == second_list)
                        return(1);
                first_list = first_list->next;
                second_list = second_list->next->next;
                //first_list->next;
        }
}