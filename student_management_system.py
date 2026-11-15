# PROJECT — STUDENT PERFORMANCE MANAGEMENT SYSTEM


# importing total records!
import json


def get_students_record():
    try:
        with open("students_record.json", "r") as file:
            students_record = json.load(file)
            return students_record
    except FileNotFoundError:
        students_record = []
        return students_record
    except json.JSONDecodeError:
        print("Empty file or Corrupted file found!")
        exit()


students = get_students_record()


# taking valid value
def get_valid_value(value):
    while True:
        try:
            given_value = int(input(f"Enter a valid {value}: "))
            if given_value <= 0:
                print(f"Enter a valid {value}!")
            else:
                return given_value
        except ValueError:
            print(f"Enter a valid {value}!")


# taking valid marks
def get_valid_score(value):
    while True:
        try:
            given_value = float(input(f"Enter the student's {value}'s score: "))
            if given_value < 0 or given_value > 100:
                print(f"Enter a valid score!")
            else:
                return given_value
        except ValueError:
            print(f"Enter a valid score!")


# taking valid name
def get_valid_name(valid_name):
    print(f"Enter the {valid_name}'s name -> ")
    while True:
        fst_name = input("Enter first name: ").lower().capitalize().strip()
        if not fst_name.isalpha():
            print("enter only alphabetical words!")
        else:
            if len(fst_name) > 30:
                print("no. of letters exceeded!")
            else:
                break
    while True:
        lst_name = input("Enter last name: ").capitalize().strip()
        if not lst_name.isalpha():
            print("enter only alphabetical words!")
        else:
            if len(lst_name) > 30:
                print("no. of letters exceeded!")
            else:
                break
    name = fst_name + " " + lst_name
    return name


# taking valid phone number
def get_valid_phone_number(name):
    while True:
        number = input(f"Enter {name}'s phone number: (+91)-")
        if not number.isnumeric():
            print("Enter only numeric values!!")
        else:
            if not len(number) == 10:
                print("Enter 10 digit phone number")
            else:
                return number


# taking valid email
def get_valid_email(person):
    while True:
        email = input(f"Enter {person}'s email: ")
        email = email.strip()
        if email == "":
            print("Email must not be empty.")
        else:
            if not ("." in email and "@" in email):
                print("Email must contain '.' and '@' ")
            else:
                if not (email.count("@") == 1):
                    print("Email must contain exactly one '@' symbol")
                else:
                    if not email.endswith((".com", ".org", ".net")):
                        print("Email must end with '.com', '.org' or '.net'")
                    else:
                        if len(email) > 254:
                            print("Email must not be longer than 254 characters")
                        else:

                            if not (email[0].isalnum() and email[-1].isalnum()):
                                print("Email must start and end with a letter or digit")
                            else:
                                return email


# funtion of Register New Student(option 1)
def register_student():
    student_id = get_valid_value("ID")
    student_name = get_valid_name("Student")
    student_number = get_valid_phone_number("Student")
    student_email = get_valid_email("Student")
    guardian_name = get_valid_name("Guardian")
    guardian_number = get_valid_phone_number("Guardian")
    guardian_email = get_valid_email("Guardian")
    return {
        "Student ID": student_id,
        "Student Name": student_name,
        "Student Number": student_number,
        "Student Email": student_email,
        "Guardian Name": guardian_name,
        "Guardian Number": guardian_number,
        "Guardian Email": guardian_email,
        "Academic Scores": {
            "Python": None,
            "Mathematics": None,
            "Physics": None
        }
    }


def get_academic_score():
    while True:
        ID = get_valid_value("Student's ID")
        for student in students:
            if ID == student["Student ID"]:
                print(f"Student found!\n Student's name = {student["Student Name"]}\n")
                if all(score is None for score in student["Academic Scores"].values()):
                    python = get_valid_score("PYTHON")
                    mathematics = get_valid_score("MATHEMATICS")
                    physics = get_valid_score("PHYSICS")
                    student["Academic Scores"]["Python"] = python
                    student["Academic Scores"]["Mathematics"] = mathematics
                    student["Academic Scores"]["Physics"] = physics
                    return {
                        "Python": python,
                        "Mathematics": mathematics,
                        "Physics": physics
                    }
                else:
                    print("This student's scores have been registered already!")
        else:
            print("THIS ID ISN'T REGISTERED!")


