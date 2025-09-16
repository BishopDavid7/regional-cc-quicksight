# Calculated Fields Documentation – College Boards to Dashboards (Amazon QuickSight)

This document lists calculated fields used or recommended for the QuickSight analysis. Each entry includes:
- **Name** — calculated field name in QuickSight
- **Formula** — QuickSight formula (copy/paste into QuickSight calculated field editor)
- **Description** — what the field means
- **Use case** — where it's used in visuals/analysis

---

## 1) Student Type
**Formula**
ifelse({Age} < 30, 'Youth', 'Adult Continuing Education')
**Description**: Classifies students as Youth (under 30) or Adult Continuing Education (30 and older).  
**Use case**: Breakdowns of evaluation scores, enrollment composition visuals.

## 2) AvgEvaluationByProfessor
**Formula**
avgOver({EvaluationScore}, [Professor], PRE_AGG)
**Description**: Average evaluation score, grouped by Professor.  
**Use case**: Bar charts that rank professors by their average evaluation.

## 3) AvgEvaluationByCourse
**Formula**
avgOver({EvaluationScore}, [Course], PRE_AGG)
**Description**: Average evaluation score per Course.  
**Use case**: Identify top/bottom courses by average evaluations.

## 4) AvgCostByProfessor
**Formula**
avgOver({CostPerCourse}, [Professor], PRE_AGG)
**Description**: Average course cost by professor.  
**Use case**: Compare cost vs evaluation for each professor.

## 5) AvgCostByCourse
**Formula**
avgOver({CostPerCourse}, [Course], PRE_AGG)
**Description**: Average cost per course.  
**Use case**: Identify the most expensive courses (average).

## 6) EvaluationScore_Normalized
**Formula**
({EvaluationScore} - minOver({EvaluationScore}, [], PRE_AGG)) /
(maxOver({EvaluationScore}, [], PRE_AGG) - minOver({EvaluationScore}, [], PRE_AGG))
**Description**: Normalizes individual evaluation scores to a 0–1 scale.  
**Use case**: Comparisons across courses or professors where absolute scales differ.

## 7) CourseEnrollmentCount
**Formula**
countOver({StudentId}, [Course, Semester], PRE_AGG)
**Description**: Number of students enrolled in a course in a semester.  
**Use case**: Use as a proxy for class size in charts and correlation analysis.

## 8) Eval_By_StudentType
**Formula**
avgOver({EvaluationScore}, [{Student Type}], PRE_AGG)
**Description**: Average evaluation score by Student Type (Youth vs Adult Continuing Education).  
**Use case**: Compare evaluations between demographic groups.

## 9) ImprovementPct (example if you have previous evaluation)
**Formula**
({EvaluationScore} - {PreviousEvaluationScore}) / {PreviousEvaluationScore} * 100
**Description**: Percentage improvement between successive evaluations (requires a `PreviousEvaluationScore` field).  
**Use case**: Trend visualizations and evaluating intervention effectiveness.

---
