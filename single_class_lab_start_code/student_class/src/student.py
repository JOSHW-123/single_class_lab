class Student:
    def __init__(self, input_name, input_cohort):
        self.name = input_name
        self.cohort = input_cohort
        
        
        

    def test_student_has_name(self, input_name):
        self.name == input_name

    def test_student_has_cohort(self, input_cohort):
        self.cohort == input_cohort

    def test_student_can_update_name(self, input_name):
        self.name == input_name

    def test_student_can_change_cohort(self, input_cohort):
        self.cohort = input_cohort

    def test_student_can_talk(self):
        return "I can talk!"