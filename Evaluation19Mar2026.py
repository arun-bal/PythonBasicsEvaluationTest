class Eval:
    @staticmethod
    def check_odd_or_even(num):
        if num % 2 == 0:
            print("Given number is Even")
        else:
            print("Given number is Odd")

    @staticmethod
    def check_citizen_eligibility(age):
        if age >= 18:
            print("Citizen Eligible to vote")
        else:
            print("Citizen not eligible to vote")

    @staticmethod
    def check_a_number(num):
       return True if num >20 and num<50 and num%5==0 else False

Eval.check_odd_or_even(13)
Eval.check_citizen_eligibility(20)
if Eval.check_a_number(25):
    print("The number is between  20 and 50 and must be divisible by 5")
else:
    print("The number is not between  20 and 50 and must be divisible by 5")

## Right angle triangle with *
rows = 3
for i in range(1, rows + 1):
    print('* ' * i) #multiply a string with a number to repeat it.