def update_academic_score():
    while True:
        ID = get_valid_value("Student's ID")
        for student in students:
            if ID == student["Student ID"]:
                print(f"Student found!\n Student's name = {student["Student Name"]}\n")
                subject = input("Which subject's score you want to change? : ").lower().strip()
                if subject.isalpha():
                    if subject == "python":
                        python = get_valid_score("PYTHON")
                        student["Academic Scores"]["Python"] = python
                        return python
                    elif subject == "mathematics":
                        mathematics = get_valid_score("MATHEMATICS")
                        student["Academic Scores"]["Mathematics"] = mathematics
                        return mathematics
                    elif subject == "physics":
                        physics = get_valid_score("PHYSICS")
                        student["Academic Scores"]["Physics"] = physics
                        return physics
                    else:
                        print("Please Enter A Valid Subject")
                else:
                    print("In subject name, numbers aren't allowed!")
        else:
            print("THIS ID ISN'T REGISTERED!")


def display_student_details(student, heading):
    print(f"\n\n{"-"*40} \n{heading:^40}\n {"-"*40}\n\n\n")
    print(f"{"Student ID":<20}: {student["Student ID"]}")
    print(f"{"Student Name":<20}: {student["Student Name"]}")
    print(f"{"Student Number":<20}: {student["Student Number"]}")
    print(f"{"Student Email":<20}: {student["Student Email"]}\n\n")
    print(f"{"Guardian Name":<20}: {student["Guardian Name"]}")
    print(f"{"Guardian Number":<20}: {student["Guardian Number"]}")
    print(f"{"Guardian Email":<20}: {student["Guardian Email"]}\n\n")
    print(f"{"ACADEMIC SCORES":<20}")
    print(f"{"-"*40}")
    if student["Academic Scores"]["Python"] is not None:
        print(f"{"Python":<20}: {student["Academic Scores"]["Python"]}/100")
    else:
        print(f"{"Python":<20}: Not Registered")
    if student["Academic Scores"]["Mathematics"] is not None:
        print(f"{"Mathematics":<20}: {student["Academic Scores"]["Mathematics"]}/100")
    else:
        print(f"{"Mathematics":<20}: Not Registered")
    if student["Academic Scores"]["Physics"] is not None:
        print(f"{"Physics":<20}: {student["Academic Scores"]["Physics"]}/100")
    else:
        print(f"{"Physics":<20}: Not Registered")


def save_student_record():
    with open("students_record.json", "w") as file:
        json.dump(students, file, indent=4)


def update_student_details(student):
    heading = "UPDATE STUDENT DETAILS"
    print(f"\n\n{"-"*40} \n{heading:^40}\n {"-"*40}\n\n\n")
    while True:
        print(f"1. Update Student Name\n2. Update Student Phone Number\n3. Update Student Email\n4. Upadte Student's Guardian Name\n5. Update Student's Guardian Phone Number\n6. Update Student's Guardian Email\n7. EXIT")
        sub_option = get_valid_value("option")
        if sub_option == 1:
            print(f"\nOLD NAME: {student["Student Name"]}\nUPDATING...")
            new_student_name = get_valid_name("Student")
            student["Student Name"] = new_student_name
            print("SUCCESSFULLY UPDATED NAME!\n\n")
            save_student_record()
        elif sub_option == 2:
            print(f"\nOLD PHONE NUMBER: {student["Student Number"]}\nUPDATING...")
            new_student_number = get_valid_phone_number("Student")
            student["Student Number"] = new_student_number
            print("SUCCESSFULLY UPDATED PHONE NUMBER!\n\n")
            save_student_record()
        elif sub_option == 3:
            print(f"\nOLD EMAIL: {student["Student Email"]}\nUPDATING...")
            new_student_email = get_valid_email("Student")
            student["Student Email"] = new_student_email
            print("SUCCESSFULLY UPDATED EMAIL!\n\n")
            save_student_record()
        elif sub_option == 4:
            print(f"\nOLD NAME: {student["Guardian Name"]}\nUPDATING...")
            new_student_guardian_name = get_valid_name("Guardian")
            student["Guardian Name"] = new_student_guardian_name
            print("SUCCESSFULLY UPDATED NAME!\n\n")
            save_student_record()
        elif sub_option == 5:
            print(f"\nOLD PHONE NUMBER: {student["Guardian Number"]}\nUPDATING...")
            new_student_guardian_number = get_valid_phone_number("Guardian")
            student["Guardian Number"] = new_student_guardian_number
            print("SUCCESSFULLY UPDATED PHONE NUMBER!\n\n")
            save_student_record()
        elif sub_option == 6:
            print(f"\nOLD Email: {student["Guardian Email"]}\nUPDATING...")
            new_student_guardian_email = get_valid_email("Guardian")
            student["Guardian Email"] = new_student_guardian_email
            print("SUCCESSFULLY UPDATED EMAIL!\n\n")
            save_student_record()
        elif sub_option == 7:
            break
        else:
            print("\nPLEASE ENTER AN OPTION FROM ABOVE MENU\n")


