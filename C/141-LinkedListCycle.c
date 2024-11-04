/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    if(head == NULL || head->next == NULL) return false;
    if(head->next->next == head) return true;

    struct ListNode *slow = head, *fast = head;
    while(fast->next != NULL && fast->next->next != NULL && slow->next != NULL){
        fast = fast->next->next;
        slow = slow->next;
        if(fast == slow){
            return true;
        }
    }
    return false;
}