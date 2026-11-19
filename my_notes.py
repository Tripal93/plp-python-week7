# Write three notes to a new file
with open("my_notes.txt", "w") as f:
    f.write("Python is fun\n")
    f.write("Files are useful\n")
    f.write("Week 7 is going well\n")

# Add a fourth note WITHOUT erasing the first three
with open("my_notes.txt", "a") as f:
    f.write("I added this later\n")

# Read the file back and print each line with no blank lines between
print("--- My notes ---")
with open("my_notes.txt", "r") as f:
    for line in f:
        print(line.rstrip("\n"))

# Count the lines
with open("my_notes.txt", "r") as f:Python is fun
Files are useful
Week 7 is going well
I added this later
    lines = f.readlines()
print("Total lines:", len(lines))--- My notes ---
Python is fun
Files are useful
Week 7 is going well
I added this later
Total lines: 4name,hub,score
Amina,ASAL,82
Brian,NENAP,45
Fatuma,ASAL,90
Kevin,TCDM,61import csv

try:
    with open("hubs.csv", "r") as f:
        rows = list(csv.DictReader(f))
except FileNotFoundError:
    print("hubs.csv not found")
    rows = []

total = 0
passed = 0

for row in rows:
    score = int(row["score"])
    total += score
    if score >= 50:
        passed += 1

failed = len(rows) - passed
average = round(total / len(rows), 1)

with open("report.txt", "w") as f:
    f.write("LEARNER REPORT\n")
    f.write("Total learners: " + str(len(rows)) + "\n")
    f.write("Passed: " + str(passed) + "\n")
    f.write("Failed: " + str(failed) + "\n")
    f.write("Average score: " + str(average) + "\n")

print("Report written to report.txt")
Halima,NENAP,38LEARNER REPORT
Total learners: 5
Passed: 3
Failed: 2
Average score: 63.2
