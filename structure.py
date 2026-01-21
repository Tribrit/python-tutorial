students = []

def display_students():
    if students:
        print("Student Details:")
        for student in students:
            print("ID:", student['id'])
            print("Name:", student['name'])
            print("Marks:", student['marks'])
            print()
    else:
        print("No student details found.")

def add_student():
    student_id = input("Enter student ID: ")
    if any(student['id'] == student_id for student in students):
        print("Student ID already exists.")
    else:
        name = input("Enter student name: ")
        marks = input("Enter student marks: ")
        students.append({'id': student_id, 'name': name, 'marks': marks})
        print("Student added successfully.")

def update_student():
    student_id = input("Enter student ID to update: ")
    for student in students:
        if student['id'] == student_id:
            print("Current details:")
            print("ID:", student['id'])
            print("Name:", student['name'])
            print("Marks:", student['marks'])
            print()
            name = input("Enter new student name (leave blank to keep the current name): ")
            marks = input("Enter new student marks (leave blank to keep the current marks): ")
            if name:
                student['name'] = name
            if marks:
                student['marks'] = marks
            print("Student details updated successfully.")
            break
    else:
        print("Student ID not found.")

def delete_student():
    student_id = input("Enter student ID to delete: ")
    for student in students:
        if student['id'] == student_id:
            students.remove(student)
            print("Student details deleted successfully.")
            break
    else:
        print("Student ID not found.")

# Main menu loop
while True:
    print("\nMenu:")
    print("1. Display student details")
    print("2. Add student")
    print("3. Update student")
    print("4. Delete student")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        display_students()
    elif choice == "2":
        add_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
#In this code, a list called students is used to store the student details. Each student is represented as a dictionary containing the student's ID, name, and marks. 


