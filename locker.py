import pyperclip

class Credentials:
    '''
    Class that creates accounts and authenticates the users
    '''
    users_list=[]

    def __init__(self, identify, user_name, password):
        '''
        Initalizing the variables
        '''
        self.identify = identify
        self.user_name = user_name
        self.password = password