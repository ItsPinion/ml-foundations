# Expense Tracker CLI

## 2. Problem Statement

This project develops a lightweight command-line expense tracking application designed for users who need quick, efficient expense logging without graphical overhead. The expense tracker solves the problem of manual expense management by providing an organized, accessible way to record and review spending in real-time.

**Who it's for:** Individuals seeking a simple, text-based tool for personal expense management; developers who value simplicity and control over bloated UI frameworks.

**Why CLI:** CLI offers superior efficiency for rapid data entry, minimal resource consumption, easy automation and scripting integration, and maintains full transparency of operations. For v1, we prioritize functionality and lean architecture over visual appeal.

---

## 3. Core Features (Version 1 Only)

**Minimal Essential Features:**

- **Add Expense:** Record a new expense with amount and description
- **View All Expenses:** Display logged expenses with total sum
- **Exit Program:** Clean exit

**Explicitly Excluded (v1):**

- Delete/edit expenses (add in Day 27)
- Timestamps (in-memory only, no file persistence v1)
- Confirmation prompts
- Data persistence between sessions (v1 is in-memory)
- Categories or tags
- Budget limits or alerts
- Charts, graphs, or visualizations

**Rationale:** Month 1 = core functionality only. Perfect ground for refactoring on Day 27.

---

## 4. Inputs / Outputs Definition

**User Inputs:**

- Menu choice (string, converted to int 1-3 with validation)
- Amount (string, converted to float, must be strictly positive: > 0)
- Description (string, non-empty)

**Note:** `input()` always returns string. All inputs must be validated and converted before use.

**System Outputs:**

- Menu: "1) Add | 2) View | 3) Exit"
- Expense list: "$50.00 - Coffee" (simple format)
- Total sum
- Success messages: "Expense added!"

**Error Handling:**

- Invalid input → "Please enter a valid choice"
- Negative amount → "Amount must be positive"
- Empty description → "Description required"

**Storage:** In-memory list only (no file I/O in v1)

---

## 5. Program Flow (Write as Steps)

1. **Startup:** Initialize empty expenses list
2. **Display Menu:** Show numbered options (Add, View, Exit)
3. **Get User Input:** Call `get_menu_choice()` which contains internal validation loop
4. **Validation Happens Inside get_menu_choice():**
   - Loop internally until valid input (1-3) is received
   - Print error message if invalid, continue prompting
   - Return int only when valid
5. **Route to Handler (main receives ONLY valid choice):**
   - Choice 1 → Call `add_expense(expenses)`
   - Choice 2 → Call `view_expenses(expenses)`
   - Choice 3 → Exit program
6. **Loop:** Return to step 2 until user chooses exit
7. **Exit:** Program ends (no save, data lost)

**Loop Pattern:**

```
expenses = []
while True:
    choice = get_menu_choice()  # Validates internally, returns int (1-3)
    if choice == 1:
        add_expense(expenses)
    elif choice == 2:
        view_expenses(expenses)
    elif choice == 3:
        break
```

**Key Design Principle:** Error handling for menu choice is INSIDE `get_menu_choice()`, NOT in main loop. Main loop is clean and only handles valid input.

---

## 6. Required Components

**Project Structure:**

```
mini_project/
├── __init__.py          # Makes directory importable (optional v1 discipline)
├── main.py              # Entry point, menu loop, feature routing
└── utils.py             # Input validation, amount formatting
```

**Note on **init**.py:** Not required for v1 CLI, but establishes modular discipline early. Allows future main.py to be imported cleanly.

**Component Responsibilities:**

- **main.py:** Menu display, user input loop, feature routing, expenses list management
- **utils.py:** Input validation, amount formatting, helper functions

**Design Principles:**

- Keep it simple (Month 1)
- No file I/O yet
- No class overhead
- No storage.py until persistence is needed
- All logic in main.py or utils.py
- Menu validation is OWNED by `get_menu_choice()` (internal loop, not main responsibility)
- Input validation (amount, description) is OWNED by utility validators
- Main loop remains clean and error-free
- Refactor on Day 27

---

## 6.5. Function Breakdown (Before Implementation)

**main.py Functions:**

