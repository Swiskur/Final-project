import random
def random_password():

    options = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*')
    generated_password = ''
    for i in range(12):
        generated_password += random.choice(options)


    return generated_password
