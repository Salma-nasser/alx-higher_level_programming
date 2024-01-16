#include <stdlib.h>
#include "lists.h"
/**
 *check_cycle: check a linked list for cycles
 *@list: head pointer to the list
 *Return: 0 for no cycles 1 if it has cycle
 */
int check_cycle(listint_t *list)
{
	struct listint_s *slow = list;
	struct listint_s *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
