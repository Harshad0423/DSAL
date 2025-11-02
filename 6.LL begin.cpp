#include <iostream>
using namespace std;

struct node {
    int data;
    node *next;
};

// Function to create a new node
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
        cout << "List is empty. Nothing to delete.\n\n";
        return head;
    }
    node* temp = head;
    head = head->next;
    delete temp;
    cout << "Node deleted from beginning.\n\n";
    return head;
}

// c. Display the linked list
void display(node* head) {
    if (head == NULL) {
        cout << "List is empty.\n\n";
        return;
    }
    node* temp = head;
    cout << "Linked List: ";
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

    do {
        cout << "1. Insert at Beginning\n";
        cout << "2. Delete from Beginning\n";
        cout << "3. Display Linked List\n";
        cout << "4. Count Number of Elements\n";
        cout << "5. Exit\n";
        cout << "Enter your choice: ";
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

            case 5:
                cout << "Exiting program...\n";
                break;
        }

    } while (choice != 5);

    return 0;
}
