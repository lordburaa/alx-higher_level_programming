#include "lists.h"
/**
 * check_cycle - check if it is cylce
 * @list: linked list
 * Return: 0 if no scyle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *p2;
	listint_t *prev;

	p2 = list;
	prev = list;
	while (list && p2 && p2->next)
	{
		list = list->next;
		p2 = p2->next->next;

		if (list == p2)
		{
			list = prev;
			prev = p2;
			while (1)
			{
				p2 = prev;
				while (p2->next != list && p2->next != prev)
				{
					p2 = p2->next;
				}
				if (p2->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}
	return (0);
}
