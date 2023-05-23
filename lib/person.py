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
    def __init__(self, name = "name", job = "Admin"):
        self.name = name
        self.job = job
    
    def set_name(self):
        return self._name
    
    def get_name(self, name):
        try:
            if(type(name) == str) and (len(name) >= 1) and (len(name) <= 25):
                self._name = name.title() 
            else:
                raise NameError("Name must be string between 1 and 25 characters.")
        except NameError as err:
            print(err)
    
    def set_job(self):
        return self._job
    
    def get_job(self, job):
        try:
            if(job in APPROVED_JOBS):
                self._job = job
            else:
                raise LookupError("Job must be in list of approved jobs.")
        except LookupError as err:
            print(err)
    
    name = property(set_name, get_name)
    job = property(set_job, get_job)