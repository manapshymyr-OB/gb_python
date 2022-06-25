import yaml
import os

with open(r'dirs.yaml') as file:
    project_dir_structure = yaml.load(file, Loader=yaml.FullLoader)


current_dir = os.getcwd()
for project_name, project_folders in project_dir_structure.items():
    root_dir = os.path.join(current_dir, project_name)
    for project_folder, project_sub_folder in project_folders.items():
        sub_root_dir = os.path.join(root_dir, project_folder)
        os.makedirs(sub_root_dir, exist_ok = True)
        for file in project_sub_folder:
            if type(file) == dict:
                for sub_dir, sub_sub_dir in file.items():
                    sub_root_root_dir = os.path.join(sub_root_dir, sub_dir)
                    for project_sub_folder_folder, project_sub_folder_files in sub_sub_dir.items():
                        sub_root_root_root_dir = os.path.join(sub_root_root_dir, project_sub_folder_folder)
                        os.makedirs(sub_root_root_root_dir, exist_ok=True)

                        for sub_file in project_sub_folder_files:
                            create_file = os.path.join(sub_root_root_root_dir, sub_file)
                            open(create_file, 'a').close()

            else:
                create_file = os.path.join(sub_root_dir, file)
                open(create_file, 'a').close()








