
import sys
import random
import string
from credentials import Credentials
from credentials import User

def create_credential(sname, fname, lname, password):
    '''
    Function to create a new user credentials
    '''
    new_credential = Credentials (sname, fname, lname,password)
    return new_credential



def save_credential(credential):
    '''
    Funtion to save the credential
    '''
    credential.save_credential()


def delete_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()


def find_credential(site_name):
    '''
    Function to find a credential
    '''
    return Credentials.find_by_account_name(site_name)


def check_existing_credentials(account_name):
    '''
    Function to check whether a credential exists
    '''
    return Credentials.credential_exist(account_name)


def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()



#Users funtions
def create_user(username, psswrd):
    '''
    Function to create a new user credentials
    '''
    new_user = User(username, psswrd)
    return new_user


def save_users(user):
    '''
    Funtion to save the credential
    '''
    user.save_users()


def main():
  print("Helllo,Welcome to Pasword Manager.Please input your name?")
  user_name = input("Your name: ")
  print("\n")

  while True:
    print(f"Hello {user_name},\n Please use these short codes to sign-up or log-in")
    print('\n')
    print("lg - log into your account")
    print("ca - create an account")
    print('\n')
    s_code = input("Short_Code:").lower()

    if s_code == 'ca':
      print("Enter user_name")
      fuser_name = input()

      print("Enter password")
      fpassword = input()




      print("Account creation successful")
      print("please proceed to log_in ")

      print('Enter your user_name:')
      user_name = input()
      print('Enter your password: ')
      password = input()

      if user_name == fuser_name and password == fpassword:
        print('LOG-IN SUCCESSFUL')
        print('\n')
        
        while True:
          print('Use these short codes: sc- Save existing credentials,cc - Create new credentials,dc - display credentials, fc - Find a credential, del - delete credentials, ex-exit the account')

          short_code = input().lower()

        if short_code == 'cc':
            print("New Credentials")
            print("-"*10)

            print("Site Name...")
            sname = input("Site Name: ")

            print("First Name")
            fname = input("")

            print("Last Name....")
            lname = input()

            print("Would you prefer a generated password?, type yes/no")
            password = input().upper()
            if password == 'YES':
                            print("Specify length of password?")
                            password_length = int(input())
                            chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
                            my_pass = "".join(random.choice(chars) for i in range(password_length))
                       
            elif password == 'NO':
                            print("Enter your preferred password:")
                            password = input()

            else:
                            print("Input is not recognised")
            save_credential(create_credential(sname, fname, lname, password)) #Create and save credentials
            print('\n')
            print('-'*30)
            print(f"New Credential {fname} {lname} created" )
            print('-'*30)
            print('\n')


        elif short_code == 'sc':
          print("Save Existing credentials")
          print("-"*10)

          print("Site Name...")
          sname = input()

          print("First Name")
          fname = input()

          print("Last Name")
          lname = input()

          print("Password")
          password = input()

                        
                    
          save_credential(create_credential(sname, fname, lname, password)) #Create and save credentials
          print('\n')
          print(f"{sname} credentials saved")
          print('\n')


        elif short_code == 'dc':
                        if display_credentials():
                            print("Here is a list of all you credentials")
                            print('\n')

                            for credential in display_credentials():
                                print(f"{credential.account_name}")
                                print("-"*30)
                                print(f"Username: {credential.first_name} {credential.last_name}")
                                print(f"Password: {credential.user_password}")
                                print('\n')

                        else:
                            print('\n')
                            print("You don't seem to have any credentials saved yet")
                            print('\n')

        elif short_code == 'fc':
                        print("Please enter the site name you want to search for")

                        search_site = input("Site Name: ")
                        if check_existing_credentials(search_site):
                            search_site = find_credential(search_site)
                            print(f"{search_site.first_name} {search_site.last_name}")
                            print("-"*20)

                            print(f"Password.....{search_site.user_password}")

                        else:
                            print("These credentials do not exist")
                            print('\n')

        elif short_code == 'del':
                        print("Please enter the name name of the site you want to delete")
                        site_delete = input()
                        if check_existing_credentials(site_delete):
                            site_delete = find_credential(site_delete)
                            delete_credential(site_delete)

                            print("Credentials deleted successfully")

                        else:
                            print("Credentials do not exist")


        elif short_code == "ex":
                        print("Thank you")
                        print('\n')
                        print('-'*20)
                        break
        else:
                        print("Please retry")

      else:
                print("Invalid login details")
                print('\n')

    elif s_code == 'lg':
            print("Please Enter your name")
            inputname = input()

            print("Enter Your Password")
            inputpass = input()

            print("The login details are non-existent. Please create an account before you can login")
            print('\n')
    
if __name__ == '__main__':
    
    main()
        

    




if __name__ == '__main__':
    
    main()