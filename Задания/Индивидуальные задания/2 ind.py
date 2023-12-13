#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class PlanEducation:
    MAX_SIZE = 10

    def __init__(self, code, name, approval_date, total_hours, disciplines):
        self.code = code
        self.name = name
        self.approval_date = approval_date
        self.total_hours = total_hours
        self.disciplines = disciplines
        self.size = PlanEducation.MAX_SIZE
        self.count = len(disciplines)

    def add_discipline(self, discipline):
        if self.count < self.size:
            if discipline not in self.disciplines:
                self.disciplines.append(discipline)
                self.count += 1

    def remove_discipline(self, discipline):
        if discipline in self.disciplines:
            self.disciplines.remove(discipline)
            self.count -= 1

    def find_discipline_by_semester(self, semester):
        result = [discipline for discipline in self.disciplines if discipline["semester"] == semester]
        return result

    def find_discipline_by_type(self, type):
        result = [discipline for discipline in self.disciplines if discipline["type"] == type]
        return result

    def find_discipline_by_assessment_type(self, assessment_type):
        result = [discipline for discipline in self.disciplines if discipline["assessment_type"] == assessment_type]
        return result

    def calculate_total_hours(self):
        total = 0
        for discipline in self.disciplines:
            total += discipline["total_hours"]
        self.total_hours = total

    def calculate_exams_and_credits_per_semester(self):
        exams_credits = {}
        for discipline in self.disciplines:
            semester = discipline["semester"]
            if semester not in exams_credits:
                exams_credits[semester] = {"exams": 0, "credits": 0}
            if discipline["assessment_type"] == "exam":
                exams_credits[semester]["exams"] += 1
            elif discipline["assessment_type"] == "credit":
                exams_credits[semester]["credits"] += 1
        return exams_credits

    def size(self):
        return self.size

    # Other methods for set operations and group generation can be added as needed

# Example usage
discipline1 = {
    "number": 1,
    "type": "federal",
    "name": "Math",
    "semester": 1,
    "assessment_type": "exam",
    "total_hours": 100,
    "self_study_hours": 40,
    "coursework": True
}

discipline2 = {
    "number": 2,
    "type": "regional",
    "name": "Physics",
    "semester": 2,
    "assessment_type": "credit",
    "total_hours": 120,
    "self_study_hours": 50,
    "coursework": False
}

education_plan = PlanEducation("SP123", "Computer Science", "01/01/2023", 1500, [discipline1, discipline2])
education_plan.calculate_total_hours()
print(education_plan.total_hours)
print(education_plan.find_discipline_by_semester(1))
print(education_plan.calculate_exams_and_credits_per_semester())