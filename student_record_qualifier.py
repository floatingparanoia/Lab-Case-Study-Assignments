""" 
Amelia Cortez
student_record_qualifier
This program will ask the student for their last name, first name, and gpa.
The program will then determine by gpa input if they made the deans list
or honor roll list. It will display what list they made or inform the
student if they did not make either list.
"""

while True:
    last_name = input("Enter your last name or ZZZ to quit: ").upper()
    if last_name == "ZZZ":
        print("Program Ended")
        break
    
    first_name = input("Enter your first name: ").upper()
    
    while True:
        try:
            student_gpa = float(input("Enter student's GPA: "))
            if 0.0 <= student_gpa <= 4.0:
                break
            else:
                print("Invalid input, GPA should be between 0.0 and 4.0. Please enter a valid input")
        except ValueError:
            print("Invalid input, please enter your GPA as a numeric value")
        
    
    if student_gpa >= 3.5:
        print(f"{first_name} {last_name} made it on the Dean's list!")
    elif student_gpa >= 3.25:
        print(f"{first_name} {last_name} made it on the Honor Roll!")
    else:
        print(f"{first_name} {last_name} did not make it on the Dean's list or Honor Roll")



    
        
