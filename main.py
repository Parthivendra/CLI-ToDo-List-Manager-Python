# Import necessary modules and libraries
import os
import time
import utils
import pandas
import motif
import datetime
import string
import random
import csv

user_welcomed = False
new_user_registered = False
user_logged_in = False

while True:
    try:

        if not user_welcomed:
            # Put User in Welcome Page
            # Display an initial greeting message
            utils.Utils.initial_greeting()

            # Read user passwords from a CSV file into a DataFrame
            usr_pswd_df = pandas.read_csv('usr_pswd_csv.csv', index_col=None)

            # Wait for user input to continue
            user_input_wait = input('''
Press 'Enter' to Continue.

>>> ''')
            utils.Utils.clear_screen()
        else:
            # User has been welcomed
            # Moving on to new user registration 
            pass
        user_welcomed = True

        if not new_user_registered:
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
                        encrypted_new_username = utils.Utils.encrypt_text(new_username)

                        # Decrypting stored encrypted usernames
                        decrypted_user_name_list = []
                        for each_encrypted_username in usr_pswd_df['UserName'].to_list():
                            each_decrypted_username = utils.Utils.decrypt(each_encrypted_username)
                            decrypted_user_name_list.append(each_decrypted_username)

                        # Check if the entered username already exists
                        if new_username in decrypted_user_name_list:
                            unique_new_usr_entered = False 
                            utils.Utils.try_again_user_already_registered()
                        else:
                            unique_new_usr_entered = True
                            utils.Utils.clear_screen()
                            motif.Motif.enter_password()
                            new_password = input('>>> ')
                            encrypted_new_password = utils.Utils.encrypt_text(new_password)

                            # Add the new user to the DataFrame and save to the CSV file
                            usr_pswd_df.loc[len(usr_pswd_df)] = [encrypted_new_username, encrypted_new_password]
                            usr_pswd_df.to_csv('usr_pswd_csv.csv', index=None, quoting= csv.QUOTE_ALL)
                            utils.Utils.clear_screen()
                            motif.Motif.user_listed()
                            time.sleep(2)
                            utils.Utils.clear_screen()
                            user_registered = True
                else:
                    user_registered = True      #False True to exit while loop
            new_user_registered = True


        else:
            # User had already reached new user registration page
            # Sending User To Login Page
            pass
        
        if not user_logged_in:
            # Put User in login page
            # Display a login message
            motif.Motif.please_login()
            time.sleep(2)
            utils.Utils.clear_screen()

            correct_user_entered = False
            # Ask the user to enter their username
            motif.Motif.enter_username()
            user_name = input('>>> ')
            encrypted_user_name = utils.Utils.encrypt_text(user_name)

            # Decrypting stored encrypted usernames
            decrypted_user_name_list = []
            for each_encrypted_username in usr_pswd_df['UserName'].to_list():
                each_decrypted_username = utils.Utils.decrypt(each_encrypted_username)
                decrypted_user_name_list.append(each_decrypted_username)

            # Decrypting stored encrypted usernames
            decrypted_password_list = []
            for each_encrypted_password in usr_pswd_df['Password'].to_list():
                each_decrypted_password = utils.Utils.decrypt(each_encrypted_password)
                decrypted_password_list.append(each_decrypted_password)

            decrypted_dict = dict(zip(decrypted_user_name_list, decrypted_password_list))

            # Check if the entered username exists
            if user_name not in decrypted_user_name_list:
                # Ensuring that the user goes to new user registration page
                new_user_registered = False
                # User name dosen't exist
                utils.Utils.clear_screen()
                motif.Motif.user_not_listed()
                time.sleep(2)
                utils.Utils.clear_screen()
                motif.Motif.please_register()
                time.sleep(2)
                utils.Utils.clear_screen()
                # Skip Remaning code go back to asking for new user
                continue
            else:
                # User name exists
                # Move on to password entry
                pass

            # Initialize a flag for correct password entry
            correct_pswd_entered = False
            # Loop for entering the correct password
            while not correct_pswd_entered:
                utils.Utils.clear_screen()
                motif.Motif.enter_password()
                password = input('>>> ')
                encrypted_password = utils.Utils.encrypt_text(password)

                # Create a dictionary of usernames and passwords
                # usr_pswd_dic = {key: value for key, value in zip(usr_pswd_df['UserName'].to_list(), usr_pswd_df['Password'].to_list())}

                # Check if the entered password is correct
                if password != decrypted_dict[user_name]:
                    # Incorrect password entered
                    correct_pswd_entered = False
                    utils.Utils.try_again_incorrect_password()           
                else:
                    # Correct password entered
                    correct_pswd_entered = True
            user_logged_in = True
            utils.Utils.clear_screen()
            motif.Motif.logged_in()
            time.sleep(2)
            utils.Utils.clear_screen()
        else:
            # User Has Already Logged In 
            # Sending User to Main Menu Page
            pass

        # Main menu loop
        while True:
            utils.Utils.clear_screen()
            motif.Motif.cli_todo_manager()
            print('''
Please choose an option by entering the corresponding number :

[1] View To-Do List
[2] Add Task
[3] Mark Task as Complete
[4] Delete Task
[5] Edit Task
[6] Import Tasks from a File
[7] Export Tasks to a File
[8] Quit
''')

            # Checking if the user has an existing To-Do list
            if os.path.exists(f'{user_name}_to-do.csv'):
                user_todo_df = pandas.read_csv(f'{user_name}_to-do.csv')
                user_todo_df.sort_values(by='Due Date')
            else:
                # Create an empty DataFrame for the user's To-Do list
                user_todo_df = pandas.DataFrame(columns=['Task', 'Due Date', 'Priority', 'Status'])
                user_todo_df.to_csv(f'{user_name}_to-do.csv', index=None)
                user_todo_df.sort_values(by='Due Date')

            # Check if the user's To-Do list is empty
            user_todo_df_is_empty = True if len(user_todo_df) == 0 else False

            # Get user input for menu options
            user_input_task_index = input('>>> ')

            if user_input_task_index == '1':
                # VIEW TO-DO
                if user_todo_df_is_empty:
                    utils.Utils.try_again_list_is_empty()
                else:
                    # Display the user's To-Do list
                    utils.Utils.clear_screen()
                    motif.Motif.cli_todo_manager()
                    print(f'''
Your To-Do List :


{user_todo_df}
''')
                    user_input_wait = input("""Press 'Enter' to Continue.

>>> """)

            elif user_input_task_index == '2':
                # ADD TASK
                utils.Utils.add_task_details(user_todo_df, user_name)

            elif user_input_task_index == '3':    
                # TASK DONE
                if user_todo_df_is_empty:
                    utils.Utils.try_again_list_is_empty()
                else:
                    task_done_data_listed = False
                    while not task_done_data_listed:
                        while True:
                            try:
                                utils.Utils.clear_screen()
                                motif.Motif.task_status()
                                print(f'''
Your To-Do List :


{user_todo_df}
''')
                                task_done_index = int(input('''
Please Enter the Corresponding Index of the Task you want to Edit.

>>> '''))
                                if task_done_index > len(user_todo_df['Task'].to_list()) or task_done_index < 0:
                                    raise ValueError(f"Index must be within range (0 to {len(user_todo_df['Task'].to_list())})")
                            except ValueError:
                                utils.Utils.try_again_invalid_input()
                            else:
                                break
                        utils.Utils.clear_screen()
                        motif.Motif.task_status()
                        print(f'''
Press 'Enter' if you wish to mark the following task as 'Done', else Press Any Other Key.
''')
                        for key, value in user_todo_df.loc[task_done_index].items():
                            print(f'''
{key} : {value}
''')
                        task_done_index_cnfrm = input('''
>>> ''')
                        if task_done_index_cnfrm == '':
                            # User agrees to mark the task as 'Done'
                            utils.Utils.mark_task_complete(user_todo_df, user_name, task_done_index)
                            task_done_data_listed = True
                        else:
                            really_want_task_done = input('''
Please press 'T' if you wish to mark a task as done or press any other key to go to the previous menu.

>>> ''')
                            if really_want_task_done.upper() == 'T':
                                task_done_data_listed = False
                                utils.Utils.try_again()
                            else:
                                utils.Utils.clear_screen()
                                motif.Motif.exit_status()
                                time.sleep(2)
                                utils.Utils.clear_screen()
                                task_done_data_listed = True        # False True to exit while loop

            elif user_input_task_index == '4':
                # DELETE TASK
                if user_todo_df_is_empty:
                    utils.Utils.try_again_list_is_empty()
                else:
                    task_deleted_successfully = False
                    while not task_deleted_successfully:
                        while True:
                            try:
                                utils.Utils.clear_screen()
                                motif.Motif.delete_task()
                                print(f'''
Your To-Do List :


{user_todo_df}
''')
                                task_delete_index = int(input('''
Please Enter the Corresponding Index of the Task you want to Delete.

>>> '''))
                                if task_delete_index > len(user_todo_df['Task'].to_list()) or task_delete_index < 0:
                                    raise ValueError(f"Index must be within range (0 to {len(user_todo_df['Task'].to_list())})")
                            except ValueError:
                                utils.Utils.try_again_invalid_input()
                            else:
                                break
                        utils.Utils.clear_screen()
                        motif.Motif.delete_task()
                        print(f'''
Press 'Enter' if you wish to delete the following task, else Press Any Other Key.
''')
                        for key, value in user_todo_df.loc[task_delete_index].items():
                            print(f'''
{key} : {value}
''')
                        task_delete_index_cnfrm = input('''
>>> ''')
                        if task_delete_index_cnfrm == '':
                            # User agrees to delete the task
                            utils.Utils.delete_task(user_todo_df, user_name, task_delete_index)
                            task_deleted_successfully = True
                        else:
                            really_want_task_deleted = input('''
Please press 'T' if you wish to delete a task or press any other key to go to the previous menu.

>>> ''')
                            if really_want_task_deleted.upper() == 'T':
                                task_deleted_successfully = False
                                utils.Utils.try_again()
                            else:
                                utils.Utils.clear_screen()
                                motif.Motif.exit_delete()
                                time.sleep(2)
                                utils.Utils.clear_screen()
                                task_deleted_successfully = True        # False True to exit while loop

            elif user_input_task_index == '5':
                # EDIT TASK
                task_edit_page_reached = False
                while not task_edit_page_reached:
                    while True:
                        try:
                            utils.Utils.clear_screen()
                            motif.Motif.edit_task()
                            print(f'''
Your To-Do List :


{user_todo_df}
''')
                            task_edit_index = int(input('''
Please Enter the Corresponding Index of the Task you want to Edit.

>>> '''))
                            if task_edit_index > len(user_todo_df['Task'].to_list()) or task_edit_index < 0:
                                raise ValueError(f"Index must be within range (0 to {len(user_todo_df['Task'].to_list())})")
                        except ValueError:
                            utils.Utils.try_again_invalid_input()
                        else:
                            break
                    utils.Utils.clear_screen()
                    motif.Motif.edit_task()
                    print(f'''
Press 'Enter' if you wish to edit the following task, else Press Any Other Key.
''')
                    for key, value in user_todo_df.loc[task_edit_index].items():
                        print(f'''
{key} : {value}
''')
                    task_edit_index_cnfrm = input('''

>>> ''') 
                    if task_edit_index_cnfrm == '':
                        # User agrees to change the task
                        utils.Utils.edit_task_details(user_todo_df, user_name, task_edit_index)
                        task_edit_page_reached = True
                    else:
                        utils.Utils.clear_screen()
                        motif.Motif.edit_task()
                        really_want_task_edit = input('''
Please press 'T' if you wish to edit a task or press any other key to go to the previous menu.

>>> ''')            
                        if really_want_task_edit.upper() == 'T':
                            task_edit_page_reached = False
                            utils.Utils.try_again()
                        else:
                            utils.Utils.clear_screen()
                            motif.Motif.exit_edit()
                            time.sleep(2)
                            utils.Utils.clear_screen()
                            task_edit_page_reached = True       # False True to exit while loop 

            elif user_input_task_index == '6':
                # Import Tasks from a File
                utils.Utils.clear_screen()
                motif.Motif.import_file()
                import_file_path = input('''
Please enter the file path of the CSV file that you want to import.

>>> ''')
                if os.path.exists(import_file_path):
                    # File path is valid
                    import_user_todo_df = pandas.read_csv(import_file_path)
                    if import_user_todo_df.columns.to_list() == ['Task', 'Due Date', 'Priority', 'Status']:
                        # File is readable
                        utils.Utils.clear_screen()
                        motif.Motif.importing_file()
                        time.sleep(2)
                        import_user_todo_df.to_csv(f'{user_name}_to-do.csv', index=None)
                        utils.Utils.clear_screen()
                        motif.Motif.file_imported()
                        time.sleep(2)
                        utils.Utils.clear_screen()
                    else:
                        # File is unreadable
                        utils.Utils.try_again_import_file_unreadable()
                else:
                    # File path is invalid
                    utils.Utils.try_again_invalid_import_path()

            elif user_input_task_index == '7':
                # Export Tasks to a File
                utils.Utils.clear_screen()
                motif.Motif.export_file()
                print(f'''
Your To-Do List :


{user_todo_df}
''')
                really_want_export_file = input('''
Press 'Enter' to export this To-Do List or press any other key to go to the previous menu.

>>> ''')
                if really_want_export_file == '':
                    # User agrees to export the file
                    utils.Utils.clear_screen()
                    motif.Motif.exporting_file()
                    export_user_todo_markdown = user_todo_df.to_markdown(index=None)
                    export_directory_name = f"{user_name}'s To-Do List Dated {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}"
                    os.makedirs(export_directory_name, exist_ok=True)
                    export_txt_file_path = os.path.join(os.path.abspath(export_directory_name), 'To-Do List.txt')
                    export_csv_file_path = os.path.join(os.path.abspath(export_directory_name), 'To-Do List.csv')
                    export_inst_file_path = os.path.join(os.path.abspath(export_directory_name), 'Instructions.txt')

                    user_todo_df.to_csv(export_csv_file_path, index=None)
                    with open(export_txt_file_path, 'w') as export_txt_file:
                        export_txt_file.write(export_user_todo_markdown)
                    with open(export_inst_file_path, 'w') as export_inst_file:
                        export_inst_file.write('''
#####################################################
## To-Do List Export Folder - Instructions for Use ##
#####################################################

Welcome to your To-Do List export folder!

This folder contains your To-Do List in two different formats:

1. To-Do List (TXT):
    - The "To-Do List.txt" file contains your To-Do List in plain text format.
    - You can open and view this file with any text editor or viewer.
    - Use this file to easily read and share your To-Do List.

2. To-Do List (CSV):
    - The "To-Do List.csv" file contains your To-Do List in CSV (Comma-Separated Values) format.
    - You can import this file into various applications, such as spreadsheet software.
    - To import, you will need to provide the complete path to this CSV file in the importing application.

Feel free to use these files to manage and keep track of your tasks. If you have any questions or need further assistance, please refer to the documentation of the application you are using for task management.

Thank you for using our To-Do List manager!

#####################################################
''')
                    time.sleep(2)
                    utils.Utils.clear_screen()
                    motif.Motif.file_exported()
                    user_input_wait = input(f'''
Your To-Do List has been exported to "{os.path.abspath(export_directory_name)}"                                     

Press 'Enter' to continue.

>>> ''')
                    utils.Utils.clear_screen()
                else:
                    # User does not want to export the file
                    utils.Utils.try_again_exit_export()

            elif user_input_task_index == '8':  
                # QUIT PROGRAM
                utils.Utils.really_want_quit()
            else:
                # Invalid input
                utils.Utils.try_again_invalid_input()
    except KeyboardInterrupt:
       utils.Utils.really_want_quit()
