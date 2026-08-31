students = {}

try:
    file = open("students.txt", "r")

    for line in file:
        data = line.strip().split(",")

        if len(data) >= 4:
            student_id = data[0]
            name = data[1]
            age = data[2]
            courses = tuple(data[3:])

            students[student_id] = {
                "name": name,
                "age": age,
                "courses": courses
            }

    file.close()

except:
    pass


while True:

    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Courses")
    print("5. Delete Student")
    print("6. Save and Exit")

    choice = input("Choose: ")

    if choice == "1":

        student_id = input("ID: ")
        name = input("Name: ")
        age = input("Age: ")
        courses = input("Courses: ").split()

        students[student_id] = {
            "name": name,
            "age": age,
            "courses": tuple(courses)
        }

        print("Student Added")

    elif choice == "2":

        if len(students) == 0:
            print("No Students")

        else:
            for student_id in students:

                print("ID:", student_id)
                print("Name:", students[student_id]["name"])
                print("Age:", students[student_id]["age"])
                print("Courses:", ", ".join(students[student_id]["courses"]))
                print()

    elif choice == "3":

        search = input("Enter ID or Name: ").lower()

        found = False

        for student_id in students:

            if student_id == search or students[student_id]["name"].lower().startswith(search):

                print("ID:", student_id)
                print("Name:", students[student_id]["name"])
                print("Age:", students[student_id]["age"])
                print("Courses:", ", ".join(students[student_id]["courses"]))

                found = True

        if found == False:
            print("Student Not Found")

    elif choice == "4":

        student_id = input("Student ID: ")

        if student_id in students:

            course_set = set(students[student_id]["courses"])

            print("1. Add Course")
            print("2. Remove Course")

            x = input("Choose: ")

            if x == "1":

                course = input("Course: ")
                course_set.add(course)

            elif x == "2":

                course = input("Course: ")
                course_set.discard(course)

            students[student_id]["courses"] = tuple(course_set)

            print("Updated")

        else:
            print("Student Not Found")

    elif choice == "5":

        student_id = input("Student ID: ")

        if student_id in students:
            del students[student_id]
            print("Deleted")

        else:
            print("Student Not Found")

    elif choice == "6":

        file = open("students.txt", "w")

        for student_id in students:

            line = student_id + "," + students[student_id]["name"] + "," + str(students[student_id]["age"])

            for course in students[student_id]["courses"]:
                line += "," + course

            file.write(line + "\n")

        file.close()

        print("Data Saved")
        break

    else:
        print("Wrong Choice")