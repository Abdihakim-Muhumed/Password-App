import unittest
import pyperclip
from classes import User
from classes import Credential


class TestUser(unittest.TestCase):
    """TestUser class to test User methods/behaviours
    arg:
     unittest.Testcase:  Testcase class that provides test methods.
    """

    def setUp(self):
        '''set up method to run before every test'''
        self.new_user = User('Abdihakim','10203040')

    def tearDown(self):
        '''tearDown method to set User list to to 0'''
        User.users = []

    def test__init__(self):
        '''tets__init__ test case to check for proper object initialization'''
        self.assertEqual(self.new_user.userName,'Abdihakim')
        self.assertEqual(self.new_user.password,'10203040')

    def test_saveUser(self):
        '''test case method to test if user is saved to users list'''
        self.new_user.saveUser()
        self.assertEqual(len(User.users),1)


    def test_findUser(self):
        '''Test case method to test for functionality find user'''
        self.new_user.saveUser()
        confirm_user = User('Ali@234','Ali12345')
        confirm_user.saveUser()
        found_user = User.findUser("Ali@234")
        self.assertEqual(found_user.userName,confirm_user.userName)
if __name__ == '__main__':
    unittest.main()
