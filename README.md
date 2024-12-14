# Directory Builder

### Introduction
This Python script simulates a hierarchical directory for file management. It allows a user to create, move, or delete directories by taking commands as inputs. An in-memory nested dictionary data structure is used for the implementation of the directory.

### Requirements
- Python 3.x

### How to Use
Follow these steps to use the directory builder:

1. Clone this repository locally:
    ```
    git clone https://github.com/jackgr83/directory-builder.git
    ```

2. Navigate to the project root directory:
    ```
    cd ./directory-builder
    ```

3. Run the directory builder via python:
    ```
    python directories.py
    ```
When finished using the tool, press ctrl+c to exit the script.

### Command Reference

The following commands can be used:
- CREATE [path]: Creates a new directory at the specified path.
    ```
    CREATE fruits/apples/fuji
    ```
- LIST: Lists the entire directory structure in a tree-like format.
    ```
    LIST
    ```
- MOVE [source_path] [destination_path]: Moves a directory from the source path to the destination path.
    ```
    MOVE grains/squash vegetables
    ```
- DELETE [path]: Deletes the directory at the specified path.
    ```
    DELETE fruits/apples/fuji
    ```