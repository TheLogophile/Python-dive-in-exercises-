# “Write a function that takes the information of a class and checks whether a student named Alireza exists among its students.”

def alireza_check(**kwargs):
    try:
        if "Alireza" in kwargs["students"]:
                return True
        else:
                return False
    except:
        print("There's no 'student' list")


print(alireza_check(
    class_name = ['Python 101'],
    teacher = ['Mr. Rezaei'],
    students = ['Alireza', 'Sara', 'Mina', 'Omid', 'Hassan'],
    schedule = ['Monday 10:00-12:00', 'Wednesday 10:00-12:00']
    ))