def del_student(student):
    students.remove(student)


def get_individual_report(student):
    heading = "individual student report".upper()
    print(f"{"="*40} \n{heading:^40}\n {"="*40}\n\n")
    print(f"STUDENT ID: {student["Student ID"]}\n")
    print(f"STUDENT NAME: {student["Student Name"]}")
    heading = "REPORT CARD".upper()
    print(f"{"-"*40} \n{heading:^40}\n {"-"*40}\n\n")
    if student["Academic Scores"]["Python"] is not None:
        print(f"{"Python":<20}: {student["Academic Scores"]["Python"]}/100")
    else:
        print(f"{"Python":<20}: Not Registered")
    if student["Academic Scores"]["Mathematics"] is not None:
        print(f"{"Mathematics":<20}: {student["Academic Scores"]["Mathematics"]}/100")
    else:
        print(f"{"Mathematics":<20}: Not Registered")
    if student["Academic Scores"]["Physics"] is not None:
        print(f"{"Physics":<20}: {student["Academic Scores"]["Physics"]}/100")
    else:
        print(f"{"Physics":<20}: Not Registered")
    if all(score is not None for score in student["Academic Scores"].values()):
        total_sum = sum(student["Academic Scores"].values())
        print(f"\nTOTAL SCORE: {total_sum}")
        perecentage_total_score = round((total_sum/300)*100, 2)
        print(f"Percentage: {perecentage_total_score}%")
        highest_sub = max(student["Academic Scores"], key=student["Academic Scores"].get)
        print(f"Highest: {highest_sub}({student["Academic Scores"][highest_sub]})\n")
        lowest_sub = min(student["Academic Scores"], key=student["Academic Scores"].get)
        print(f"Lowest: {lowest_sub}({student["Academic Scores"][lowest_sub]})\n")

        if percentage_total_score >= 90:
            print("Remark: Outstanding")
        elif percentage_total_score >= 80:
            print("Remark: Excellent")
        elif percentage_total_score >= 70:
            print("Remark: Very Good")
        elif perecentage_total_score >= 60:
            print("Remark: Good")
        elif perecentage_total_score >= 50:
            print("Remark: Average")
        elif perecentage_total_score >= 40:
            print("Remark: Below Average")
        else:
            print("Remark: Need Improvement")
    else:
        print("\n\nERROR! NOT ALL SUBJECT'S SCORES REGISTERED.")


def get_class_average_percentage():
    total_score_all_students = 0
    if student_with_registered_score != []:
        for student in student_with_registered_score:
            total_score_all_students += sum(student["Academic Scores"].values())
            class_average_percentage = round(((total_score_all_students)/(300*len(student_with_registered_score)))*100, 2)
        return class_average_percentage
    else:
        print("N/A")


def get_highest_overall_scorer():
    if student_with_registered_score != []:
        highest_scorer = max(student_with_registered_score, key=lambda student: sum(student["Academic Scores"].values()))
        highest_scorer_percentage = round((((sum(highest_scorer["Academic Scores"].values()))/300)*100), 2)
        print(f"{"HIGHEST SCORER":<30} : {highest_scorer["Student Name"]}, OVERALL PERCENTAGE: {highest_scorer_percentage}%")
    else:
        print(f"{"HIGHEST SCORER":<30} : N/A, OVERALL PERCENTAGE: N/A")


def get_lowest_overall_scorer():
    if student_with_registered_score != []:
        lowest_scorer = min(student_with_registered_score, key=lambda student: sum(student["Academic Scores"].values()))
        lowest_scorer_percentage = round((((sum(lowest_scorer["Academic Scores"].values()))/300)*100), 2)
        print(f"{"LOWEST SCORER":<30} : {lowest_scorer["Student Name"]}, OVERALL PERCENTAGE: {lowest_scorer_percentage}%")
    else:
        print(f"{"LOWEST SCORER":<30} : N/A, OVERALL PERCENTAGE: N/A")


