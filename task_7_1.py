import os


# get current directory
current_dir = os.getcwd()

project_name = 'my_project'
sub_folders = ['settings', 'mainapp', 'adminapp', 'authapp']

for sub_folder in sub_folders:
    new_dir = os.path.join(current_dir, project_name + '\\' + sub_folder)
    # create dir if does not exist
    try:
        os.makedirs(new_dir, exist_ok=False)
    except OSError as e:
        print(e)