```python
def show_menu():
    # Display menu options ONLY
    # Does NOT accept input
    # Does NOT validate anything
    # Prints: "1) Add | 2) View | 3) Exit"

def get_menu_choice():
    # IMPORTANT: Contains internal validation loop
    # Does NOT display menu (menu displayed by caller)
    # Does NOT rely on main loop for error recovery
    #
    # String validation strategy (WHY NOT int() with try/except?):
    # - String membership test {'1','2','3'} avoids exception control flow
    # - Exceptions are for exceptional cases, not normal validation
    # - String set membership is cleaner: faster lookup, clearer intent
    # - No hidden exception handling in validation logic
    #
    # Pattern:
    #   while True:
    #       read input as string, strip whitespace
    #       validate using: if user_input.strip() in {"1", "2", "3"}:
    #       if valid → convert to int and return
    #       else → print error message, loop continues
    # Returns: int (1, 2, or 3) — ALWAYS valid
    # Main loop will never see invalid choice

def add_expense(expenses):
    # Prompt amount → validate → prompt description → validate → append to list

def view_expenses(expenses):
    # Display all expenses or "No expenses" message
    # When displaying each expense, call format_currency() for amount
    # Example format: "$50.00 - Lunch" (never inline f-string amounts)
    # Call calculate_total(expenses) to get sum
    # Display total using: "Total: " + format_currency(total)
    # Display total with currency formatting

def calculate_total(expenses):
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

def main():
    # Initialize expenses list, main loop
    # Data shape constants (optional v1 discipline improvement):
    #   AMOUNT = "amount"
    #   DESCRIPTION = "description"
    # Pattern:
    #   expenses = []
    #   while True:
    #       show_menu()  # Display first
    #       choice = get_menu_choice()  # Get validated input
    #       if choice == 1: add_expense(expenses)
    #       elif choice == 2: view_expenses(expenses)
    #       elif choice == 3: break  # Exit cleanly

if __name__ == "__main__":
    main()
```

**Execution Guard:** `if __name__ == "__main__":` ensures modular execution. Code can be safely imported without auto-executing. Required for professional Python modules.

**Menu Ownership Principle (Refined):**

- `show_menu()` displays menu options, nothing else
- `get_menu_choice()` handles input + validation, no display
- Main loop calls both explicitly: first display, then validate
- Separation: display responsibility vs input responsibility

```python
while True:
    show_menu()          # Display menu
    choice = get_menu_choice()  # Get + validate choice
    # Route based on choice
```

**utils.py Functions:**

```python
def validate_amount(user_input):
    # Convert string to float, check strictly > 0 (not >= 0)
    # Rationale: $0.00 expense has no semantic meaning; only positive amounts are valid
    #
    # Return Contract (STRICT):
    # - (True, float_value): float_value already validated > 0, no rounding, ready for storage
    # - (False, error_string): error_string is non-empty string describing exact error
    #
    # IMPORTANT: Wrap float() in try/except to catch ValueError
    # - ValueError from float() conversion must be caught here, never bubble up
    #
    # Usage pattern: success, result = validate_amount(user_input)
    #               if not success: print(result); continue
    #
    # Consistency: Do NOT mix return types. Always (bool, value_or_msg) tuple.

def validate_description(user_input):
    # Check non-empty, strip whitespace with .strip()
    # If .strip() results in empty string → reject
    # Returns: (True, string_description) OR (False, error_message_string)
    # Usage pattern: success, result = validate_description(user_input)
    #               if not success: print(result); continue
    # Consistent unpacking everywhere.

def format_currency(amount):
    # Convert float to string "$XX.XX" with exactly 2 decimal places
    # Use f-string or .format() with precision specifier
    # Example: format_currency(50.0) → "$50.00"
    # Returns: "$50.00"
```

**Data Shape Explicitness (Optional v1 Discipline):**

Instead of hardcoding `"amount"` and `"description"` strings throughout, define constants in main.py (top of file):

```python
AMOUNT = "amount"
DESCRIPTION = "description"

# Usage in add_expense():
expense = {AMOUNT: amount, DESCRIPTION: description}
expenses.append(expense)

# Usage in calculate_total():
total = sum(exp[AMOUNT] for exp in expenses)
```

**Placement Note For v1:** Top of main.py is acceptable. For larger systems, consider separate `constants.py`. Month 1: keep it simple.

**Benefit:** Centralizes key names, prevents typo errors. Not required for v1 but good discipline.

**Total Calculation Strictness:**

`calculate_total()` does ONLY summation with no side effects:

- No rounding (formatting handles that)
- No print statements
- No modifications to expenses list
- Returns raw float
- Formatting happens in `view_expenses()` via `format_currency()`

**Consistency Commitment:** No class usage. Functional approach throughout. Full code will remain procedural in v1.

---

## 7. Data Storage Strategy

**Storage Method:** In-memory list (Month 1)

**Data Structure:**

```python
expenses = [
    {"amount": 50.00, "description": "Lunch"},
    {"amount": 25.50, "description": "Coffee"}
]
```

**Why Dict Instead of Tuple:**

- Named fields (`"amount"`, `"description"`) prevent positional ambiguity
- More readable: `exp["amount"]` vs `exp[0]` (clarity matters)
- Future extensibility: adding "timestamp" or "category" in v2 requires only `exp["timestamp"]`, no index changes
- Maintains SRP: each field has semantic meaning, not positional meaning

**Strategy:**

- List persists only during current session
- Data lost on exit (acceptable for Month 1)
- No file I/O complexity

**Float Precision Note:**
For v1, storing amounts as `float` is acceptable for CLI prototyping. In production systems, use `decimal.Decimal` for currency. This is v2+ consideration.

**Rounding Behavior (for awareness):**

