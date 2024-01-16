#include <stdlib.h>
#include "lists.h"
/**
 * insert_node: insert a node in a linked list
 * @head: head of list
 * @number: value to be added
 * Return: address or null if fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current = *head;

	if (!new_node)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;
	if (!(*head) || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (current->next && current->next->n < number)
	{
		current = current->next;
	}
	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}
