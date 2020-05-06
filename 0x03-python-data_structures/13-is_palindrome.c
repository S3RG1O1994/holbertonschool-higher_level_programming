#include "lists.h"
/**
 * is_palindrome - check for palindrome in the construction of the linkedlist
 * @head: pointer to linkedlist
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *copy = *head;
	int buff[10240], h = 0, t = 0;

	if (!*head || !((*head)->next))
		return (1);

	while (copy)
	{
		buff[t] = copy->n;
		copy = copy->next;
		t += 1;
	}

	t--;

	while (h <= t / 2)
	{
		if (buff[h] != buff[t - h])
			return (0);
		h++;
	}

	return (1);
}
