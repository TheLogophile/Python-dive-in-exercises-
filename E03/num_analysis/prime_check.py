def is_prime(user_number):
    if len([i for i in range(2,user_number) if not user_number%i]) == 0:
        return True
    else:
        return False

