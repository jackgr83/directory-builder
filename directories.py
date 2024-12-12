
directory_structure = {}

def get_cmd():
    valid_inputs = ["CREATE", "LIST", "MOVE", "DELETE"]
    while True:
        cmd = input("Enter a command (CREATE/LIST/MOVE/DELETE): ").upper()
        if cmd not in valid_inputs:
            print("Please enter a valid command (CREATE/LIST/MOVE/DELETE)")
            continue
        else:
            return cmd

def create_dir():
    resp = input("Enter a name for the directory/s you would like to create.\nNote: Use a slash to enter subdirectories (e.g. directory1/directory2): \n")

    dirs = resp.split('/')
    dir_str = directory_structure
    for dir in dirs[:-1]:
        dir_str[dir] = {}
        dir_str = dir_str[dir]
    dir_str[dirs[-1]] = None

    print(f"CREATE {resp}")

def list_dir(structure, indent=""):
    for folder, subfolder in structure.items():
        if isinstance(subfolder, dict):
            print(f"{indent}{folder}")
            list_dir(subfolder, indent + "  ")
        else:
            print(f"{indent}{folder}")

def move_dir():
    while True:
        resp = input("Enter the absolute path of the directory you would like to move followed by a space and the absolute path fo the directory to move it to: ")
        if resp not in directory_structure:
            print(f"{resp} does not exist. Please choose a valid directory name: {directory_structure.keys()}")
            continue
        else:
            # TODO: Move directories
            print(f"MOVE {resp}")
            break

def delete_dir():
    while True:
        resp = input("Enter a name for the directory you would like to create: ")
        if resp not in directory_structure:
            print(f"{resp} does not exist. Please choose a valid directory name: {directory_structure.keys()}")
            continue
        else:
            directory_structure.pop("dir_name")
            print(f"DELETE {resp}")
            break

def keep_going():
    while True:
        resp = input("Enter another command? (y/n):").lower()
        if resp not in ['y', 'n']:
            print("Please enter either y or n.")
            continue
        elif resp == "n":
            return False
        else:
            return True
    
if __name__ == "__main__":
    while True:
        cmd=get_cmd()

        if cmd == "CREATE":
            create_dir()
        elif cmd == "LIST":
            print(cmd)
            list_dir(directory_structure)
        elif cmd == "MOVE":
            move_dir()
        elif cmd == "DELETE":
            delete_dir()
        
        if keep_going():
            continue
        else:
            print(directory_structure)
            break
