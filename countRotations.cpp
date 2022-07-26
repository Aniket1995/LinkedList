#include <bits/stdc++.h>
using namespace std;

struct Node{
    int data;
    Node* next;
};

int countRotations(Node *head){
    
    if(head == NULL) return 0;
    
    int count = 0;
    
    int min = head->data;
    
    while(head != NULL){
        
        if(min > head->data){
            break;
        }
        
        count++;
        
        head = head->next;
        
    }
    
    
    return head == NULL ? 0 : count;
    
}

void push(Node **head, int data){
    
    Node* node = new Node;
    
    node->data = data;
    
    node->next = (*head);
    
    (*head) = node;
    
}

void print(Node* head){
    while(head != NULL){
        cout << head->data << "->";
        head = head->next;
    }
    cout << head << endl;
}

int main(){
    Node * head = NULL;
      
    
    push(&head, 5);
    push(&head, 4);
    push(&head, 3);
    push(&head, 2);
    push(&head, 1);
    
    print(head);
    cout << "rotations: " << countRotations(head) << endl;
    return 0;
}
