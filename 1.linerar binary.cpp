#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;

struct student {
    int ID;
    char Student_name[50];
    float CGPA;
};

// Function to create student records
void create(student *s, int n) {
    for (int i = 0; i < n; i++) {
        cout << "Enter student details:\n";
        cout << "ID: "; cin >> s[i].ID;
        cout << "Name: "; cin >> s[i].Student_name;
        cout << "CGPA: "; cin >> s[i].CGPA;
        cout << endl;
    }
}

// Function to display student records
void display(student *s, int n) {
    cout << "ID\tName\tCGPA\n";
    for (int i = 0; i < n; i++) {
        cout << s[i].ID << "\t" << s[i].Student_name << "\t" << s[i].CGPA << endl;
    }
    cout << endl;
}

// Linear Search
int linearsearch(student *s, int n) {
    int key;
    cout << "Enter the ID to be searched: ";
    cin >> key;
    for (int i = 0; i < n; i++) {
        if (s[i].ID == key)
            return i;
    }
    return -1;
}

// Bubble Sort by ID (for Binary Search)
void bubblesort(student *s, int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (s[j].ID > s[j + 1].ID) {
                swap(s[j], s[j + 1]);
            }
        }
    }
}

// Binary Search by ID (array must be sorted)
int binarysearch(student *s, int n) {
    int key;
    cout << "Enter the ID to be searched: ";
    cin >> key;
    int low = 0, high = n - 1, mid;
    while (low <= high) {
        mid = (low + high) / 2;
        if (s[mid].ID == key)
            return mid;
        else if (s[mid].ID < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}

int main() {
    student *s = NULL;
    int n = 0, option, loc;

    do {
        cout << "1) Create Student Records\n";
        cout << "2) Display Data\n";
        cout << "3) Linear Search by ID\n";
        cout << "4) Binary Search by ID\n";
        cout << "5) Exit\n";
        cout << "Enter your option: ";
        cin >> option;
        cout << endl;

        switch (option) {
            case 1:
                cout << "Enter number of students: ";
                cin >> n;
                s = (student*)malloc(sizeof(student) * n);
                create(s, n);
                break;

            case 2:
                if (s == NULL || n == 0)
                    cout << "No data available. Please create records first.\n\n";
                else
                    display(s, n);
                break;

            case 3:
                if (s != NULL) {
                    loc = linearsearch(s, n);
                    if (loc != -1) {
                        cout << "Student found:\n";
                        cout << "ID: " << s[loc].ID 
                             << ", Name: " << s[loc].Student_name 
                             << ", CGPA: " << s[loc].CGPA << endl << endl;
                    } else {
                        cout << "Student not found.\n\n";
                    }
                } else {
                    cout << "No records available to search.\n\n";
                }
                break;

            case 4:
                if (s != NULL) {
                    bubblesort(s, n);
                    loc = binarysearch(s, n);
                    if (loc != -1) {
                        cout << "Student found:\n";
                        cout << "ID: " << s[loc].ID 
                             << ", Name: " << s[loc].Student_name 
                             << ", CGPA: " << s[loc].CGPA << endl << endl;
                    } else {
                        cout << "Student not found.\n\n";
                    }
                } else {
                    cout << "No records available to search.\n\n";
                }
                break;

            case 5:
                cout << "Exiting program.\n";
                break;

            default:
                cout << "Invalid option! Try again.\n\n";
        }
    } while (option != 5);

    free(s);
    return 0;
}
