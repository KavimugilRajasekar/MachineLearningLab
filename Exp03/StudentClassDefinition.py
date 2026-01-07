import re
from collections import defaultdict

# -------------------------------
# Student Class Definition
# -------------------------------
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.activities = []
        self.login_count = 0
        self.submit_count = 0
        self.active_session = False

    def add_activity(self, activity, date, time):
        self.activities.append((activity, date, time))

        if activity == "LOGIN":
            self.login_count += 1
            if self.active_session:
                print(f"⚠ Abnormal behavior detected for {self.student_id}: Multiple logins without logout")
            self.active_session = True

        elif activity == "LOGOUT":
            self.active_session = False

        elif activity == "SUBMIT_ASSIGNMENT":
            self.submit_count += 1

    def display_summary(self):
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Logins     : {self.login_count}")
        print(f"Submissions: {self.submit_count}")
        print("-" * 35)


# -------------------------------
# Generator to Read Log File
# -------------------------------
def read_log_file(filename):
    with open(filename, "r") as file:
        for line in file:
            try:
                parts = [p.strip() for p in line.split("|")]
                if len(parts) != 5:
                    raise ValueError("Invalid format")

                student_id, name, activity, date, time = parts

                # Regex validations
                if not re.match(r"S\d+", student_id):
                    raise ValueError("Invalid Student ID")

                if activity not in {"LOGIN", "LOGOUT", "SUBMIT_ASSIGNMENT"}:
                    raise ValueError("Invalid Activity")

                yield student_id, name, activity, date, time

            except Exception as e:
                print(f"❌ Skipping invalid entry: {line.strip()} ({e})")


# -------------------------------
# Main Processing
# -------------------------------
students = {}
daily_stats = defaultdict(int)

input_file = "activity_log.txt"
output_file = "activity_report.txt"

for record in read_log_file(input_file):
    sid, name, activity, date, time = record

    if sid not in students:
        students[sid] = Student(sid, name)

    students[sid].add_activity(activity, date, time)
    daily_stats[(date, activity)] += 1


# -------------------------------
# Display and Save Report
# -------------------------------
with open(output_file, "w") as out:
    print("\n----- Student Activity Report -----\n")
    out.write("----- Student Activity Report -----\n\n")

    for student in students.values():
        student.display_summary()
        out.write(
            f"{student.student_id} | {student.name} | "
            f"Logins: {student.login_count} | "
            f"Submissions: {student.submit_count}\n"
        )

    print("\n----- Daily Activity Statistics -----\n")
    out.write("\n----- Daily Activity Statistics -----\n")

    for (date, activity), count in daily_stats.items():
        line = f"{date} - {activity}: {count}\n"
        print(line.strip())
        out.write(line)
