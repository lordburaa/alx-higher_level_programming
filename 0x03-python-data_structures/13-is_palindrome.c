#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - is planidrome
 * @head: linked list
 * Return: whether is palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}
	if (!dup)
		return (1);
	return (0);
}
/**
 * reverse_listint- reverse linked list
 * @head: pointer to the first item
 * Return: new head of reversed list
 */
void reverse_listint(listint_t **head)
{
	listint_t *next = NULL, *prev = NULL;
	listint_t *current = *head;

	while (current)
	{
		next = current->next;
		current->next = prev;

		prev = current;

		current = next;
	}
	*head = prev;
}
