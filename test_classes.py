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
        '''tets__init__ test case to check for proper User object initialization'''
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


class TestCredentiasl(unittest.TestCase):
    """class for testing various behaviours of class Credential
    arg:
        unittest.Testcase:  Testcase class that provides test methods.
    """
    def setUp(self):
        self.new_credential = Credential('Instagram','Abdihakim9_','Abdulhakim@9')

    def tearDown(self):
        '''tearDown method to set User list to to 0'''
        Credential.credentials = []

    def test__init__(self):
        '''tets__init__ test case to check for proper credential object initialization'''
        self.assertEqual(self.new_credential.account_name,'Instagram')
        self.assertEqual(self.new_credential.user_name,'Abdihakim9_')
        self.assertEqual(self.new_credential.pass_word,'Abdulhakim@9')

    def test_saveCredential(self):
        self.new_credential.saveCredential()
        self.assertEqual(len(Credential.credentials),1)

    def test_findCredential(self):
        self.new_credential.saveCredential()
        confirm_credential = Credential('Facebook','Abdihakym Muhumed','ABDULHAKIM')
        confirm_credential.saveCredential()
        found_credential = Credential.findCredential('Facebook')
        self.assertEqual(found_credential.account_name,confirm_credential.account_name)


    def test_showCredentials(self):
        self.new_credential.saveCredential()
        chosen_credential = Credential('Gmail','abdihakim1434@gmail.com','Abdulhakim1434')
        chosen_credential.saveCredential()
        shown_credential = Credential.showCredentials('Gmail')
        self.assertEqual(shown_credential.account_name,chosen_credential.account_name)
        self.assertEqual(shown_credential.user_name,chosen_credential.user_name)
        self.assertEqual(shown_credential.pass_word,chosen_credential.pass_word)


    def test_deleteCredential(self):
        self.new_credential.saveCredential()
        toDelete = Credential('Gmail','abdihakim1434@gmail.com','Abdulhakim9')
        toDelete.saveCredential()
        toDelete.deleteCredential()
        self.assertEqual(len(Credential.credentials),1)


if __name__ == '__main__':
    unittest.main()
