#include <iostream>
using namespace std;

struct node {
    int data;
    node *next;
};

// Create a new node
node* create_node(int data) {
    node* newnode = new node();
    newnode->data = data;
    newnode->next = NULL;
    return newnode;
}

// a. Insert at beginning
node* insert_at_begin(node* head, int data) {
    node* newnode = create_node(data);
    newnode->next = head;
    head = newnode;
    return head;
}

// b. Delete from beginning
node* delete_from_begin(node* head) {
    if (head == NULL) {
        return head;
    }
    node* temp = head;
    head = head->next;
    delete temp;
    return head;
}

// c. Display the linked list
void display(node* head) {
    if (head == NULL) {
        cout << "List is empty.\n\n";
        return;
    }
    node* temp = head;
    while (temp != NULL) {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << "NULL\n\n";
}

// d. Count the number of elements
int count_nodes(node* head) {
    int count = 0;
    node* temp = head;
    while (temp != NULL) {
        count++;
        temp = temp->next;
    }
    return count;
}

// Main function
int main() {
    node* head = NULL;
    int choice, data;

        cout <<"1. Insert at Beginning\n";
        cout <<"2. Delete from Beginning\n";
        cout <<"3. Display Linked List\n";
        cout <<"4. Count Number of Elements\n";
        cout <<"Enter your choice: ";
        cin >> choice;
        cout << endl;

        switch (choice) {
            case 1:
                cout << "Enter data to insert: ";
                cin >> data;
                head = insert_at_begin(head, data);
                break;

            case 2:
                head = delete_from_begin(head);
                break;

            case 3:
                display(head);
                break;

            case 4:
                cout << "Total nodes in Linked List: " << count_nodes(head) << "\n\n";
                break;
        }

    return 0;
}
