"""
================================================================
Course: CSCE 1030
Assignment: Project 1 - Student Grade Management System
Lab Section: CSCE 1030.341
Team Members:
1. Vidhi Desai (EUID: vd0583) - Submitter
2. Minh DO (EUID: mtd0129)
Contribution Overview:
- Vidhi Desai : Designed overall data structures and implemented options 0, and 2-5
- Minh Do: Implemented option 1 and tested program
Github For Version Control: https://github.com/VidhiVD/CS1030Project1
================================================================
"""
student_ids = [1001, 1002, 1003, 1004, 1005]
student_names = ["Alex Mercer", "Jordan Lee", "Taylor Smith", "Morgan Grimes", "Casey Jones"]
student_grades = {
    1001: [88.5, 92.0, 79.0, 95.5],
    1002: [72.0, 68.5, 74.0, 81.0],
    1003: [95.0, 98.0, 91.5, 94.0],
    1004: [55.0, 62.0, 48.0, 59.5],
    1005: [84.0, 87.5, 89.0, 82.0]
}
student_gpas = {
    1001: 3.0,
    1002: 1.0,
    1003: 4.0,
    1004: 0.0,
    1005: 3.0
}
enrolled_courses = {"CS101", "MATH201", "ENG102", "CSCE1030"}

GRADE_BOUNDARIES = (90.0, 80.0, 70.0, 60.0)
GRADE_LETTERS = ('A', 'B', 'C', 'D', 'F')
system_active = True

while system_active:
    # Render Main Menu Console
    print("\n" + "=" * 50)
    print("      ACADEMIC RECORD MANAGEMENT SYSTEM (ARMS)      ")
    print("=" * 50)
    print(" [1] Input & Record Student Grades")
    print(" [2] Compute GPAs & Academic Averages")
    print(" [3] Display Formatted Grade Roster")
    print(" [4] Search Student & Flag Academic Risk")
    print(" [5] Class Statistics & High/Low Analysis")
    print(" [0] Exit Portal")
    print("-" * 50)
    
    choice = input("Enter your selection (0-5): ").strip()
    print("-" * 50)
    
#Option 1 
    if choice == '1':
        raw_id = input("Enter 4-digit Student ID: ").strip()
        if not raw_id.isdigit() or len(raw_id) != 4:
            print("[ERROR] Invalid Student ID. Must be exactly 4 digits.")
        else:
            sid = int(raw_id)
            
            name = input("Enter student's full name: ").strip()
            course = input("Enter course code: ").strip().upper()
            enrolled_courses.add(course)
            
            raw_count = input("How many assignment scores will be entered? ").strip()
            if not raw_count.isdigit() or int(raw_count) <= 0:
                print("[ERROR] Invalid count. Returning to menu.")
            else:
                num_scores = int(raw_count)
                temp_scores = []
                valid_scores = True
                
                for i in range(num_scores):
                    try:
                        score_input = float(input(f"  Enter score #{i+1} (0.0 - 100.0): "))
                        if 0.0 <= score_input <= 100.0:
                            temp_scores.append(score_input)
                        else:
                            print("[ERROR] Score out of bounds. Aborting entry.")
                            valid_scores = False
                            break
                    except ValueError:
                        print("[ERROR] Score must be a numerical value. Aborting.")
                        valid_scores = False
                        break
                
                if valid_scores:
                    if sid not in student_ids:
                        student_ids.append(sid)
                        student_names.append(name)
                    else:
                        idx = student_ids.index(sid)
                        student_names[idx] = name
                    
                    student_grades[sid] = temp_scores
                    print(f"\n[SUCCESS] Records updated for {name} (ID: {sid}).")
                    
        input("\nPress Enter to return to Main Menu...")
