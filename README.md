# Student Performance Management System

A terminal-based Python application to manage student records, enter scores, and generate performance reports. Data is saved in a JSON file, so records stay between runs.

## Features

- **Register students** with ID, name, phone number, email, and guardian details
- **Input validation** for names, 10-digit phone numbers, emails, IDs, and scores (0-100)
- **Enter and update scores** for Python, Mathematics, and Physics
- **View all students** or **search** by student ID
- **Update details** such as name, phone number, and email (student or guardian)
- **Delete students** with a YES/NO confirmation
- **Individual report card** with total score, percentage, highest and lowest subject, and a performance remark
- **Class statistics**: class average, highest and lowest scorer, subject-wise averages, and performance distribution

## Tech Used

- Python 3.12 or newer (built and tested on 3.14)
- `json` module for data storage

## How to Run

1. Make sure Python 3.12+ is installed.
2. Clone the repository:
   ```
   git clone https://github.com/prrix999/student-management-system.git
   cd student-management-system
   ```
3. Run the program:
   ```
   python student_management_system.py
   ```

`students_record.json` already contains sample test data. Delete it if you want to start fresh, and the program will create a new one.

## Menu Options

| Option | What it does |
|--------|--------------|
| 1 | Register a new student |
| 2 | Enter or update student marks |
| 3 | View all students |
| 4 | Search a student by ID |
| 5 | Update student details |
| 6 | Delete a student |
| 7 | Individual performance analysis |
| 8 | Class performance statistics |
| 9 | Exit |

## Performance Remarks

| Percentage | Remark |
|------------|--------|
| 90 and above | Outstanding |
| 80 - 89 | Excellent |
| 70 - 79 | Very Good |
| 60 - 69 | Good |
| 50 - 59 | Average |
| 40 - 49 | Below Average |
| Below 40 | Need Improvement |

## Future Improvements

- Remove repeated code by looping over subjects
- Let users add or remove subjects
- Add a way to go back at any prompt
- Split the code into multiple modules

## Author

Prionjit