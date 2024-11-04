/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    if(!head || !head->next) return head;
    
    struct ListNode *temp = head->next, *temp2 = temp->next;
    head->next = NULL;
    while(temp != NULL){
        temp->next = head;
        head = temp;
        temp = temp2;
        if(temp2 != NULL)
            temp2 = temp2->next;
    }
    return head;
}