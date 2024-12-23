import random

def generate_phone():
    """Генерирует случайный номер телефона в формате +7 (XXX) XXX-XX-XX."""
    return f"+7 ({random.randint(100, 999)}) {random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(10, 99)}"

def generate_email():
    """Генерирует случайный email-адрес в формате *@*.*."""
    domains = ["example.com", "test.net", "gmail.com", "company.org"]
    username = "".join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(random.randint(5, 10)))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def generate_name():
    """Генерирует случайное имя."""
    first_names = ["John", "Jane", "Alice", "Bob", "Peter", "Eva", "Tom", "Mary", "Michael", "Anna"]
    last_names = ["Doe", "Smith", "Pan", "Green", "Hanks", "Marley", "Brown", "White", "Black", "Lee"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_correct_line():
    """Генерирует строку с правильным форматом телефона и email."""
    name = generate_name()
    phone = generate_phone()
    email = generate_email()
    return f"{name}, phone: {phone}, email: {email}"

def generate_incorrect_line(error_type):
    """Генерирует строку с одним из вариантов неправильного формата."""
    name = generate_name()
    if error_type == "no_phone":
        email = generate_email()
        return f"{name}, email: {email}"
    elif error_type == "no_email":
        phone = generate_phone()
        return f"{name}, phone: {phone}"
    elif error_type == "wrong_phone":
        phone = f"+3 ({random.randint(100, 999)}) {random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(10, 99)}"
        email = generate_email()
        return f"{name}, phone: {phone}, email: {email}"
    elif error_type == "wrong_email":
        phone = generate_phone()
        email = f"wrong.email@"
        return f"{name}, phone: {phone}, email: {email}"
    elif error_type == "no_phone_no_email":
        return f"{name}"
    else:
        return f"{name}, phone: {generate_phone()}, email: wrongemail"


def generate_file(correct_lines, incorrect_lines, filename="file.txt"):
    """Генерирует файл с заданным количеством правильных и неправильных строк."""
    with open(filename, "w") as f:
        for _ in range(correct_lines):
            f.write(generate_correct_line() + "\n")

        error_types = ["no_phone", "no_email", "wrong_phone", "wrong_email", "no_phone_no_email"]
        for _ in range(incorrect_lines):
            f.write(generate_incorrect_line(random.choice(error_types)) + "\n")

if __name__ == "__main__":
    correct_lines_count = 100
    incorrect_lines_count = 10
    generate_file(correct_lines_count, incorrect_lines_count)
    print(f"Файл file.txt сгенерирован с {correct_lines_count} правильными и {incorrect_lines_count} неправильными строками.")