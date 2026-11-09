import csv

FIELDNAMES = ["Name", "Age", "Gender", "Rating", "Comments"]

# Survey data
survey_data = [
    {"Name": "Ali", "Age": 25, "Gender": "Male", "Rating": 4, "Comments": "Good service"},
    {"Name": "Sara", "Age": 22, "Gender": "Female", "Rating": 5, "Comments": "Excellent!"},
    {"Name": "Ahmed", "Age": 30, "Gender": "Male", "Rating": 3, "Comments": "Average experience"},
]


def save_survey(data, filename="survey_data.csv"):
    """Save a list of survey answers (dictionaries) to a CSV file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(data)


def average_rating(data):
    """Return the average rating of all survey answers."""
    return sum(row["Rating"] for row in data) / len(data)


def main():
    save_survey(survey_data)
    print("Survey data saved to 'survey_data.csv' ✅")
    print(f"Average rating: {average_rating(survey_data):.1f} / 5")


if __name__ == "__main__":
    main()
