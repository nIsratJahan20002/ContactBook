def validate_name(name):
    if not name.isalpha():
        raise ValueError("The contact’s name must be a string.")

def validate_phone(phone):
    if not phone.isdigit():
        raise ValueError("The phone number must be an integer.")
