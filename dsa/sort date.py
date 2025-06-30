from datetime import datetime
def sorted_date(dates):
    return sorted(dates, key=lambda date: datetime.strptime(date, "%d-%m-%Y"))

# Example usage
if __name__ == "__main__":
    dates = ["12-05-2023", "01-01-2022", "15-08-2021"]
    sorted_dates = sorted_date(dates)
    print("Sorted Dates:", sorted_dates)

