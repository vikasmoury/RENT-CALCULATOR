def calculate_rent(rent_amount, utilities, lease_duration, security_deposit, other_expenses):
    # Step 1: Calculate total monthly cost
    total_monthly_cost = rent_amount + utilities

    # Step 2: Calculate total cost for lease duration
    total_lease_cost = total_monthly_cost * lease_duration

    # Step 3: Calculate total initial cost including security deposit and other expenses
    total_initial_cost = total_lease_cost + security_deposit + other_expenses

    return total_monthly_cost, total_lease_cost, total_initial_cost

def main():
    # Define the variables (example values)
    rent_amount = float(input("Enter the monthly rent amount: "))
    utilities = float(input("Enter the monthly utilities amount: "))
    lease_duration = int(input("Enter the lease duration in months: "))
    security_deposit = float(input("Enter the security deposit amount: "))
    other_expenses = float(input("Enter any other one-time expenses: "))

    # Calculate costs
    total_monthly_cost, total_lease_cost, total_initial_cost = calculate_rent(
        rent_amount, utilities, lease_duration, security_deposit, other_expenses
    )

    # Display the results
    print("\nRent Calculator Summary:")
    print(f"Total Monthly Cost: ₹{total_monthly_cost:.2f}")
    print(f"Total Cost for Lease Duration: ₹{total_lease_cost:.2f}")
    print(f"Total Initial Cost (including security deposit and other expenses): ${total_initial_cost:.2f}")

if __name__ == "__main__":
    main()
