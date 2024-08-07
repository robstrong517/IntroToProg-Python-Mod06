# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Rob Armstrong>,<08/05/2024>,<Assignment06>
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.json"

students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files.

    ChangeLog: (Who, When, What)
    RArmstrong,08.05.2024,Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a JSON file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        RArmstrong,08.05.2024,Created function

        :return: list
        """
        try:
            with open(file_name, "r") as file:
                student_data = json.load(file)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a JSON file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        RArmstrong,08.05.2024,Created function

        :return: None
        """
        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file)
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message, error=e)


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output.

    ChangeLog: (Who, When, What)
    RArmstrong,08.05.2024,Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays custom error messages to the user.

        ChangeLog: (Who, When, What)
        RArmstrong,08.05.2024,Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user.

        ChangeLog: (Who, When, What)
        RArmstrong,08.05.2024,Created function

        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user.

        :return: string with the user's choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise ValueError("Please, choose only 1, 2, 3, or 4")
        except ValueError as e:
            IO.output_error_messages(message=str(e))  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays student names and course names to the user.

        ChangeLog: (Who, When, What)
        RArmstrong,08.05.2024,Created function

        :return: None
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name, with a course name from the user.

        ChangeLog: (Who, When, What)
        RArmstrong,08.05.2024,Created function

        :return: list with new student data
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was an incorrect type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data



# Start of main body --------------------------------------- #

# When the program starts, read the file data into a list of lists (table)
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:
    # Present the menu of choices
    IO.output_menu(menu=MENU)

    # Get menu choice
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":
        students = IO.input_student_data(student_data=students)

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(student_data=students)

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)

    # Stop the loop
    elif menu_choice == "4":
        break

    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")