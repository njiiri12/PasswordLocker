class User:
    """
    Class that generates new instances of users
    """
    user_list =[]

    def __init__(self,first_name,last_name,password):

        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

      

new_user = User("Yvonne","Njiiri","yves012")

print("First Name?")
first_name = input()
print("Last Name?")
last_name = input()
print("Password?")
password = input()

user_name = first_name+ ""+last_name
print(user_name,password)
print("\n")

  
print(new_user.last_name,new_user.first_name,new_user.password)


class Credentials :
    '''
    class that creates  users_accounts credentials
    '''

    credentials_list = [] 

    def __init__(self, account_name, first_name, last_name, user_password):
        self.account_name = account_name
        self.first_name = first_name
        self.last_name = last_name
        self.user_password = user_password


    @classmethod
    def save_credential(self):
        '''
        Method to save a new object in the credential list
        '''
        Credentials.credentials_list.append(self)


    @classmethod
    def delete_credential(self):
        '''
        Method to delete a credential from the list
        '''
        Credentials.credentials_list.remove(self)

    

    @classmethod
    def find_by_account_name(cls, account_name):
        '''
        Method that takes in a site name and returns the credentials
        '''
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential



    @classmethod
    def credential_exist(cls, account_name):
        '''
        Method that checks if a credential actually exists
        '''
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return True

        return False