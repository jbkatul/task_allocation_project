from django.test import TestCase

# Create your tests here.
# checking voting eligibility
def check_voting_eligibility(age):
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

# Example usage:
user_age = int(input("Enter your age: "))
result_message = check_voting_eligibility(user_age)
print(result_message)