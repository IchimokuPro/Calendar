import calendar

def display_calendar(year):
    cal = calendar.TextCalendar(calendar.SUNDAY)  # Create a TextCalendar instance starting from Sunday
    for month in range(1, 13):  # Loop through each month
        month_name = calendar.month_name[month]
        month_calendar = cal.formatmonth(year, month)
        month_calendar_lines = month_calendar.split('\n')[2:]  # Exclude the first two lines
        month_calendar = '\n'.join(month_calendar_lines)
        
        print(f"\n{month_name} {year}")  # Display the month name and year
        print(month_calendar)  # Display the calendar for the month

def main():
    try:
        year = int(input("Enter the year: "))
        display_calendar(year)
    except ValueError:
        print("Please enter a valid year.")

if __name__ == "__main__":
    main()
