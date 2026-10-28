# README Claims Audit — Struct-to-Dict

## 1. Program Purpose
**Claim:** The program converts a Python object's attributes into a dictionary.

**Status:** Supported

**Evidence:** The statement `student.__dict__` returns a dictionary containing the object's attributes.

## 2. Class Definition
**Claim:** The program defines a `Student` class.

**Status:** Supported

**Evidence:** The code uses `class Student:` to define the class.

## 3. Student Attributes
**Claim:** The program initializes a student with a name, age, and course.

**Status:** Supported

**Evidence:** The `__init__` method assigns values to `self.name`, `self.age`, and `self.course`.

## 4. Dictionary Conversion
**Claim:** The program uses `__dict__` to access the object's attributes as a dictionary.

**Status:** Supported

**Evidence:** The statement `student_dict = student.__dict__` stores the attributes in a dictionary.

## 5. Output
**Claim:** The program prints the resulting dictionary.

**Status:** Supported

**Evidence:** The statement `print(student_dict)` displays the dictionary.

## 6. Example Output
**Claim:** The program prints the student's name, age, and course in dictionary format.

**Status:** Supported

**Evidence:** The student is initialized with the values `"Jayesh"`, `19`, and `"BTech CSE"`.

## 7. Learning Objectives
**Claim:** The program demonstrates Python classes, objects, attributes, and dictionaries.

**Status:** Supported

**Evidence:** The code defines a class, creates a student object, assigns attributes, and accesses those attributes through `__dict__`.

## Conclusion
All claims reviewed above are supported by the sample `struct-to-dict.py` program. No unsupported claims were identified.
