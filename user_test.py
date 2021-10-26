import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestUsers(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
      # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("yvonne","Njiiri","Sherryl","Jamlick12") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"James")
        self.assertEqual(self.new_user.last_name,"Muriuki")
        self.assertEqual(self.new_user.username,"0712345678")
        self.assertEqual(self.new_user.password,"Jamlick12")


    if __name__ == '__main__':
         unittest.main

    def test_save_user(self):
        '''
        test_save_user test case to test if the contact object is saved into
         the contact list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.user_list),1)

if __name__ ==  '__main__':
    unittest.main()