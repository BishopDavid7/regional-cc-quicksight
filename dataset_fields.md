# Dataset fields — Q - Student Enrollment

This file lists the field names used in the `Q - Student Enrollment` dataset, with types and short descriptions.

FieldName | Type | Description
---|---:|---
StudentId | string | Unique student identifier
StudentName | string | Full name of student
Age | integer | Age at admission
NationalOrigin | string | Country of Residence on admission application (renamed from HomeOfOrigin)
Gender | string | Gender of student
StudentClassification | string | e.g., Freshman, Sophomore, Continuing Ed
Major | string | Primary academic major
Course | string | Course title
CourseId | string | Unique course identifier
Credit | integer | Credit units for the course
CostPerCourse | decimal | Administrative cost per course (USD or local currency)
EvaluationScore | decimal | Student evaluation score for professor (0-100)
TestScore | decimal | Average test score for this student/course
Grade | string | Final grade (A, B, C, etc.)
Semester | string | Semester identifier (e.g., Fall 2024)
AcademicYear | integer | Academic year (e.g., 2024)
EnrollmentDate | date | Date of enrollment
GraduationDate | date | Graduation date (if available)
Student Type | string | Calculated field: 'Youth' or 'Adult Continuing Education'
