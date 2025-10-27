#include <iostream>
#include <string>
using namespace std;

// Node structure for linked list
struct Node {
    char data;
    Node *next;
};

// Stack implemented using linked list
class Stack {
private:
    Node *top;

public:
    Stack() {
        top = NULL;
    }

    bool isEmpty() {
        return top == NULL;
    }

    void push(char x) {
        Node *newNode = new Node();
        newNode->data = x;
        newNode->next = top;
        top = newNode;
    }

    char pop() {
        if (isEmpty()) {
            return '\0';
        }
        Node *temp = top;
        char x = top->data;
        top = top->next;
        delete temp;
        return x;
    }

    char peek() {
        if (isEmpty())
            return '\0';
        return top->data;
    }
};

// Function to return precedence of operators
int precedence(char ch) {
    switch (ch) {
        case '^': return 3;
        case '*':
        case '/': return 2;
        case '+':
        case '-': return 1;
        default: return 0;
    }
}

// Function to check if character is operand
bool isOperand(char ch) {
    return (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') || (isdigit(ch));
}

// Function to convert infix to postfix
string infixToPostfix(string infix) {
    Stack st;
    string postfix = "";

    for (int i = 0; i < infix.length(); i++) {
        char ch = infix[i];

        if (isOperand(ch)) {
            postfix += ch;
        } 
        else if (ch == '(') {
            st.push(ch);
        } 
        else if (ch == ')') {
            while (!st.isEmpty() && st.peek() != '(') {
                postfix += st.pop();
            }
            st.pop(); // remove '('
        } 
        else { // operator
            while (!st.isEmpty() && precedence(st.peek()) >= precedence(ch)) {
                postfix += st.pop();
            }
            st.push(ch);
        }
    }

    // pop remaining operators
    while (!st.isEmpty()) {
        postfix += st.pop();
    }

    return postfix;
}

// Main Function
int main() {
    string infix;
    cout << "Enter Infix Expression: ";
    cin >> infix;

    string postfix = infixToPostfix(infix);
    cout << "\nPostfix Expression: " << postfix << endl;

    return 0;
}
