import unittest
from credentials import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the User class behaviours
    '''

    def setUp(self):
        # self.new_user = User("John","James", "jj0897") #Create user  object
        
        
        self.new_user = User("John","James","jj0897")
        


    def tearDown(self):
        '''
        Tear down method that does clean up after each test case has run
        '''
        User.user_list = []
        

    def test__init(self,first_name,last_name,password):
        '''
        Test to check whether the user objects are instantiated correctly
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def test_save_user(self):
        '''
        Test to check if the object is saved into the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_users(self):
        self.new_users.save_user()
        test_user = User("Yvonne", "Njiiri", "yves012")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)