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

// Selection Sort by CGPA (Ascending)
void selectionSortByCGPA(student *s, int n) {
    for (int i = 0; i < n - 1; i++) {
        int min = i;
        for (int j = i + 1; j < n; j++) {
            if (s[j].CGPA < s[min].CGPA)
                min = j;
        }
        if (min != i)
            swap(s[i], s[min]);
    }
}

int main() {
    student *s = NULL;
    int n = 0, option;

    do {
        cout << "1) Create Student Records\n";
        cout << "2) Display Data\n";
        cout << "3) Sort by CGPA (Ascending)\n";
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
                    selectionSortByCGPA(s, n);
                    cout << "Records sorted by CGPA (Ascending):\n";
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
