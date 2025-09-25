import csv


# Survey data
survey_data = [
    {"Name": "Ali", "Age": 25, "Gender": "Male", "Rating": 4, "Comments": "Good service"},
    {"Name": "Sara", "Age": 22, "Gender": "Female", "Rating": 5, "Comments": "Excellent!"},
    {"Name": "Ahmed", "Age": 30, "Gender": "Male", "Rating": 3, "Comments": "Average experience"}
]

# CSV file save
with open("survey_data.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Age", "Gender", "Rating", "Comments"])
    writer.writeheader()
    writer.writerows(survey_data)

print("Survey data 'survey_data.csv' file saved✅")
