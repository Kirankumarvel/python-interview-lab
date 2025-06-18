while True:
    try:
        num = int(input("Enter a number (or type 'exit' to quit): "))
        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")
    except ValueError:
        user_input = input("Invalid input. Type 'exit' to quit or press Enter to try again: ")
        if user_input.strip().lower() == 'exit':
            break