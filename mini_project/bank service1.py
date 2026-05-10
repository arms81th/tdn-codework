# Bank Service System
def main():
    # Login Section
    print("=== Bank Service Login ===")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username == "admin" and password == "1234":
        print("\nLogin successful! Welcome to our banking service.")
        show_services()
    else:
        print("\nError: Invalid username or password. Please try again.")

def show_services():
    """Display available banking services"""
    print("\nAvailable Services:")
    print("1. Deposit Service")
    print("2. Transfer Service")
    print("3. Withdraw Service")
    print("4. Exit")

    while True:
        try:
            service = input("\nPlease select service (1-4): ").strip()

            if service == "1":
                deposit_service()
            elif service == "2":
                transfer_service()
            elif service == "3":
                withdraw_service()
            elif service == "4":
                print("\nThank you for using our banking service. Goodbye!")
                break
            else:
                print("Invalid selection. Please enter 1, 2, 3 or 4.")

        except ValueError:
            print("Please enter a valid number.")

def deposit_service():
    """Handle deposit operations"""
    print("\n--- Deposit Service ---")
    account_number = validate_input("Enter your account number: ", numeric=True)
    amount = validate_input("Enter deposit amount: ", numeric=True, min_value=0.01)
    print(f"\nSuccessfully deposited {amount} to account {account_number}")

def transfer_service():
    """Handle transfer operations"""
    print("\n--- Transfer Service ---")
    source_account = validate_input("Enter your account number: ", numeric=True)
    target_account = validate_input("Enter recipient account number: ", numeric=True)
    amount = validate_input("Enter transfer amount: ", numeric=True, min_value=0.01)
    print(f"\nSuccessfully transferred {amount} from {source_account} to {target_account}")

def withdraw_service():
    """Handle withdrawal operations"""
    print("\n--- Withdraw Service ---")
    account_number = validate_input("Enter your account number: ", numeric=True)
    amount = validate_input("Enter withdrawal amount: ", numeric=True, min_value=0.01)
    print(f"\nSuccessfully withdrew {amount} from account {account_number}")

def validate_input(prompt, numeric=False, min_value=None):
    """Validate user input with error handling"""
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                raise ValueError("Input cannot be empty")

            if numeric:
                value = float(value)
                if min_value is not None and value < min_value:
                    raise ValueError(f"Amount must be at least {min_value}")
                return value
            return value

        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

if __name__ == "__main__":
    main()
