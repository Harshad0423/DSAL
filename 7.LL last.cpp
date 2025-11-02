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

// a. Insert at Last
node* insert_at_last(node* head, int data) {
    node* newnode = create_node(data);
    if (head == NULL) {
        head = newnode;
    } else {
        node* temp = head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newnode;
    }
    cout << "Node inserted at the end.\n\n";
    return head;
}

// b. Delete from Last
node* delete_from_last(node* head) {
    if (head == NULL) {
        cout << "List is empty. Nothing to delete.\n\n";
        return NULL;
    }
    if (head->next == NULL) {
        cout << "Deleted node with data: " << head->data << "\n\n";
        delete head;
        return NULL;
    }
    node* temp = head;
    while (temp->next->next != NULL) {
        temp = temp->next;
    }
    cout << "Deleted node with data: " << temp->next->data << "\n\n";
    delete temp->next;
    temp->next = NULL;
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

// d. Search element in linked list
void search(node* head, int key) {
    node* temp = head;
    int pos = 1;
    while (temp != NULL) {
        if (temp->data == key) {
            cout << "Element " << key << " found at position " << pos << ".\n\n";
            return;
        }
        temp = temp->next;
        pos++;
    }
    cout << "Element " << key << " not found in the list.\n\n";
}

// Main function
int main() {
    node* head = NULL;
    int choice, data;

    do {
        cout << "1. Insert at Last\n";
        cout << "2. Delete from Last\n";
        cout << "3. Display Linked List\n";
        cout << "4. Search Element\n";
        cout << "5. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;
        cout << endl;

        switch (choice) {
            case 1:
                cout << "Enter data to insert: ";
                cin >> data;
                head = insert_at_last(head, data);
                break;

            case 2:
                head = delete_from_last(head);
                break;

            case 3:
                display(head);
                break;

            case 4:
                cout << "Enter element to search: ";
                cin >> data;
                search(head, data);
                break;

            case 5:
                cout << "Exiting program...\n";
                break;
        }

    } while (choice != 5);

    return 0;
}
