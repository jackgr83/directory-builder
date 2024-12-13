directory_structure = {}

def get_cmd():
    valid_inputs = ["CREATE", "LIST", "MOVE", "DELETE"]
    while True:
        cmd = input("Enter a command (CREATE/LIST/MOVE/DELETE): ")
        if cmd.split(" ")[0].upper() not in valid_inputs:
            print("Please enter a valid command (CREATE/LIST/MOVE/DELETE)")
            continue
        else:
            return cmd

def create_dir(dir_path):
    dirs = dir_path.split('/')
    dir_str = directory_structure
    for d in dirs[:-1]:
        dir_str[d] = {}
        dir_str = dir_str[d]
    dir_str[dirs[-1]] = {}

def list_dir(structure, indent=""):
    for folder, subfolder in sorted(structure.items()):
        if isinstance(subfolder, dict):
            print(f"{indent}{folder}")
            list_dir(subfolder, indent + "  ")
        else:
            print(f"{indent}{folder}")

def move_dir(structure, src_path, dest_path):
    src_dirs = src_path.split("/")
    dest_dirs = dest_path.split("/")

    src_parent = structure
    for dir in src_dirs[:-1]:
        if dir in src_parent and isinstance(src_parent[dir], dict):
            src_parent = src_parent[dir]

    move_dir = src_dirs[-1]
    moved_dir = src_parent.pop(move_dir)

    dest_parent = structure
    for dir in dest_dirs:
        if dir in dest_parent and isinstance(dest_parent[dir], dict):
            dest_parent = dest_parent[dir]
    dest_parent[move_dir] = moved_dir   

def delete_dir(structure, dir_path):
    dirs = dir_path.split("/")
    parent_dir = structure
    for dir in dirs[:-1]:
        if dir in parent_dir and isinstance(parent_dir[dir], dict):
            parent_dir = parent_dir[dir]
    if dirs[-1] in parent_dir:
        del parent_dir[dirs[-1]]
    else:
        print(f"Cannot delete {dir_path} - {dirs[0]} does not exist")
    
if __name__ == "__main__":
    while True:
        cmd = input("Enter a command: ")
        if cmd.split(" ")[0] not in ["CREATE", "LIST", "MOVE", "DELETE"]:
            print("Please enter a valid command (CREATE/LIST/MOVE/DELETE)")
            continue
        else:
            cmds = cmd.split(" ")

            if cmds[0] == "CREATE":
                print(cmd)
                create_dir(cmds[1])
            elif cmds[0] == "LIST":
                print(cmd)
                list_dir(directory_structure)
            elif cmds[0] == "MOVE":
                print(cmd)
                move_dir(directory_structure, cmds[1], cmds[2])
            elif cmds[0] == "DELETE":
                print(cmd)
                delete_dir(directory_structure, cmds[1])

