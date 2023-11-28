#include "lists.h"
/**
 * check_cycle - check if it is cylce
 * @list: linked list
 * Return: 0 if no scyle else 1
 */
int check_cycle(listint_t *list)
{
	if (list == NULL)
		return (-1);
	if (list->next == NULL)
		return (0);
	else
		return (1);
}
