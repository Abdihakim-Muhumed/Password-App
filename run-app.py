#!/usr/bin/env python3.8

from classes import User
from classes import Credential

def create_user(username,password):
    '''Function to create a user object'''
    newUser = User(username,password)
    return newUser

def create_credentials(the_account,username,password):
    '''Function to create a credential object'''
    newCredential = Credential(the_account,username,password)
    return newCredential

def save_user(user):
    '''Function to save a user object'''
    user.saveUser()

def find_user(user):
    '''Function to find a user'''
    user.findUser()

def save_credentials(user,credentials):
    '''Function for saving user's credentials'''
    user.saveCredentials(credentials)

def find_credentials(user,the_account):
    '''Function to find a certain account credentials by a user'''
    user.findCredentials(the_account)

def delete_credentials(user,the_account):
    '''function to delete a certain account credentials by a user'''
    user.deleteCredentials(the_account)

def delete_all_credentials(user):
    '''function to delete all credentials of a user'''
    user.deleteAllCredentials()

def view_all_credentials(user):
    '''function to view all user credentials'''
    user.viewAllCredentials()

def generate_password(length):
    letters_and_digits = string.ascii_letters + string.digits
    random_password = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return  random_password



def main():
    while True:
            print('Welcome to Credential Store ! Use the following to chose an action:')
            print('\n')
            print('su - sign Up')
            print('\n')
            print('si - sign in')
            print('\n')
            print('ex - exit app')
            start_code = input().lower()
            if start_code == 'su':
                print('Enter your Name:')
                username = input()
                print('Enter a password:')
                password = input()

                user = create_user(username,name)
                save_user(user)
                print('You have successfully signed up!')
                while True:
                    print(f"Dear {user.userName}, What would you like to do today?")
                    print('\n')
                    print("Use these short codes to choose a corresponding action: ")
                    print('\n')
                    print("nw - to create new credentials for an account")
                    print('\n')
                    print("vw - to view specific account credentials")
                    print('\n')
                    print("va - to view all your credentials")
                    print('\n')
                    print("dl - to delete specific account credentials")
                    print('\n')
                    print("da - to delete all credentials")
                    print('\n')
                    print("lo -  to log out of your account")
                    print('\n')
                    short_code = input().lower()
                    if short_code == 'nw':
                        print('Enter the account name you want to create credentials for:')
                        theAccount = input().capitalise()
                        print('Enter username: ')
                        username = input()
                        print("Do you want to generate a password or enter your own password? Enter 'y' to generate a password or 'n' to create your own.")
                        pass_code =input()
                        if pass_code =='y':
                            print('Enter length of password you desire:')
                            p_length = int(input())
                            password = generate_password(p_length)
                            print(f'Password created ; {password}')

                        elif pass_code == 'n':
                            print('Enter password:')
                            password = input()

                        else :
                            print('OOPS! I did not get that please enter correct code')

                        credential = create_credentials(theAccount,username,password)
                        save_credentials(user,credential)
                        print(f"Credentials for {credential.the_account} successfully created and saved")

                    elif short_code == 'vw':
                        Print('Enter account name you want to view its credentials: ')
                        to_view = input().capitalise()
                        to_show = find_credentials(user,to_view)
                        if to_show:
                            print(f" Account : {to_show.account_name}")
                            print('\n')
                            print(f"Username : {to_show.user_name}")
                            print('\n')
                            print(f"Password : {to_show.pass_word}")

                        else :
                            print('Accout credentials not found . Please create.')

                    elif short_code == 'va':
                        all_credentials = view_all_credentials(user)
                        print("Account              Username                Password")
                        for credential in all_credentials:
                            print(f"{credential.account_name}      {credential.user_name}      {credential.pass_word}")
