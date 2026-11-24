### Question: Accept a date in DD-MM-YYYY format and handle invalid dates

from datetime import datetime

dates = ["25-01-20226","30-10-2026"]

for date in dates:
    try:
        result = datetime.strptime(date, "%d-%m-%Y")
        print("Valid date:", result.date())

    except ValueError:
        print("Invalid date:", date)