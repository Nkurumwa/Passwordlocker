import pyperclip

class Credentials:
    '''
    Class that creates accounts and authenticates the users
    '''
    users_list=[]

    def __init__ (self, identify, user_name, password):
        '''
        Initalizing the variables
        '''
        self.identify = identify
        self.user_name = user_name
        self.password = password

            def create_account(self):
        '''
        creating and saving log in credentials for the various users
        '''
        Credentials.users_list.append(self)

          @classmethod
    def authenticate_account(cls, name, key):
        '''
        Method that checks if the username and password are correct
        '''
        for user in cls.users_list:
            if user.user_name == name and user.password == key:
                return user
        return 0

     class UsersData:
    '''
    Class that holds website and password data for the users
    '''
    data_list = []
    def __init__(self,ident,data_id,website,web_key,name):
        self.ident = ident
        self.data_id = data_id
        self.website = website
        self.web_key = web_key
        self.name = name
    
    def add_password(self):
        '''
        creating a method that creates the username and password
        '''
        UsersData.data_list.append(self)