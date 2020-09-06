class User:
    """user class"""
    users = []
    def __init__(self, userName,password):
        '''Method for creating a user object'''
        self.userName = userName
        self.password = password
        self.credentials = []

    def saveUser(self):
        '''Method to save new user in the users list'''
        User.users.append(self)

    @classmethod
    def findUser(cls,find_name):
        '''method to find a user'''
        for user in cls.users:
            if user.userName == find_name :
                return user

    def saveCredentials(self,credentials):
        '''methods that saves credentials about a user in credentials list'''
        self.credentials.append(credentials)

    def findCredentials(self,account):
        '''method to find a credential of the user'''
        for credential in self.credentials:
            if credential.account_name == account:
                return credential
    def deleteCredentials(self,account):
        '''method to delete a credential of a user'''
        self.credentials.remove(self.findCredentials(account))

    def deleteAllCredentials(self):
        '''User method that deletes all the credentials of the user'''
        self.credentials = []

    def viewAllCredentials(self):
        '''method for a user to view all their credentials'''
        return self.credentials


class Credential:
    '''user credentials class'''
    def __init__(self, account_name,user_name,pass_word):
        '''Method to instantiate credential objec'''
        self.account_name = account_name
        self.user_name = user_name
        self.pass_word = pass_word
