def student_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    elif score >= 50:
        return 'E'
    else:
        return 'F'

def main():
    try:
        score = float(input("Enter the student's score: "))
        if score < 0 or score > 100:
            print("Score must be between 0 and 100.")
        else:
            grade = student_grade(score)
            print("The student's grade is:", grade)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()




