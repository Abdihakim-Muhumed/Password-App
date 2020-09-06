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

    def test_saveCredentials(self):
        '''Method to test if the user credentials are being saved'''
        self.new_user.saveUser()
        test_user = User('Abdihakim99','ABDULHAKIM')
        test_user.saveUser()
        credential1= Credential('Facebook','Abdihakim9_','ABDULHAKIM')
        test_user.saveCredentials(credential1)
        self.assertEqual(len(test_user.credentials),1)

    def test_findCredentials(self):
        '''Method to find a credential of a user'''
        self.new_user.saveUser()
        test_user2 = User('Abdihakim99','ABDULHAKIM')
        test_user2.saveUser()
        credential2 = Credential('Facebook','Abdihakim9_','ABDULHAKIM')
        test_user2.saveCredentials(credential2)
        found_credential1 = test_user2.findCredentials('Facebook')
        self.assertEqual(found_credential1.account_name,credential2.account_name)

    def test_deleteCredentials(self):
        '''test case method to taste use method deletCredentials()'''
        self.new_user.saveUser()
        test_user3= User('Abdihakim017','CIT0017')
        test_user3.saveUser()
        credential3 = Credential('Gmail','Abdihakim.0017@gmail.com','CIT-017')
        credential4 = Credential('Instagram','Abdihakym22','Week1234')
        test_user3.saveCredentials(credential3)
        test_user3.saveCredentials(credential4)
        test_user3.deleteCredentials('Instagram')
        self.assertEqual(len(test_user3.credentials),1)

    def test_viewAllCredentials(self):
        '''test case method to test view all credentials of a user behaviour of the user class'''
        self.new_user.saveUser()
        test_user4 = User('Abdul De Matchan','Abdul1234')
        test_user4.saveUser()
        credential5 = Credential('Instagram','Abdul_De_','Abdul1234')
        credential6 = Credential('Facebook','Abdul_De_2','Abdul2341')
        test_user4.saveCredentials(credential5)
        test_user4.saveCredentials(credential6)
        self.assertEqual(test_user4.viewAllCredentials(),test_user4.credentials)

    def test_deleteAllCredentials(self):
        '''test case method to test if deleteAllCredentials method of a user is functional'''
        self.new_user.saveUser()
        test_user5 = User('Ali kimmich','Kimmich@123')
        test_user5.saveUser()
        credential7 = Credential('Snapchat','Kimmic_ali','Kimmich1234')
        credential8 = Credential('IG','Kimmicx','Kimmix123')
        test_user5.saveCredentials(credential7)
        test_user5.saveCredentials(credential8)
        test_user5.deleteAllCredentials()
        self.assertEqual(len(test_user5.credentials),0)


class TestCredentiasl(unittest.TestCase):
    """class for testing various behaviours of class Credential
    arg:
        unittest.Testcase:  Testcase class that provides test methods.
    """
    def setUp(self):
        self.new_credential = Credential('Instagram','Abdihakim9_','Abdulhakim@9')

    def test__init__(self):
        '''tets__init__ test case to check for proper credential object initialization'''
        self.assertEqual(self.new_credential.account_name,'Instagram')
        self.assertEqual(self.new_credential.user_name,'Abdihakim9_')
        self.assertEqual(self.new_credential.pass_word,'Abdulhakim@9')


if __name__ == '__main__':
    unittest.main()
