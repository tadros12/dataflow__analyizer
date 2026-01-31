class Course:
    _id_counter = 1


    def __init__(self, name):
        self.course_id = Course._id_counter

        Course._id_counter += 1
        self.name = name
        self.enrolled_students = []


    def __str__(self):
        return f"course ID:{self.course_id},name{self.name},Enrolled :{len(self.enrolled_students)}"
    

    def enroll_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            print("student enrolled")

        else:
            print("sutdent already enrolled")

    def remove_student(self, student):
        # for course in self.Course.values():
            if student in self.enrolled_students:
                 
                 
