# Student Grade Management System

A simple Python project I made for fun to practise working with dictionaries, lists, functions, loops, and user input.

It runs in the terminal, stores student grades, calculates averages, and prints a class summary.

## Features

- Enter multiple students with three subject grades each.
- Check whether entered scores are between 0 and 100.
- Add a student through the `add_student()` function.
- Calculate individual student averages.
- Convert averages into letter grades.
- Display a student's grades, average, and letter grade.
- Find the student with the highest average.
- Calculate the class average.
- Show passing and failing student counts and percentages.

## Requirements

- Python 3
- No additional packages required — the project uses Python's built-in `statistics` module.

## How to Run

1. Download the Python file or clone this repository.
2. Open a terminal in the folder containing the file.
3. Run:

   ```bash
   python student-grade-management-system.py
   ```

   If your system uses `python3`, run:

   ```bash
   python3 student-grade-management-system.py
   ```

4. Enter the number of students, followed by each student's name and three integer scores.

## Important: Update the Placeholder Names Before Running

Some example function calls use `NAME` as a placeholder. Before running the script, replace these placeholders with the actual student names you plan to enter.

For example, change:

```python
display_students(NAME)
```

to:

```python
display_students("alice")
```

Then make sure you enter `alice` when the program asks for student names.

Names must match exactly, including capitalization. If an example call looks up a name that you haven't entered, the program will stop with a `KeyError`.

Check every example student lookup, not just `display_students()`. You can use different names in different calls, as long as those students exist in the data you entered.

## Example Student Report

For a student named `alice` with scores of 80, 85, and 90, the student report looks like:

```text
Name: alice
Grades:[80][85][90]
Average: 85.0
Letter grade: B
```

## Grading

The current letter-grade conditions are:

| Average | Letter grade |
|---------|--------------|
| 90 or higher | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| Anything else | F |

These are the conditions currently written in the code. Decimal averages between the listed ranges, such as 89.5, currently fall through to F. Fixing these boundaries is a planned improvement.

The summary uses a separate pass/fail threshold:

- Pass: average of 50 or higher
- Fail: average below 50

This means the summary's pass/fail result is not the same as the letter-grade classification.

## How It Works

Student data is stored in a dictionary, with each student's name as the key and a list of grades as the value:

```python
{
    "aarav":,[78][85][90]
    "alice":[80][85][90]
}
```

Functions handle adding students, calculating averages, converting grades, and displaying results.

Data is stored only while the program runs. It is not saved when the program closes.

## Known Limitations

This is a learning project, so there are still a few rough edges:

- Inputs must be integers; non-numeric input is not handled.
- Out-of-range scores display an error but do not prompt for a replacement.
- Student names must match exactly, including capitalization.
- Entering an existing name overwrites that student's grades.
- The letter-grade boundaries need adjustment for decimal averages.
- The example calls depend on specific student names.
- Some summary lines print `None` because they print the result of functions that already display their own output.
- The student counter can become inaccurate if a name is overwritten.

## Possible Improvements

- Add an interactive menu.
- Improve input validation and retry invalid entries.
- Fix the decimal letter-grade boundaries.
- Remove hard-coded student lookups.
- Support a custom number of subjects.
- Save and load student records.
- Add options to edit or delete students.
- Clean up the summary output and student count.

## About

Made for fun as a Python practice project. Not intended to be a production-ready school management system.
