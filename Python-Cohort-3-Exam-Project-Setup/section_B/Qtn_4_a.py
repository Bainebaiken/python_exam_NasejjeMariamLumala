
# employee_name = (input('\nEnter the your name : '))
# salary = int(input('Enter the employee salary : '))
# net_bonus =salary + bonus 
# result=()
def calculate_bonus(salary, years_of_service):
    bonus = 0
    if years_of_service > 4:
        bonus = salary * 0.08
    elif years_of_service == 3:
        bonus = salary * 0.05
    return bonus

def main():
    while True:
        salary = float(input("Enter your  employee salary: "))
        years_of_service = int(input("Enter your years of service: "))
        bonus = calculate_bonus(salary, years_of_service)
        net_salary = salary + bonus
        print(f"Your bonus amount is: {bonus}")
        print(f"Your net salary amount is: {net_salary}")
        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != 'yes':
            break

if __name__ == "__main__":
    main()