#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="", job=""):
        self.name = name
        self.job = job

   
    def name(self):
        return self._name

    
    def name(self, value):
        if isinstance(value, str) and len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be string under 25 characters.")

 
    def job(self):
        return self._job


    def job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
