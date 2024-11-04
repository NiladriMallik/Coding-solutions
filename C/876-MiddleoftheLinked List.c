/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    struct ListNode *fast = head, *slow = head;

    if(head->next == NULL) return head;

    if(head->next->next == NULL) return head->next;

    while(1){

        fast = fast->next->next;
        slow = slow->next;
        //for odd number of nodes
        if(fast->next == NULL){
            return slow;
        }
        //for even number of nodes
        if(fast->next != NULL && fast->next->next == NULL){
            return slow->next;
        }
    }
}