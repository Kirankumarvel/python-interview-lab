#Using List Comprehension
def count_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return len([c for c in s.lower() if c in vowels])

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    print("Number of vowels:", count_vowels(user_input))