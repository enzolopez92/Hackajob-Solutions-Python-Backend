class Solution:
    def run(self, student_list):
        single_student_number = 0
        for student in student_list:
            single_student_number ^= student
        return single_student_number
