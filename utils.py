# Import necessary modules and libraries
import os
import time
import utils
import pandas
import motif
import datetime
import string
import random


class Utils:


    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')


    def new_user_register(usr_pswd_df):
        utils.Utils.clear_screen()
        # Initialize a flag for user registration
        user_registered = False
        # Loop for user registration or login
        while not user_registered:
            # Ask the user if they are a new user or an existing one
            already_registered_bool = input("""▀▄▀▄▀▄ If you are a new user press 'Y', else press any other key ▄▀▄▀▄▀

▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀

>>> """)
            utils.Utils.clear_screen()

            # Check if the user wants to register as a new user
            if already_registered_bool.upper() == 'Y':
                
                unique_new_usr_entered = False
                # Loop to ensure the entered username is unique
                while not unique_new_usr_entered:
                    # Ask the user to enter their credentials
                    motif.Motif.enter_username()
                    new_username = input('>>> ')

                    # Check if the entered username already exists
                    if new_username in usr_pswd_df['UserName'].to_list():
                        unique_new_usr_entered = False 
                        utils.Utils.try_again_user_already_registered()
                    else:
                        unique_new_usr_entered = True
                        utils.Utils.clear_screen()
                        motif.Motif.enter_password()
                        new_password = input('>>> ')

                        # Add the new user to the DataFrame and save to the CSV file
                        usr_pswd_df.loc[len(usr_pswd_df)] = [new_username, new_password]
                        usr_pswd_df.to_csv('usr_pswd_csv.csv', index=None)
                        utils.Utils.clear_screen()
                        motif.Motif.user_listed()
                        time.sleep(2)
                        utils.Utils.clear_screen()
                        user_registered = True
            else:
                user_registered = True # False True to Exit While Loop

    
    def add_task_details(user_todo_df, user_name):
        add_task_sucessfull = False
        while add_task_sucessfull == False:
            utils.Utils.clear_screen()
            motif.Motif.add_task()
            task_name = input('''
Please Enter the Task Name.

>>> ''')
            utils.Utils.clear_screen()
            motif.Motif.add_task()
            task_due = input('''
Please Enter the Task Due Date in DD-MM-YYYY format.

>>> ''')
            utils.Utils.clear_screen()
            motif.Motif.add_task()
            task_priority = input('''
Please Enter the Task Priority Status.

>>> ''')
            task_status = 'Incomplete' 
            utils.Utils.clear_screen()
            motif.Motif.add_task()
            task_list_correct = input(f"""
Please verify the entered details.
                                
Name : {task_name}
Due Date : {task_due}
Priority : {task_priority}
Status : {task_status} 

Press 'Enter' to Confirm, or Any Other Key to Re-Enter the Details.

>>> """)
            if task_list_correct == '':
                utils.Utils.clear_screen()
                motif.Motif.task_added()
                add_task_sucessfull = True
                user_todo_df.loc[len(user_todo_df)] = [task_name, task_due, task_priority, task_status]
                user_todo_df.to_csv(f'{user_name}_to-do.csv', index=None)
                time.sleep(2)
                utils.Utils.clear_screen()
            else:
                utils.Utils.clear_screen()
                motif.Motif.add_task()
                really_want_task_add = input('''
Please press 'T' if you wish to add a task or press any other key to go to main menu.
   
>>> ''')            
                if really_want_task_add.upper() == 'T':
                    add_task_sucessfull = False
                    utils.Utils.try_again()
                else:
                    utils.Utils.clear_screen()
                    motif.Motif.exit_add()
                    time.sleep(2)
                    utils.Utils.clear_screen()
                    add_task_sucessfull = True # False True to exit While Loop
    
    
    def edit_task_details(user_todo_df, user_name, task_edit_index):
        edit_task_sucessfull = False
        while edit_task_sucessfull == False:
            task_edit_dic = user_todo_df.loc[task_edit_index].to_dict()
            utils.Utils.clear_screen()
            motif.Motif.edit_task()
            task_name_input = input(f'''
Press Enter to Continue with Original Task Name '{task_edit_dic['Task']}' or Enter New Task Name.

>>> ''')
            task_name = task_edit_dic['Task'] if task_name_input == '' else task_name_input
            utils.Utils.clear_screen()
            motif.Motif.edit_task()
            task_due_input = input(f'''
Press Enter to Continue with Original Due Date '{task_edit_dic['Due Date']}' or Enter New Due Date.

>>> ''')
            task_due = task_edit_dic['Due Date'] if task_due_input == '' else task_due_input
            utils.Utils.clear_screen()
            motif.Motif.edit_task()
            task_priority_input = input(f'''
Press Enter to Continue with Original Task Priority '{task_edit_dic['Priority']}' or Enter New Task Priority.

>>> ''')
            task_priority = task_edit_dic['Priority'] if task_priority_input == '' else task_priority_input
            utils.Utils.clear_screen()
            motif.Motif.edit_task()
            task_status_input = input(f'''
Press Enter to Continue with Original Task Status '{task_edit_dic['Status']}' or Enter New Task Status.

>>> ''') 
            task_status = task_edit_dic['Status'] if task_status_input == '' else task_status_input
            utils.Utils.clear_screen()
            motif.Motif.edit_task()
            edit_task_list_cnfrm = input(f"""
Please verify the entered details.
                                
Name : {task_name}
Due Date : {task_due}
Priority : {task_priority}
Status : {task_status} 

Press 'Enter' to Confirm, or Any Other Key to Re-Enter the Details.

>>> """)
            if edit_task_list_cnfrm == '':
                utils.Utils.clear_screen()
                motif.Motif.task_edited()
                edit_task_sucessfull = True
                user_todo_df.loc[task_edit_index] = [task_name, task_due, task_priority, task_status]
                user_todo_df.to_csv(f'{user_name}_to-do.csv', index=None)
                time.sleep(2)
                utils.Utils.clear_screen()
            else:
                utils.Utils.clear_screen()
                motif.Motif.edit_task()
                print(f"""
Please verify the entered details.
                                
Name : {task_name}
Due Date : {task_due}
Priority : {task_priority}
Status : {task_status}
""")
                really_want_task_edit = input('''
Please press 'T' if you wish to edit this task or press any other key to go to main menu.

>>> ''')            
                if really_want_task_edit.upper() == 'T':
                    edit_task_sucessfull = False
                    utils.Utils.try_again()
                else:
                    utils.Utils.clear_screen()
                    motif.Motif.exit_edit()
                    time.sleep(2)
                    utils.Utils.clear_screen()
                    edit_task_sucessfull = True # False True to exit While Loop


    def mark_task_complete(user_todo_df, user_name, task_done_index):
        utils.Utils.clear_screen()
        motif.Motif.task_done()
        task_done_dic = user_todo_df.loc[task_done_index].to_dict()
        task_done_dic['Status'] = 'Done'
        user_todo_df.loc[task_done_index] = task_done_dic
        user_todo_df.to_csv(f'{user_name}_to-do.csv', index= None)
        time.sleep(2)
        utils.Utils.clear_screen()
    

    def delete_task(user_todo_df, user_name, task_delete_index):
        utils.Utils.clear_screen()
        motif.Motif.task_deleted()
        user_todo_df = user_todo_df.drop(task_delete_index)
        user_todo_df.to_csv(f'{user_name}_to-do.csv', index= None)
        time.sleep(2)
        utils.Utils.clear_screen()


    def really_want_quit():
        # Ask User if He Really Wants to Quit
        utils.Utils.clear_screen()
        motif.Motif.quit_program()
        really_want_quit = input('''
Press 'T' if you want to quit the program or else press any other key.

>>> ''')
        if really_want_quit.upper() == 'T':
            # User Go-Ahead Quit Program
            utils.Utils.quit()
            exit()
        else:
            # User dosen't Want to Quit
            utils.Utils.try_again()


    def encrypt_text(plain_text, encryption_key = '346826225783524277765475541271882162717441692277463342484484495266342596393526438787944338597623448'):
        encrypted_text = ''
        name_chr_index = 0
        encrypt_chars_string = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
        encrypt_chars_string = encrypt_chars_string.replace("'", "")
        encrypt_chars_string = encrypt_chars_string.replace('"', "")
        encrypt_chars_string = encrypt_chars_string.replace(',', "")
        encryption_key = encryption_key[:len(plain_text)]
        for num_encryption_chars in encryption_key:
            num_encryption_chars = int(num_encryption_chars)
            for encryption_character in range(num_encryption_chars):
                encrypted_text += random.choice(encrypt_chars_string)
            encrypted_text += plain_text[name_chr_index]
            name_chr_index += 1
        encrypted_text = f'{len(plain_text)} {encrypted_text}'    
        return encrypted_text
    

    def decrypt(encrypted_text, encryption_key = '346826225783524277765475541271882162717441692277463342484484495266342596393526438787944338597623448'):
        length_plain_text = int(encrypted_text.split(' ')[0])
        encrypted_text = encrypted_text.split(' ')[1]
        plain_text = ''
        encryption_key = encryption_key[:length_plain_text]
        encrypted_text_index = 0
        loop_counter = 0
        for num_encryption_chars in encryption_key:
            num_encryption_chars = int(num_encryption_chars)
            encrypted_text_index += num_encryption_chars
            if loop_counter == 0:
                plain_text += encrypted_text[encrypted_text_index]
            else:
                plain_text += encrypted_text[encrypted_text_index + loop_counter]
            loop_counter += 1
        return plain_text


    def initial_greeting():
        utils.Utils.clear_screen()
        motif.Motif.welcome_stage_1()
        time.sleep(0.25)
        utils.Utils.clear_screen()
        motif.Motif.welcome_stage_2()
        time.sleep(0.25)
        utils.Utils.clear_screen()
        motif.Motif.welcome_stage_3()
        time.sleep(0.25)
        utils.Utils.clear_screen()
        motif.Motif.welcome_stage_4()
        time.sleep(0.25)
        utils.Utils.clear_screen()
        motif.Motif.welcome_stage_5()
        time.sleep(1.2)
        motif.Motif.greeting_instructions()


    def try_again():
        utils.Utils.clear_screen()
        motif.Motif.try_again_in_3()
        time.sleep(1.2)
        utils.Utils.clear_screen()
        motif.Motif.try_again_in_2()
        time.sleep(1.2)
        utils.Utils.clear_screen()
        motif.Motif.try_again_in_1()
        time.sleep(1.2)
        utils.Utils.clear_screen()


    def try_again_list_is_empty():
        utils.Utils.clear_screen()
        motif.Motif.list_is_empty()
        time.sleep(2)
        utils.Utils.try_again()


    def try_again_invalid_input():
        utils.Utils.clear_screen()
        motif.Motif.invalid_input()
        time.sleep(2)
        utils.Utils.try_again()


    def try_again_incorrect_password():
        utils.Utils.clear_screen()
        motif.Motif.incorrect_password()
        time.sleep(2)
        utils.Utils.try_again()


    def try_again_import_file_unreadable():
        utils.Utils.clear_screen()
        motif.Motif.file_unreadable()
        time.sleep(2)
        utils.Utils.clear_screen()
        motif.Motif.exit_import()
        time.sleep(2)
        utils.Utils.try_again()

        
    def try_again_invalid_import_path():
        utils.Utils.clear_screen()
        motif.Motif.invalid_path()
        time.sleep(2)
        utils.Utils.clear_screen()
        motif.Motif.exit_import()
        time.sleep(2)
        utils.Utils.try_again()


    def try_again_exit_export():
        utils.Utils.clear_screen()
        motif.Motif.exit_export()
        time.sleep(2)
        utils.Utils.try_again()

    
    def try_again_user_already_registered():
        utils.Utils.clear_screen()
        motif.Motif.user_exists()
        time.sleep(2)
        utils.Utils.try_again()


    def quit():
        utils.Utils.clear_screen()
        motif.Motif.logging_out()
        time.sleep(2)
        utils.Utils.clear_screen()
        motif.Motif.thank_you()
        time.sleep(2)
        utils.Utils.clear_screen()

