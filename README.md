# PLP Python Week 7 — File Handling and CSV Reports

- `my_notes.py`: Writes initial notes, appends an extra note, prints each line without extra blank lines, and counts total lines.
- `my_notes.txt`: Text file containing the four notes written and appended by `my_notes.py`.
- `report_builder.py`: Reads learner scores from `hubs.csv` with `FileNotFoundError` handling and generates `report.txt`.
- `hubs.csv`: Input CSV dataset containing learner names, hubs, and scores.
- `report.txt`: Generated summary report showing total learners, passed, failed, and average score.
- `README.md`: Project overview, file descriptions, and answer to the Question 1 mode question.

If you changed `"a"` to `"w"` in Question 1, opening `my_notes.txt` for the fourth note would erase the first three lines instead of appending to them, leaving only `"I added this later"` in the file and changing the line count from 4 to 1.
