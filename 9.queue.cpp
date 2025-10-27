#include <iostream>
using namespace std;

#define MAX 5  // fixed queue size

class CircularQueue {
private:
    int arr[MAX];
    int front, rear;

public:
    CircularQueue() {
        front = -1;
        rear = -1;
    }

    // Check if queue is full
    bool isFull() {
        return ((rear + 1) % MAX == front);
    }

    // Check if queue is empty
    bool isEmpty() {
        return (front == -1);
    }

    // Enqueue operation
    void enqueue(int val) {
        if (isFull()) {
            cout << "Queue is FULL. Cannot insert " << val << endl;
            return;
        }
        if (isEmpty()) {
            front = 0;
            rear = 0;
        } else {
            rear = (rear + 1) % MAX;
        }
        arr[rear] = val;
        cout << val << " inserted into the queue.\n";
    }

    // Dequeue operation
    void dequeue() {
        if (isEmpty()) {
            cout << "Queue is EMPTY. Cannot delete.\n";
            return;
        }
        int val = arr[front];
        if (front == rear) {
            front = -1;
            rear = -1;  // queue becomes empty
        } else {
            front = (front + 1) % MAX;
        }
        cout << "Deleted element: " << val << endl;
    }

    // Display operation
    void display() {
        if (isEmpty()) {
            cout << "Queue is EMPTY.\n";
            return;
        }
        cout << "Queue elements: ";
        int i = front;
        while (true) {
            cout << arr[i] << " ";
            if (i == rear)
                break;
            i = (i + 1) % MAX;
        }
        cout << endl;
    }
};

// Main Function
int main() {
    CircularQueue q;
    int choice, val;

    while (true) {
        cout << "\n=== Circular Queue Menu ===\n";
        cout << "1. Enqueue (Insert)\n";
        cout << "2. Dequeue (Delete)\n";
        cout << "3. Display\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter value to insert: ";
                cin >> val;
                q.enqueue(val);
                break;

            case 2:
                q.dequeue();
                break;

            case 3:
                q.display();
                break;

            case 4:
                cout << "Exiting...\n";
                return 0;

            default:
                cout << "Invalid choice! Try again.\n";
        }
    }
    return 0;
}