def get_subject_wise_class_average():
    print(f"{"SUBJECT WISE CLASS AVERAGE":<40}\n{"-"*40}")
    total_score_python = 0
    python_count = 0
    for student in students:
        if student["Academic Scores"]["Python"] is not None:
            total_score_python += student["Academic Scores"]["Python"]
            python_count += 1
        else:
            continue
    total_score_mathematics = 0
    mathematics_count = 0
    for student in students:
        if student["Academic Scores"]["Mathematics"] is not None:
            total_score_mathematics += student["Academic Scores"]["Mathematics"]
            mathematics_count += 1
        else:
            continue
    total_score_physics = 0
    physics_count = 0
    for student in students:
        if student["Academic Scores"]["Physics"] is not None:
            total_score_physics += student["Academic Scores"]["Physics"]
            physics_count += 1
        else:
            continue
    if python_count != 0:
        class_average_percentage_python = round((((total_score_python)/(100*(python_count)))*100), 2)
        print(f"{"PYTHON":<20}: {class_average_percentage_python}%")
    else:
        print("No values are registered of any student in PYTHON!")
    if mathematics_count != 0:
        class_average_percentage_mathematics = round((((total_score_mathematics)/(100*(mathematics_count)))*100), 2)
        print(f"{"MATHEMATICS":<20}: {class_average_percentage_mathematics}%")
    else:
        print("No values are registered of any student in MATHEMATICS!")
    if physics_count != 0:
        class_average_percentage_physics = round((((total_score_physics)/(100*(physics_count)))*100), 2)
        print(f"{"PHYSICS":<20}: {class_average_percentage_physics}%")
    else:
        print("No values are registered of any student in PHYSICS!")


def get_class_performance_distribution():
    print(f"{"CLASS PERFORMANCE DISTRIBUTION":<40}\n{"-"*40}")
    performance_dict = {
        "Outstanding": 0,
        "Excellent": 0,
        "Very Good": 0,
        "Good": 0,
        "Average": 0,
        "Below Average": 0,
        "Need Improvement": 0
    }

    for student in student_with_registered_score:
        total_sum = sum(student["Academic Scores"].values())
        perecentage_total_score = round((total_sum/300)*100, 2)

        if perecentage_total_score >= 90:
            performance_dict["Outstanding"] += 1
        elif perecentage_total_score >= 80:
            performance_dict["Excellent"] += 1
        elif perecentage_total_score >= 70:
            performance_dict["Very Good"] += 1
        elif perecentage_total_score >= 60:
            performance_dict["Good"] += 1
        elif perecentage_total_score >= 50:
            performance_dict["Average"] += 1
        elif perecentage_total_score >= 40:
            performance_dict["Below Average"] += 1
        else:
            performance_dict["Need Improvement"] += 1
    print(f"{"Outstanding":<20} : {performance_dict["Outstanding"]}")
    print(f"{"Excellent":<20} : {performance_dict["Excellent"]}")
    print(f"{"Very Good":<20} : {performance_dict["Very Good"]}")
    print(f"{"Good":<20} : {performance_dict["Good"]}")
    print(f"{"Average":<20} : {performance_dict["Average"]}")
    print(f"{"Below Average":<20} : {performance_dict["Below Average"]}")
    print(f"{"Need Improvement":<20} : {performance_dict["Need Improvement"]}")


while True:
    heading = "student management system".upper()
    print(f"{"="*40} \n{heading:^40}\n {"="*40}\n")
    print(f"1. Register New Student\n2. Enter / Update Student Marks\n3. View All Students\n4. Search Student\n5. Update Student Details\n6. Delete Student\n7. Individual Performance Analysis\n8. Class Performance Statistics\n9. EXIT")
    option = get_valid_value("option")

# REGISTERING STUDENT
    if option == 1:
        new_student = register_student()
        if any(new_student["Student ID"] == student["Student ID"] for student in students):
            print("this student ID already exits! cant upload duplicate ID!")
        else:
            students.append(new_student)
            with open("students_record.json", "w") as file:
                json.dump(students, file, indent=4)
            print("REGISTERED SUCCESSFULLY!")

