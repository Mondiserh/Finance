#The user  should be allowed to choose which calculation they want to do. 
# The first output that the user sees when the program runs should look like this :
import math
print("--Bond to calculate the amount you'll have to pay on a home loan")
print("--Investment ti calculate the amount of interest you'll earn on interest.")
print("Choose between bond and investment ")
print("1- Investment")
print("2- Bond")
choose = int(input('Choice :'))
    
def get_investment(choose):
    deposit = int(input('Enter the amount you will like to deposit: '))
    interest_rate = int(input('Enter the interest rate: '))
    period= int(input('Enter the period years of investing:  '))
    print('Choose Simple interest or compound interest')
    print('1- Simple interest')
    print('2- Compound interest')
    choice = int(input('Choice :'))
    r=interest_rate / 100
    P=deposit
    t=period
    
    if choice == 1:
        A = P * (1 + r * t ) 
    elif choice == 2:
        A = P* math.pow((1+r),t)
    else: 
        print('Invalid choice')
        print('1- Simple interest')
        print('2- Compound interest')
        choice = int(input('Choice :'))
    return A,
def get_bond(choose):
    house_value= int(input("Enter Present value of the house: "))
    interest_rate = int(input('Enter the interest rate: '))
    period= int(input('Enter the period months to repay the bond:  '))
    n= period * 12
    i=interest_rate/1200
    P = house_value
    x = (i*P)/1 - math.pow ((1+i),(-n))
    total = round(x,2)
    return total

if choose == 1:
    print(f"R {get_investment(choose)}")
elif choose == 2:
    print(get_bond(choose))
else:
    print("Choose between bond and investment ")
    print("1- Bond")
    print("2- Investment") 
