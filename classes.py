class User:
    """user class"""
    users = []
    credentials = []
    def __init__(self, userName,password):
        '''Method for creating a user object'''
        self.userName = userName
        self.password = password

    def saveUser(self):
        '''Method to save new user in the users list'''
        User.users.append(self)


    @classmethod
    def findUser(cls,name):
        for user in cls.users:
            if user.userName == name:
                return user


class Credential:
    '''user credentials class'''
    credentials = []

    def __init__(self, account_name,user_name,pass_word):
        '''Method to instantiate credential objec'''
        self.account_name = account_name
        self.user_name = user_name
        self.pass_word = pass_word

    def saveCredential(self):
        Credential.credentials.append(self)

    def deleteCredential(self):
        Credential.credentials.remove(self)

    @classmethod
    def findCredential(cls,account):
        for credential in cls.credentials:
            if credential.account_name == account:
                return credential

    @classmethod
    def showCredentials(cls,show):
        return cls.findCredential(show)
