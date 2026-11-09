# Save Survey Data to CSV

A small Python script that saves survey answers to a CSV file using Python's built-in
`csv` module, and prints the average rating.

## Features
- Stores survey answers (name, age, gender, rating, comments) as a list of dictionaries
- Saves them to `survey_data.csv` with a header row
- Prints the average rating
- Uses UTF-8, so names in any language are saved correctly

## Sample output
The script creates `survey_data.csv`:

| Name | Age | Gender | Rating | Comments |
|------|-----|--------|--------|----------|
| Ali | 25 | Male | 4 | Good service |
| Sara | 22 | Female | 5 | Excellent! |
| Ahmed | 30 | Male | 3 | Average experience |

## How to run
```bash
python save_survey_data.py
```
Requires Python 3.x. No extra libraries needed.