# REGISTERING/UPDATING SCORES
    elif option == 2:
        heading = "student academic score system".upper()
        print(f"{"="*40} \n{heading:^40}\n {"="*40}\n")
        print(f"Do you want to register the student's new score OR update the student's score?\n 1. Register new score\n 2. Update\n 3. EXIT")
        sub_option = get_valid_value("option")
        if sub_option == 1:
            score = get_academic_score()
            with open("students_record.json", "w") as file:
                json.dump(students, file, indent=4)
            print(f"successfully registered student's new scores!\n View the student's score: {score}")

        if sub_option == 2:
            updated_score = update_academic_score()
            with open("students_record.json", "w") as file:
                students_record = json.dump(students, file, indent=4)
            print(f"Successfully updated student's choosen subject's score!\n view the updated score -> {updated_score}")

# VIEW TOTAL STUDENTS
    elif option == 3:
        heading = "total students".upper()
        print(f"\n\n{"="*40} \n{heading:^40}\n {"="*40}\n\n\n")
        print(f"Total Registered Students: {len(students)}\n\n")
        if not students:
            print("No Student Records Found!\n Please Register A Student First.")
        else:
            for n, student in enumerate(students, start=1):
                heading = "STUDENT" + "-" + str(n)
                display_student_details(student, heading)

# SEARCH STUDENT
    elif option == 4:
        heading = "search student".upper()
        print(f"\n\n{"="*40} \n{heading:^40}\n {"="*40}\n\n")
        ID = get_valid_value("Student's ID")
        for student in students:
            if ID == student["Student ID"]:
                print(f"\nStudent found!\nStudent's name = {student["Student Name"]}\n")
                display_student_details(student, "STUDENT DETAILS")
                break
        else:
            print(f"No student found with ID: {ID}")

# UPDATE STUDENT DETAILS
    elif option == 5:
        heading = "search student".upper()
        print(f"\n\n{"="*40} \n{heading:^40}\n {"="*40}\n\n")
        ID = get_valid_value("Student's ID")
        for student in students:
            if ID == student["Student ID"]:
                print(f"\nStudent Found!\nStudent's name = {student["Student Name"]}\n")
                update_student_details(student)
                break
        else:
            print(f"No student found with ID: {ID}")

# DELETE STUDENT
    elif option == 6:
        heading = "delete student".upper()
        print(f"\n\n{"="*40} \n{heading:^40}\n {"="*40}\n\n")
        ID = get_valid_value("Student's ID")
        student_found = False
        for student in students:
            if ID == student["Student ID"]:
                student_found = True
                print(f"\nStudent Found!\nStudent's name = {student["Student Name"]}\n")
                while True:
                    confirmation = input(f"DO YOU REALLY WANT TO DELETE THE STUDENT WITH ID: {ID}?- (YES/NO): ").lower()
                    if confirmation.isalpha():
                        if confirmation == "yes":
                            del_student(student)
                            print("SUCCESSFULLY DELETED THE STUDENT!")
                            save_student_record()
                            break
                        elif confirmation == "no":
                            break
                        else:
                            print("ONLY TYPE - YES or NO")
        if not student_found:
            print(f"NO STUDENT FOUND WITH ID: {ID}")

# INDIVIDUAL PERFORMANCE REPORT
    elif option == 7:
        heading = "SEARCH STUDENT".upper()
        print(f"{"-"*40} \n{heading:^40}\n {"-"*40}\n")
        ID = get_valid_value("Student's ID")
        for student in students:
            if ID == student["Student ID"]:
                get_individual_report(student)
                break
        else:
            print(f"NO STUDENT WITH ID: {ID}")

# CLASS PERFORMANCE STATISTICS
    elif option == 8:
        heading = "class report".upper()
        print(f"{"="*40} \n{heading:^40}\n {"="*40}\n\n")
        print(f"Total Registered Students: {len(students)}")
        student_with_registered_score = []
        for student in students:
            if all(score is not None for score in student["Academic Scores"].values()):
                student_with_registered_score.append(student)
        print(f"No.of students with registered score of all subject: {len(student_with_registered_score)}")
        average_percentage = get_class_average_percentage()
        if average_percentage is not None:
            print(f"{"CLASS AVERAGE PERCENTAGE":<30} : {round(average_percentage, 2)}%")
        else:
            print(f"{"CLASS AVERAGE PERCENTAGE":<30} : N/A")
        get_highest_overall_scorer()
        get_lowest_overall_scorer()
        get_subject_wise_class_average()
        get_class_performance_distribution()

    elif option == 9:
        break
    else:
        print("\nPLEASE ENTER AN OPTION FROM ABOVE MENU\n")
