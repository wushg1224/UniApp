from common.color import Color
from models.student import Student
from models.subject import Subject


class StudentView:

    def login(self):
        email = input("\tEmail: ")
        password = input("\tPassword: ")

        return (email, password)

    def register_step1(self):
        email = input("\tEmail: ")
        password = input("\tPassword: ")

        return (email, password)

    def register_step2(self):
        while True:
            username = input("\tName: ").strip()
            if username:  # Ensure the input is not empty or just whitespace
                return username
            else:
                Color.prRed("\tName cannot be empty. Please enter a valid name.")

    def get_confirm_password(self, newpassword):
        confirmnewpassword = input("\t\tConfirm Password: ")
        while confirmnewpassword != newpassword:
            Color.prRed("\t\tPassword does not match - try again")
            return self.get_confirm_password(newpassword)

        return confirmnewpassword

    def get_new_password(self):
        Color.prYellow("\t\tUpdating Password")
        newpassword = input("\t\tNew Password: ")
        confirmnewpassword = self.get_confirm_password(newpassword)

        return (newpassword, confirmnewpassword)

    def enrol_subject(self, student: Student, subject: Subject):
        Color.prYellow(f"\t\tEnrolling in {subject.name}")
        Color.prYellow(
            f"\t\tYou are now enrolled in {len(student.enrolment)} out of 4 subjects"
        )

    def view_enrolment(self, student: Student):
        Color.prYellow(f"\t\tShowing {len(student.enrolment)} subjects")
        if student.enrolment:
            for subject in student.enrolment:
                print(f"\t\t[ {subject.__str__()} ]")

    def remove_subject(self):
        removesubjectbyid = input("\t\tRemove Subject by ID: ")

        return removesubjectbyid
