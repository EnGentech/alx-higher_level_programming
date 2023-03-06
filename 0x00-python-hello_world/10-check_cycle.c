#include "lists.h"

/**
 * check_cycle - check the existence of a singly list is cycle.
 * @list: points to the beginning of the list
 * Return: 0 if no cycle, else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *lst_p, *chk;

	if (list == NULL || list->next == NULL)
		return (0);
	
	lst_p = list;
	chk = lst_p->next;

	while (lst_p != NULL && chk->next != NULL
		&& chk->next->next != NULL)
	{
		if (lst_p == chk)
			return (1);
		lst_p = lst_p->next;
		chk = chk->next->next;
	}
	return (0);
}
