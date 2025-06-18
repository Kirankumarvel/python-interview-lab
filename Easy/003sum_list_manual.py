def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    sample_list = [int(x) for x in user_input.strip().split()]
    print("List:", sample_list)
    print("Sum of list elements:", sum_list(sample_list))
