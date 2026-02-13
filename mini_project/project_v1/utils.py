def validate_amount(user_input: str):
    """
    Convert string to float, check strictly > 0 (not >= 0)
    Rationale: $0.00 expense has no semantic meaning; only positive amounts are valid

    Return Contract (STRICT):
    - (True, float_value): float_value already validated > 0, no rounding, ready for storage
    - (False, error_string): error_string is non-empty string describing exact error

    IMPORTANT: Wrap float() in try/except to catch ValueError
    - ValueError from float() conversion must be caught here, never bubble up

    Usage pattern: success, result = validate_amount(user_input)
                  if not success: print(result); continue

    Consistency: Do NOT mix return types. Always (bool, value_or_msg) tuple.

    """

    try:
        float_input = float(user_input)
    except ValueError:
        return (False, "Invalid amount. Enter a positive number.")

    if float_input > 0:
        return (True, float_input)
    else:
        return (False, "Amount must be positive.")


def validate_description(user_input: str):
    """
    Check non-empty, strip whitespace with .strip()
    If .strip() results in empty string → reject
    Returns: (True, string_description) OR (False, error_message_string)
    Usage pattern: success, result = validate_description(user_input)
                  if not success: print(result); continue
    Consistent unpacking everywhere.
    """
    result: str = user_input.strip()

    if result == "":
        return (False, "Description cannot be empty.")
    else:
        return (True, result)


def format_currency(amount: float):
    """`
    Convert float to string "$XX.XX" with exactly 2 decimal places
    Use f-string or .format() with precision specifier
    Example: format_currency(50.0) → "$50.00"
    Returns: "$50.00"
    """

    return f"${amount:.2f}"


