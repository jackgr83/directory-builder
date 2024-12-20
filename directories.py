# Create initial directory tree
directory_structure = {}

# Create a directory
def create_dir(dir_path):
    dirs = dir_path.split('/')
    dir_str = directory_structure
    for d in dirs[:-1]:
        dir_str[d] = {}
        dir_str = dir_str[d]
    dir_str[dirs[-1]] = {}

# List the directory tree
def list_dir(structure, indent=""):
    for folder, subfolder in sorted(structure.items()):
        if isinstance(subfolder, dict):
            print(f"{indent}{folder}")
            list_dir(subfolder, indent + "  ")
        else:
            print(f"{indent}{folder}")

# Move directory from source to a destination
def move_dir(structure, src_path, dest_path):
    src_dirs = src_path.split("/")
    dest_dirs = dest_path.split("/")

    # Find source parent directory in tree
    src_parent = structure
    for dir in src_dirs[:-1]:
        if dir in src_parent and isinstance(src_parent[dir], dict):
            src_parent = src_parent[dir]
        else:
            print(f"Error: Cannot move {src_path} - {src_path} does not exist")
            return

    move_dir = src_dirs[-1]

    # Remove directory from source
    moved_dir = src_parent.pop(move_dir)

    # Find destination parent directory in tree
    dest_parent = structure
    for dir in dest_dirs:
        if dir in dest_parent and isinstance(dest_parent[dir], dict):
            dest_parent = dest_parent[dir]
        else:
            print(f"Cannot move to {dest_path} - {dest_path} does not exist")

    # Move directory to destination
    dest_parent[move_dir] = moved_dir   

# Delete a directory
def delete_dir(structure, dir_path):
    dirs = dir_path.split("/")
    parent_dir = structure
    # Find parent directory
    for dir in dirs[:-1]:
        if dir in parent_dir and isinstance(parent_dir[dir], dict):
            parent_dir = parent_dir[dir]
        else:
            print(f"Cannot delete {dir_path} - {dirs[0]} does not exist")
            return
    # Delete directory
    if dirs[-1] in parent_dir:
        del parent_dir[dirs[-1]]
    else:
        print(f"Cannot delete {dir_path} - {dirs[0]} does not exist")

# Main loop to process inputs   
if __name__ == "__main__":
    while True:
        cmd = input("Enter a command: ")
        if cmd.split(" ")[0] not in ["CREATE", "LIST", "MOVE", "DELETE"]:
            print("Please enter a valid command (LIST or CREATE/MOVE/DELETE directory)")
            continue
        else:
            cmds = cmd.split(" ")

            if cmds[0] == "CREATE":
                if len(cmds) < 2:
                    print("CREATE command requires a directory")
                    continue
                else:
                    print(cmd)
                    create_dir(cmds[1])
            elif cmds[0] == "LIST":
                print(cmd)
                list_dir(directory_structure)
            elif cmds[0] == "MOVE":
                if len(cmds) < 3:
                    print("MOVE command requires a source and destination path")
                    continue
                else:
                    print(cmd)
                    move_dir(directory_structure, cmds[1], cmds[2])
            elif cmds[0] == "DELETE":
                if len(cmds) < 2:
                    print("CREATE command requires a directory")
                    continue
                else:
                    print(cmd)
                    delete_dir(directory_structure, cmds[1])

