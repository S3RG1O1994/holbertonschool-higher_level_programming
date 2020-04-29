#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - Insert node in to linked list
 * @head: pointer at init linked list
 * @number: num added list
 * Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_list = malloc(sizeof(listint_t));
	listint_t *current = *head;

	if (!new_list)
		return (NULL);

	new_list->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new_list->next = *head;
		*head = new_list;
		return (new_list);
	}

	while (current->next)
	{
		if ((current->next)->n >= number)
		{
			new_list->next = current->next;
			current->next = new_list;
			return (new_list);
		}
		current = current->next;
	}

	new_list->next = NULL;
	current->next = new_list;

	return (new_list);
}