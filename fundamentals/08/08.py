# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # `08.ipynb`

# ## ❄ Problem 1 ❄
#
# Consider the following incomplete `Student` class derived from a complete `Person` class.
#
# Complete the `Student` class by writig the following:
#
# - A constructor with
#     - a string `firstName`
#     - a string `lastName`
#     - an integer `id`, and
#     - an integer array or vector `scores` of test scores;
# - A character method `calculate()` which returns a `Student` object's
#     - average, and
#     - grade character based on the scale
# ```
# A | 90-100
# B | 80-89
# C | 70-79
# D | 60-69
# F | <60
# ```

# + tags=[] jupyter={"source_hidden": true}
# Given code to be completed

# class Person:
#     fname = ""
#     lname = ""
#     def desc(self):
#         desc_person = "%s %s is a person." % (self.fname, self.lname)
#         return desc_person

# class Student(Person):
#       def desc(self):
#           desc_person = "%s %s is a student." % (self.fname, self.lname)
#           return desc_person
        
# class Grades(Student):
#       def desc(self):
#            desc_person = "%s %s has grades." % (self.fname, self.lname)
#            return desc_person

# person1 = Person()
# person1.fname = "Gary"
# person1.lname = "Jackson"

# person2 = Student()
# person2.fname = "Gary"
# person2.lname = "Jackson"

# person3 = Grades()
# person3.fname = "Gary"
# person3.lname = "Jackson"

# Sample input and expected output

# ```
# First name: Gary
# Last name: Jackson
# Student ID: 7
# Enter a list grades separated by space: 80 50 90 75 85
# Gary Jackson Student ID 7, you got a C.
# ```

# +
# Solution to problem 1

# Class definitions

class Person:
    fname = ""
    lname = ""
    def desc(self):
        return "%s %s is a person." % (self.fname, self.lname)
    
class Student(Person):
    def desc(self):
        return "%s %s is a student." % (self.fname, self.lname)
        
class Grades(Student):
    def desc(self):
        return "%s %s has grades." % (self.fname, self.lname)

# Object instantiation

person1 = Person()
person1.fname = "Gary"
person1.lname = "Jackson"

person2 = Student()
person2.fname = "Gary"
person2.lname = "Jackson"

person3 = Grades()
person3.fname = "Gary"
person3.lname = "Jackson"

# Quick test

# test code

# print(person1.desc())
# print(person2.desc())
# print(person3.desc())

# Sample input and expected output

# ```
# First name: Gary
# Last name: Jackson
# Student ID: 7
# Enter a list grades separated by space: 80 50 90 75 85
# Gary Jackson Student ID 7, you got a C.
# ```

# +
#
