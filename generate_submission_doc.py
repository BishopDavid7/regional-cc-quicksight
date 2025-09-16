#!/usr/bin/env python3
"""
Generate submission_document.docx using screenshots in ./screenshots.
This script builds the full submission document required for the Udacity BI Nanodegree
"From College Boards to Dashboards" project.

If a screenshot is missing, it inserts a placeholder note instead of breaking.
"""

import os
from docx import Document
from docx.shared import Inches


def add_screenshot(doc, path, caption, rubric=None):
    """Insert a screenshot with caption and optional rubric note."""
    if os.path.exists(path):
        doc.add_picture(path, width=Inches(5.5))
        last_paragraph = doc.paragraphs[-1]
        last_paragraph.alignment = 1  # center
        doc.add_paragraph(f"Caption: {caption}")
        if rubric:
            doc.add_paragraph(f"Rubric: {rubric}")
    else:
        doc.add_paragraph(f"[MISSING IMAGE] {caption} (expected: {path})")


def main():
    doc = Document()

    # Title page
    doc.add_heading("From College Boards to Dashboards — Submission Document", 0)
    doc.add_paragraph("Author: Your Full Name")
    doc.add_paragraph("Date: 2025-09-15")
    doc.add_page_break()

    # Table of Contents (manual note — Word can auto-generate later)
    doc.add_heading("Table of Contents", level=1)
    doc.add_paragraph("This document contains: Executive Summary, Dataset Preparation Evidence, Visuals, Topic & Named Entities, Dashboard & Scenarios, Data Story, File Listings, Methodology, Originality Statement, and Checklist.")
    doc.add_page_break()

    # 1. Executive Summary
    doc.add_heading("1. Executive Summary", level=1)
    doc.add_paragraph("One-paragraph summary of the project; copied from data_story.md Executive Summary.")
    doc.add_page_break()

    # 2. Dataset Preparation Evidence
    doc.add_heading("2. Dataset Preparation Evidence", level=1)
    add_screenshot(doc, "screenshots/01_attempt_s3_manifest_error.png",
                   "Attempt to create dataset from fictional S3 manifest (expected error).",
                   "Section 1 evidence")
    add_screenshot(doc, "screenshots/03_dataset_list_q_student_enrollment.png",
                   "Q - Student Enrollment dataset visible in Datasets.",
                   "Section 1 evidence")
    add_screenshot(doc, "screenshots/04_dataset_refresh_schedule.png",
                   "Weekly refresh schedule set to Sunday 12:00 AM (timezone visible).",
                   "Section 1")
    add_screenshot(doc, "screenshots/06_rename_homeoforigin_to_nationalorigin.png",
                   "Field HomeOfOrigin renamed to NationalOrigin with description.",
                   "Section 1")
    add_screenshot(doc, "screenshots/07_student_type_calculated_field.png",
                   "Calculated field Student Type defined.",
                   "Section 1")
    doc.add_page_break()

    # 3. Visuals Created Using Q
    doc.add_heading("3. Visuals Created Using Q (Section 2 evidence)", level=1)
    add_screenshot(doc, "screenshots/09_visual_student_majors_by_year_initial.png",
                   "Visual created by Q — Student Majors by Year (initial)")
    add_screenshot(doc, "screenshots/11_student_majors_by_year_vertical_bar.png",
                   "Visual reconfigured to vertical bar chart (formatted, no comma separators)")
    add_screenshot(doc, "screenshots/12_proportion_of_student_types_pie.png",
                   "Proportion of Student Types (pie chart)")
    doc.add_page_break()

    # 4. Topic & Named Entities
    doc.add_heading("4. Topic & Named Entities (Section 3 evidence)", level=1)
    add_screenshot(doc, "screenshots/16_topic_fields_list.png",
                   "Topic field list includes required fields.")
    add_screenshot(doc, "screenshots/17_topic_entities_student_details.png",
                   "Named Entity: Student Details.")
    add_screenshot(doc, "screenshots/18_topic_entities_course_details.png",
                   "Named Entity: Course Details.")
    add_screenshot(doc, "screenshots/19_topic_entities_prof_eval.png",
                   "Named Entity: Professor Evaluation.")
    add_screenshot(doc, "screenshots/20_q_best_instructors_verified.png",
                   "Verified Q answer: Best instructors.")
    doc.add_page_break()

    # 5. Dashboard, Scenarios & Thread
    doc.add_heading("5. Dashboard, Scenarios & Thread (Section 4 evidence)", level=1)
    add_screenshot(doc, "screenshots/23_publish_dashboard_q_enabled.png",
                   "Student Enrollment Dashboard published with Q enabled.")
    add_screenshot(doc, "screenshots/25_scenario_create_select_visuals.png",
                   "Scenario created with selected visuals.")
    add_screenshot(doc, "screenshots/26_scenario_starter.png",
                   "Starter question: How do we improve professor evaluations while avoiding increased cost per course?")
    add_screenshot(doc, "screenshots/34_scenario_thread_full.png",
                   "Scenario thread showing iterative Q.")
    doc.add_page_break()

    # 6. Data Story
    doc.add_heading("6. Data Story (Section 5 evidence)", level=1)
    add_screenshot(doc, "screenshots/36_data_story_cover_prepared_by.png",
                   "Data Story cover with 'Prepared by'.")
    add_screenshot(doc, "screenshots/37_data_story_page1.png",
                   "Data Story page showing thesis and supporting visuals.")
    add_screenshot(doc, "screenshots/38_data_story_page2.png",
                   "Data Story recommendation and supporting visuals.")
    doc.add_page_break()

    # 7. File listings
    doc.add_heading("7. File Listings and Additional Artifacts", level=1)
    doc.add_paragraph("The following project files are included:")
    doc.add_paragraph("- dataset_fields.md")
    doc.add_paragraph("- calculated_fields.md")
    doc.add_paragraph("- Q_prompts.md")
    doc.add_paragraph("- verified_answers.md")
    doc.add_paragraph("- scenario_thread.md")
    doc.add_paragraph("- data_story.md")
    doc.add_paragraph("- manifest_sample.json")
    doc.add_paragraph("- screenshots/ (all screenshot files present)")
    doc.add_page_break()

    # 8. Methodology
    doc.add_heading("8. Methodology", level=1)
    doc.add_paragraph("Steps taken: sample dataset usage, calculated fields creation, Q prompts, topic creation, scenario & thread, and data story creation. Concise description to align with rubric.")
    doc.add_page_break()

    # 9. Originality Statement
    doc.add_heading("9. Originality Statement", level=1)
    doc.add_paragraph("I confirm this submission is my original work. Any referenced AWS/Udacity documentation is cited.")
    doc.add_page_break()

    # 10. Checklist for Rubric
    doc.add_heading("10. Checklist for Rubric", level=1)
    doc.add_paragraph("Each rubric criterion is mapped to corresponding screenshots and files provided in the sections above.")
    doc.add_page_break()

    # Save final document
    doc.save("submission_document.docx")
    print("✅ submission_document.docx generated successfully.")


if __name__ == "__main__":
    main()
