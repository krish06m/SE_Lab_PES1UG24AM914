import re

_DIGITS = re.compile(r"[0-9]+")

def _to_int(part):
    """Returns the int for a string of digits, or None if it is not valid."""
    part = part.strip()
    if not _DIGITS.fullmatch(part):
        return None
    try:
        return int(part)
    except ValueError:  # e.g. number too long for Python to convert
        return None

def clean_dish_name(name):
    """
    Removes the chef's-special markers (*, #, ~) and title-cases the name.
    Returns None if the input is not a string or is empty after cleaning.
    """
    if not isinstance(name, str):
        return None
    name = name.strip()
    for ch in ['*', '#', '~']:
        name = name.replace(ch, '')
    name = name.strip()
    if not name:
        return None
    return name.title()

def parse_item_prices(text):
    """
    Parses comma-separated prices into a list of ints.
    Returns None if the input is not a string or any price is not a whole number.
    """
    if not isinstance(text, str):
        return None
    prices = []
    for part in text.split(','):
        price = _to_int(part)
        if price is None:
            return None
        prices.append(price)
    return prices

def split_amount(text):
    """
    Splits 'TOTAL/PEOPLE' into the amount each person pays.
    Returns None if the input is malformed, not whole numbers, or people is zero.
    """
    if not isinstance(text, str):
        return None
    parts = text.split('/')
    if len(parts) != 2:
        return None
    total = _to_int(parts[0])
    people = _to_int(parts[1])
    if total is None or people is None or people == 0:
        return None
    return total // people

def main():
    print("==== Running clean_dish_name ====")
    value = input("Enter a dish name from the menu (e.g. *paneer tikka*): ")
    print("Dish name:", clean_dish_name(value))

    print("\n==== Running parse_item_prices ====")
    value = input("Enter item prices separated by commas (e.g. 250,180,320): ")
    print("Item prices:", parse_item_prices(value))

    print("\n==== Running split_amount ====")
    value = input("Enter the bill and number of people as TOTAL/PEOPLE (e.g. 1200/4): ")
    print("Each person pays:", split_amount(value))

if __name__ == "__main__":
    main()
