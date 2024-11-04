#include<math.h>
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int getDecimalValue(struct ListNode* head) {
    struct ListNode *temp = head;

    int counter = 0, dec = 0;

    //get digit count
    while(temp != NULL){
        counter++;
        temp = temp->next;
    }
    temp = head;
    while(temp != NULL){
        --counter;
        if(temp->val == 1)
            dec += pow(2,counter);
        temp = temp->next;
    }
    return dec;
}