# from types import Expense
from utils import validate_amount, validate_description, format_currency

Expense = dict[str, float | str]


def show_menu():
    """
    Display menu options ONLY
    Does NOT accept input
    Does NOT validate anything
    Prints: "1) Add | 2) View | 3) Exit"
    """

    print("\n\n\n1) Add | 2) View | 3) Exit")


def get_menu_choice():
    """
    IMPORTANT: Contains internal validation loop
    Does NOT display menu (menu displayed by caller)
    Does NOT rely on main loop for error recovery

    String validation strategy (WHY NOT int() with try/except?):
    - String membership test {'1','2','3'} avoids exception control flow
    - Exceptions are for exceptional cases, not normal validation
    - String set membership is cleaner: faster lookup, clearer intent
    - No hidden exception handling in validation logic

    Pattern:
      while True:
          read input as string, strip whitespace
          validate using: if user_input.strip() in {"1", "2", "3"}:
          if valid → convert to int and return
          else → print error message, loop continues
    Returns: int (1, 2, or 3) — ALWAYS valid
    Main loop will never see invalid choice
    """

    while True:
        user_input = input("Enter choice (1/2/3): ").strip()

        if user_input in {"1", "2", "3"}:
            return int(user_input)
        else:
            print("Invalid Input!")


def add_expense(expenses: list[Expense]):
    # Prompt amount → validate → prompt description → validate → append to list

    success_amount, amount_or_error = validate_amount(input("Enter Amount: "))
    if not success_amount:
        print(amount_or_error)
        return

    success_desc, desc_or_error = validate_description(input("Enter Description: "))
    if not success_desc:
        print(desc_or_error)
        return

    expenses.append({"amount": amount_or_error, "description": desc_or_error})
    print("Expense added!")


def view_expenses(expenses: list[Expense]):
    """
    Display all expenses or "No expenses" message
    When displaying each expense, call format_currency() for amount
    Example format: "$50.00 - Lunch" (never inline f-string amounts)
    Call calculate_total(expenses) to get sum
    Display total using: "Total: " + format_currency(total)
    Display total with currency formatting
    """

    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    for i, exp in enumerate(expenses, start=1):
        print(f"{i}) {format_currency(float(exp['amount']))} - {exp['description']}")

    total = calculate_total(expenses)
    print(f"Total: {format_currency(total)}")


def calculate_total(expenses: list[Expense]) -> float:
    # Sum all "amount" values from expenses list
    #
    # PURE FLOAT FUNCTION (Strict Rules):
    # - No f-strings
    # - No rounding (format_currency handles precision)
    # - No string return
    # - No print statements
    # - No side effects (read-only on expenses list)
    # - Returns: raw float only
    #
    # Example: total = sum(exp["amount"] for exp in expenses)
    #
    # Architectural principle: Logic functions remain pure.
    # Formatting happens in view layer only (view_expenses + format_currency).
    #
    # Used only by view_expenses().
    # Isolated for single responsibility and future unit testability.
    return sum(float(exp["amount"]) for exp in expenses)


def main():
    """
    Initialize expenses list, main loop
    Data shape constants (optional v1 discipline improvement):
      AMOUNT = "amount"
      DESCRIPTION = "description"
    Pattern:
      expenses = []
      while True:
          show_menu()  # Display first
          choice = get_menu_choice()  # Get validated input
          if choice == 1: add_expense(expenses)
          elif choice == 2: view_expenses(expenses)
          elif choice == 3: break  # Exit cleanly
    """

    expenses: list[Expense] = []

    while True:
        show_menu()  # Display menu
        choice = get_menu_choice()  # Validates internally, returns int (1-3)
        if choice == 1:
            add_expense(expenses)
        elif choice == 2:
            view_expenses(expenses)
        elif choice == 3:
            break


if __name__ == "__main__":
    main()
