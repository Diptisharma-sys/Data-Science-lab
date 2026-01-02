### 4. Writing and Reading JSON Data
### ● Stores student details (ID, name, and marks) in a JSON file
### ● Reads the JSON file and displays the student information
### ● Handles exceptions related to file access and JSON decoding

import json

students = [
    {"id": 1, "name": "Dipti", "marks": 85},
    {"id": 2, "name": "Ram", "marks": 78},
    {"id": 3, "name": "Sita", "marks": 90}
]

try:
    with open("students.json", "w") as file:
        json.dump(students, file)
    print("Data written to JSON file successfully")

    
    with open("students.json", "r") as file:
        data = json.load(file)
        
        print(f"{'id':<5} {'name':<10} {'marks':<5}")
        for data in students:
            print(f" {data['id']:<5} {data['name']:<10} {data['marks']:<5}")
except Exception as e:
    print("Error while writing file:", e)