- Float formatting via `f"${amount:.2f}"` handles all rounding
- Example: Input "50.999" → stored as 50.999 (float) → displayed as "$51.00"
- Example: Input "1000000.99" → stored as 1000000.99 → displayed as "$1000000.99"
- Precision loss can occur at large scales; this validates the Decimal note for v2

**Day 27 Upgrade:**
Add JSON persistence + delete/edit features

---

## 8. Verification Strategy (Testing Matrix)

**Architectural Testing (v1 Coverage):**

| Test Case               | Input                 | Expected Outcome                                    |
| ----------------------- | --------------------- | --------------------------------------------------- |
| Valid menu              | "1"                   | Returns int 1                                       |
| Valid menu              | "2"                   | Returns int 2                                       |
| Valid menu              | "3"                   | Returns int 3                                       |
| Invalid menu            | "4"                   | Reprints menu, loops                                |
| Invalid menu            | "abc"                 | Reprints menu, loops                                |
| Valid amount            | "50.00"               | Accepted, stored as 50.0                            |
| Valid amount            | "0.01"                | Accepted (smallest valid)                           |
| Valid amount (large)    | "1000000.99"          | Accepted, displayed as $1000000.99                  |
| Valid amount (rounding) | "50.999"              | Accepted, displayed as $51.00 (rounds up)           |
| Invalid amount          | "0"                   | Rejected: "Amount must be positive"                 |
| Invalid amount          | "-50"                 | Rejected: "Amount must be positive"                 |
| Invalid amount          | "abc"                 | Rejected: "Invalid amount. Enter a positive number" |
| Valid description       | "Lunch"               | Accepted                                            |
| Empty description       | ""                    | Rejected: "Description cannot be empty"             |
| Whitespace description  | " "                   | Rejected: "Description cannot be empty"             |
| Multiple expenses       | Add 3 items           | All stored, display shows all 3                     |
| View empty list         | View without expenses | Print "No expenses recorded yet"                    |
| Total calculation       | Add $50 + $25         | Display "Total: $75.00"                             |

**Manual Testing Approach:**

1. Run program, verify menu displays
2. Test each menu option (1, 2, 3) with valid input
3. Test invalid menu choices loop correctly
4. Add expense with valid amount + description
5. View all expenses and verify format
6. Add another expense, verify both display with indices 1) and 2)
7. Test invalid amounts (negative, zero, non-numeric)
8. Test invalid descriptions (empty, whitespace)
9. View when list is empty
10. Verify exit (choice 3) closes cleanly

**v1 is complete when:**

- ✓ User can add an expense (amount + description)
- ✓ User can view all expenses
- ✓ User can exit cleanly
- ✓ Input validation works (no negative amounts, no empty descriptions)
- ✓ Total sum displays correctly
- ✓ No crashes on bad input

**Testing approach:**

- Manual test: Add 3 expenses, verify display
- Test invalid inputs (negative, empty strings)
- Test menu navigation

---

## 8.5. Edge Case Behavior (Explicit)

**Empty List Scenario:**

- If user selects View with no expenses: print "No expenses recorded yet."

**Invalid Amount Input:**

- Input: "abc" for amount → print "Invalid amount. Enter a positive number."
- Input: "-50" for amount → print "Amount must be positive."
- Input: "0" for amount → print "Amount must be positive." (zero is not valid)
- Input: "0.00" for amount → print "Amount must be positive." (zero is not valid)
- Input: "50.00" for amount → accepted, stored as float 50.00

**Currency Display:**

- Store amounts as float
- Display each expense with index: `1) $50.00 - Lunch`
  - Index starts at 1 (user-friendly), not 0
  - Format: `index) $amount - description` (using hyphen `-` separator)
  - This indexing prepares for Day 27 delete-by-index feature
- Total sum also formatted with 2 decimals
- Consistent separator: always use `-` (hyphen), never use `—` (em-dash)
- Example view output:
  ```
  1) $50.00 - Lunch
  2) $25.00 - Coffee
  Total: $75.00
  ```

**Formatting Note on Precision:**
Precision control is centralized in `format_currency()` using `f"${amount:.2f}"`. Logic functions keep data raw (floats). Single source of truth for formatting.

**Empty Description:**

- Input: "" → print "Description cannot be empty."
- Input: " " (spaces only) → treat as empty, reject

**Invalid Menu Choice:**

- Input: "4" → print "Please enter a valid choice (1-3)"
- Input: "abc" → print "Please enter a valid choice (1-3)"

---

## 9. Implementation Deferred

No code written on Day 23.

Planning and architecture complete. Ready for Day 24 implementation.

---

## 10. Roadmap (Day 27+)

**Day 27 (v1.1):**

- Delete expenses by index
- JSON file persistence
- Timestamps for each expense
- Edit expense feature

**Day 30+ (v2):**

- Category-based filtering
- Monthly summaries
- Budget alerts
- CSV export
- SQLite backend

---

**Document Status:** Month 1 planning (realistic scope) complete. Ready for implementation.  
**Design Philosophy:** Simple > Correct > Fast. No file I/O. No classes. No premature optimization.  
**Last Updated:** February 12, 2026
