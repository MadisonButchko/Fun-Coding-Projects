def generate_paystub():
    name = input("Enter your name: ")
    hourly_wage = float(input("Enter your hourly wage: "))
    hours_worked = float(input("Enter the number of hours you worked this week: "))

    weekly_salary = hourly_wage * hours_worked
    estimated_taxes = 0.10 * weekly_salary
    net_salary = weekly_salary - estimated_taxes

    print("--- Your Paystub ------")
    print(f"Name: {name}")
    print(f"Weekly Salary (before taxes): ${weekly_salary:.2f}")
    print(f"Estimated Taxes (10%): ${estimated_taxes:.2f}")
    print("-------------------")
    print(f"Net Salary (after taxes): ${net_salary:.2f}")

# Run the paystub generator
generate_paystub()
