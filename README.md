<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>From College Boards to Dashboards — Regional Community College QuickSight Project</title>
  <style>
    body {
      font-family: Arial, Helvetica, sans-serif;
      line-height: 1.6;
      margin: 40px;
      background: #f9fafc;
      color: #222;
    }
    h1, h2, h3 {
      color: #2c3e50;
    }
    a {
      color: #0066cc;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    .screenshot {
      margin: 30px 0;
      border: 1px solid #ddd;
      border-radius: 8px;
      padding: 12px;
      background: #fff;
      text-align: center;
    }
    .screenshot img {
      width: 95%; /* make images bigger */
      max-width: 1200px; /* cap max size for clarity */
      height: auto;
      border-radius: 6px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    hr {
      border: none;
      border-top: 1px solid #ccc;
      margin: 50px 0;
    }
    ul, ol {
      margin-left: 25px;
    }
    footer {
      margin-top: 50px;
      font-size: 0.95em;
      color: #555;
      border-top: 1px solid #ddd;
      padding-top: 15px;
    }
  </style>
</head>
<body>

  <h1>From College Boards to Dashboards — Regional Community College QuickSight Project</h1>

  <p><strong>Author:</strong> Pascal Esegemou Ekenya Fonjock<br>
     <strong>GitHub:</strong> <a href="https://github.com/BishopDavid7/regional-cc-quicksight" target="_blank">regional-cc-quicksight</a><br>
     <strong>Project date:</strong> 2025-09-15</p>

  <hr>

  <h2>📌 Project Summary</h2>
  <p>This Udacity <strong>Future AWS Business Intelligence Engineer Nanodegree</strong> project uses 
     <strong>Amazon QuickSight (Q)</strong> to analyze <strong>student enrollment and course evaluation data</strong>.</p>

  <p>Deliverables include:</p>
  <ul>
    <li>Dataset preparation</li>
    <li>QuickSight Topics & Q prompts</li>
    <li>Interactive visuals</li>
    <li>A Scenario analysis</li>
    <li>A complete Data Story targeted to the Board of Directors</li>
  </ul>

  <div class="screenshot">
    <img src="https://i.postimg.cc/3WzYjYPb/01-attempt-s3-manifest-error-png.png" alt="Dashboard Preview">
  </div>

  <hr>

  <h2>📂 Repo Contents</h2>
  <ul>
    <li><strong>submission_document.docx</strong> — Word file with labeled screenshots (primary submission artifact).</li>
    <li><strong>dataset_fields.md</strong> — dataset schema (fields, types, descriptions).</li>
    <li><strong>calculated_fields.md</strong> — calculated field definitions and QuickSight formulas.</li>
    <li><strong>Q_prompts.md</strong> — all natural language prompts used with Amazon Q.</li>
    <li><strong>verified_answers.md</strong> — the Verified answers list and descriptions.</li>
    <li><strong>scenario_thread.md</strong> — scenario starter and thread.</li>
    <li><strong>data_story.md</strong> — final data story narrative and visuals list.</li>
    <li><strong>manifest_sample.json</strong> — example S3 manifest used to demonstrate the failed S3 dataset import.</li>
    <li><strong>screenshots/</strong> — folder with all screenshots referenced in <code>submission_document.docx</code>.</li>
  </ul>

  <hr>

  <h2>🛠️ How to Reproduce</h2>
  <ol>
    <li>Sign in to <strong>Amazon QuickSight Enterprise</strong> with <strong>Q enabled</strong>.</li>
    <li>Open the stock sample dataset: <strong>Student Enrollment Statistics</strong>.</li>
    <li>Follow dataset preparation, calculated fields, and analysis steps outlined in:
      <ul>
        <li><code>submission_document.docx</code></li>
        <li><code>calculated_fields.md</code></li>
        <li><code>Q_prompts.md</code></li>
      </ul>
    </li>
  </ol>

  <div class="screenshot">
    <img src="https://i.postimg.cc/47mRtSwg/07-student-type-calculated-field-png.png" alt="Calculated Field Example">
  </div>

  <hr>

  <h2>📊 Sample Visuals</h2>

  <div class="screenshot">
    <img src="https://i.postimg.cc/YhcBG8W5/09-visual-student-majors-by-year-initial-png.png" alt="Enrollment Trend">
  </div>

  <div class="screenshot">
    <img src="https://i.postimg.cc/dZsHrkJT/29-vis-courses-best-eval-png.png" alt="Course Evaluation">
  </div>

  <div class="screenshot">
    <img src="https://i.postimg.cc/rdwBXPBr/12-proportion-of-student-types-pie-png.png" alt="Student Type Distribution">
  </div>

  <hr>

  <h2>✅ Originality Statement</h2>
  <p>I confirm this submission is my <strong>original work</strong>.<br>
     Where official AWS/Udacity examples or documentation were referenced, they were used <strong>only for guidance</strong>, and are properly acknowledged.</p>

  <hr>

  <h2>📬 Contact</h2>
  <p>Pascal Esegemou Ekenya Fonjock<br>
     📧 Email: <a href="mailto:p.fonjock@gmail.com">p.fonjock@gmail.com</a></p>

  <footer>
    <p>&copy; 2025 Pascal Esegemou Ekenya Fonjock — Regional Community College QuickSight Project</p>
  </footer>

</body>
</html>
