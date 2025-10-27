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

// Linear Search by ID
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

int main() {
    student *s = NULL;
    int n = 0;
    int option, loc;

    do {
        cout << "1) Create Student Records\n";
        cout << "2) Display Data\n";
        cout << "3) Add More Students\n";
        cout << "4) Linear Search by ID\n";
        cout << "5) Exit\n";
        cout << "Enter your option: ";
        cin >> option;
        cout << endl;

        switch (option) {
            case 1: {
                cout << "Enter number of students: ";
                cin >> n;
                s = (student*)malloc(sizeof(student) * n);
                if (s == NULL) {
                    cout << "Memory allocation failed!\n";
                    break;
                }
                create(s, n);
                break;
            }

            case 2:
                if (s == NULL || n == 0)
                    cout << "No data available. Please create records first.\n\n";
                else
                    display(s, n);
                break;

            case 3: {
                if (s == NULL) {
                    cout << "No initial record exists. Please create records first.\n\n";
                    break;
                }
                int more;
                cout << "Enter number of additional students to add: ";
                cin >> more;
                s = (student*)realloc(s, sizeof(student) * (n + more));
                if (s == NULL) {
                    cout << "Memory reallocation failed!\n";
                    break;
                }
                cout << "Enter details of new students:\n";
                create(s + n, more);
                n += more;
                break;
            }

            case 4:
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
        }
    } while (option != 5);

    free(s);
    return 0;
}
