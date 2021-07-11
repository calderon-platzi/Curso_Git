from proyecto1.passwordGit.generatePassword import generate_password
# import passwordGit

def run():
    password = generate_password()
    print('Your new password is: ' + password)


if __name__ == '__main__':
    run()