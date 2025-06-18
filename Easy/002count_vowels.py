#Using a Loop
def count_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    print("Number of vowels:", count_vowels(user_input))