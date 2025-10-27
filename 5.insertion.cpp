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

// Insertion Sort by CGPA (Descending)
void insertionSortByCGPA(student *s, int n) {
    for (int i = 1; i < n; i++) {
        student key = s[i];
        int j = i - 1;
        while (j >= 0 && s[j].CGPA < key.CGPA) {  // Descending order
            s[j + 1] = s[j];
            j--;
        }
        s[j + 1] = key;
    }
}

int main() {
    student *s = NULL;
    int n = 0, option;

    do {
        cout << "1) Create Student Records\n";
        cout << "2) Display Data\n";
        cout << "3) Sort by CGPA (Descending)\n";
        cout << "4) Exit\n";
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
                if (s != NULL && n > 0) {
                    insertionSortByCGPA(s, n);
                    cout << "Records sorted by CGPA (Descending):\n";
                    display(s, n);
                } else {
                    cout << "No data available to sort.\n\n";
                }
                break;

            case 4:
                cout << "Exiting program.\n";
                break;
        }
    } while (option != 4);

    free(s);
    return 0;
}
