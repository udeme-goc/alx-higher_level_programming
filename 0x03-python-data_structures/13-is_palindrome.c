#include <stddef.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the first node of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev_slow = *head;
    listint_t *second_half, *midnode = NULL;
    int is_palindrome = 1;

    if (*head != NULL && (*head)->next != NULL)
    {
        /* Get the middle of the list */
        while (fast != NULL && fast->next != NULL)
        {
            fast = fast->next->next;
            prev_slow = slow;
            slow = slow->next;
        }

        /* Odd length, move midnode to the next node */
        if (fast != NULL)
        {
            midnode = slow;
            slow = slow->next;
        }

        /* Reverse the second half and compare */
        second_half = slow;
        prev_slow->next = NULL;
        reverse_list(&second_half);
        is_palindrome = compare_lists(*head, second_half);

        /* Revert changes made to second_half */
        reverse_list(&second_half);

        if (midnode != NULL)
        {
            prev_slow->next = midnode;
            midnode->next = second_half;
        }
        else
        {
            prev_slow->next = second_half;
        }
    }

    return (is_palindrome);
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to pointer of the first node of the list
 */

void reverse_list(listint_t **head)
{
    listint_t *prev = NULL, *current = *head, *next;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}

/**
 * compare_lists - compares two linked lists
 * @list1: pointer to the first linked list
 * @list2: pointer to the second linked list
 * Return: 1 if the lists are equal, 0 if they are not
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
    while (list1 != NULL && list2 != NULL)
    {
        if (list1->n != list2->n)
            return (0);

        list1 = list1->next;
        list2 = list2->next;
    }

    if (list1 == NULL && list2 == NULL)
        return (1);

    return (0);
}

