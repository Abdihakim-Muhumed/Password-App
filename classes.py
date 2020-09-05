class User:
    """user class"""

    def __init__(self, userName,password):
        '''Method for creating a user object'''
        self.userName = userName
        self.password = password



class Credential:
    '''user credentials class'''

    def __init__(self, name,user_name,pass_word):
        '''Method to instantiate credential objec'''
        self.name = name
        self.user_name = user_name
        self.pass_word = pass_word