#Option 2 
    elif choice == '2':
        if not student_grades:
            print("[NOTICE] System contains no student grade records.")
        else:
            print(f"{'STUDENT ID':<12} | {'AVG SCORE':<10} | {'LETTER':<8} | {'GPA':<5}")
            print("-" * 45)
            
            for sid, grades_list in student_grades.items():
                if len(grades_list) == 0:
                    avg_score = 0.0
                else:
                    avg_score = sum(grades_list) / len(grades_list)
                
                if avg_score >= 90.0:
                    gpa = 4.0
                elif avg_score >= 80.0:
                    gpa = 3.0
                elif avg_score >= 70.0:
                    gpa = 2.0
                elif avg_score >= 60.0:
                    gpa = 1.0
                else:
                    gpa = 0.0
                
                letter_grade = 'F' 
                for index, boundary in enumerate(GRADE_BOUNDARIES):
                    if avg_score >= boundary:
                        letter_grade = GRADE_LETTERS[index]
                        break
                
                student_gpas[sid] = gpa
                print(f"ID: {sid} | Avg Score: {avg_score:.1f}% | Letter: {letter_grade} | GPA: {gpa:.1f}")
                
            print("\n[SUCCESS]")
            
        input("\nPress Enter to return to Main Menu...")

#Option 3 Code
    elif choice == '3':
        border_char = input("Enter a single border character (or hit Enter for default '*'): ").strip()
        if len(border_char) != 1:
            border_char = '*'
            
       
        print(border_char * 67)
        header_text = " INSTITUTIONAL ACADEMIC ROSTER "
        print(f"{header_text:{border_char}^67}")
        print(border_char * 67)
        
        
        print(f"{'#':<4} | {'ID':<6} | {'NAME':<18} | {'GPA':<5} | {'STATUS':<15}")
        print("-" * 67)
        
       
        for index, sid in enumerate(student_ids):
            name = student_names[index]
            gpa = student_gpas.get(sid, 0.0)
            
            if gpa >= 3.5:
                status = "Dean's List"
            elif gpa >= 2.0:
                status = "Good Standing"
            else:
                status = "Probation Risk"
                
            student_tuple = (index + 1, sid, name, gpa, status)
            print(f"{student_tuple[0]:<4} | {student_tuple[1]:<6} | {student_tuple[2]:<18} | {student_tuple[3]:<5.1f} | {student_tuple[4]:<15}")
            
        print(border_char * 67)
        
        input("\nPress Enter to return to Main Menu...")

    #Option 4 
    elif choice == '4':
        search_input = input("Enter Student ID to search: ").strip()
        if not search_input.isdigit():
            print("[ERROR] ID lookup must be numeric.")
        else:
            target_id = int(search_input)
            found = False
            
            for i in range(len(student_ids)):
                if student_ids[i] == target_id:
                    found = True
                    
                    name = student_names[i]
                    grades_list = student_grades.get(target_id, [])
                    gpa = student_gpas.get(target_id, 0.0)
                    
                    print(f"\nProfile Found for Student: {name}")
                    print(f"  - Student ID: {target_id}")
                    print(f"  - Current Score Registry: {grades_list}")
                    print(f"  - Established System GPA: {gpa:.1f}")
                    
                    if gpa < 2.0:
                        print("  - [AT RISK] Student is on Academic Probation.")
                    elif gpa >= 3.5:
                        print("  - [EXCELLENT] Student made Honor Roll.")
                    else:
                        print("  - [NORMAL] Student is in Good Standing.")
                    break
            
            if not found:
                print(f"[NOTICE] Student ID {target_id} not found in system records.")
                
        input("\nPress Enter to return to Main Menu...")
    elif choice == '5':
        all_scores = []
        for sid, grades_list in student_grades.items():
            for score in grades_list:
                all_scores.append(score)
        if len(all_scores) == 0:
            print("[NOTICE] No scores registered in the system to calculate metrics.")
        else:
            total_grades = len(all_scores)
            highest_score = max(all_scores)
            lowest_score = min(all_scores)
            class_average = sum(all_scores)/total_grades
        print("===================================================")
        print("          INSTITUTIONAL PERFORMANCE METRICS        ")
        print("===================================================")
        print(f" Total Graded Assignments Tracked : {total_grades}")
        print(f" Maximum Grade Score    : {highest_score:.1f}%")
        print(f" Minimum Grade Score    : {lowest_score:.1f}%")
        print(f" Global Class Average  : {class_average:.1f}%")
        print("===================================================")
        print(f" Courses Included : {sorted(list(enrolled_courses))}")
        print("===================================================")
        input("\nPress Enter to return to Main Menu...")

# Option 0 Code:
    elif choice == '0':
        system_active = False
        print("\nLogging out of portal -- Session terminated")