student_ids = [1001, 1002, 1003, 1004, 1005]
student_names = {
    1001: "MINH DO",
    1002: "VIDHI DESAI",
    1003: "JANE DOE",
    1004: "JOHN SMITH",
    1005: "JOHN WICK"
}
course_in_catalog = {'MATH201', 'ENG102', 'CS101', 'PHYS150', 'DATA210'}
student_grades = {}
while True:
    print("\n===== MENU OPTIONS =====")
    print("Choose a menu option(0-5): \n1. Input & Record Student Grades\n2. Compute GPAs & Academic Averages\n3. Display Formatted Grade Roster\n4. Search Student & Flag Academic Risk\n5. Class Statistics & High/Low Analysis\n0. Exit")
    choice = input("Enter Your Option: ")
#option 1
    if choice == "1":
        student_id_entered = int(input("Enter 4-digit Student ID: "))
        if student_id_entered in student_ids and str(student_id_entered).isdigit() and len(str(student_id_entered)) == 4:
            student_name = input("Enter Student Full Name: ").upper()
            if student_name == student_names[student_id_entered]:
                print(f"Student Name: {student_name}")
                print("Courses in Catalog:", course_in_catalog)
                course = input("Enter course code being recorded: ").upper()
                if course in course_in_catalog:
                    student_grades[student_id_entered] = {course: []}
                    number_of_assignment = input("How many assignment scores to enter? ")
                    if number_of_assignment.isdigit() and int(number_of_assignment) > 0:
                        for i in range(int(number_of_assignment)):
                            student_grade_entered = float(input(f"Enter score #{i + 1} (0-100): "))
                            student_grades[student_id_entered][course].append(student_grade_entered)
                        print(f"[Success] Grades successfully recorded for {student_name} (ID:{student_id_entered})")
                        input("\nPress Enter to return to Main Menu...")
                    else:
                        print("\nInvalid number of assignments. Please enter positive integers.")
                        input("\nPress Enter to return to Main Menu...")
                else:
                    print("\nInvalid course code. Please enter a valid course code from the catalog.")
                    input("\nPress Enter to return to Main Menu...")
            else:
                print("\nInvalid student name. Please enter the correct name for the given ID.")
                input("\nPress Enter to return to Main Menu...")
        elif student_id_entered not in student_ids and str(student_id_entered).isdigit() and len(str(student_id_entered)) == 4:
            new_id_question = input("Student ID not found. Would you like to add a new student? (yes/no): ").strip().lower()
            if new_id_question == "yes" or new_id_question == "y":
                student_id_entered = int(input("Enter new 4-digit Student ID: "))
                student_ids.append(student_id_entered)
                student_names[student_id_entered] = input("Enter Student Full Name: ").upper()
                print(f"New student added: {student_names[student_id_entered]} (ID: {student_ids[-1]})")
                input("\nPress Enter to return to Main Menu...")
            else:
                input("\nPress Enter to return to Main Menu...")

        else:
            print("\nInvalid student ID, must be a 4-digit number.")
            input("\nPress Enter to return to Main Menu...")
#option 2
    elif choice == "2":
        print("You selected option 2.") 
        # Add functionality for option 2 here
    elif choice == "3":
        print("You selected option 3.")
        # Add functionality for option 3 here
    elif choice == "4":
        print("You selected option 4.")
        # Add functionality for option 4 here  
    elif choice == "5":
        print("You selected option 5.")
        # Add functionality for option 5 here
    elif choice == "0":
        print("Exiting the program.")
        break
    else:
        print("The number you entered is not valid. Please enter a number between 0 and 5.")
        input("\nPress Enter to return to Main Menu...")
