import os
"""
def list_all_directories(start_path):
    directory_list = []
    for root, dirs, files in os.walk(start_path):
        for name in dirs:
            directory_list.append(os.path.join(root, name))
    return directory_list

# Example usage:
start_path = "C:\\Users\\Default\\Dowloads"  # For Unix-like systems, use "C:\\" for Windows.
all_directories = list_all_directories(start_path)
print("Directories found:")
for directory in all_directories:
    print(directory)"""
def name_file():
    file_name="pruebas.xlsx"
    list_path = []
    start_path="C:\\Users\\Default\\Downloads"
    if file_name:
        for file in os.walk(start_path):
            list_path.append(os.path.join(start_path,file_name))
        print(f"{str(list_path[0])}")
    else:
        print("Ruta no encontrada por favor intentelo otra vez")

name_file()

def name_file():
    filename = get_prompt("Please say the filename (without extension)...:")
    if filename:
        current_directory = os.getcwd()
        full_path = os.path.join(current_directory, f"{filename}.xlsx")
        if os.path.exists(full_path):
            return full_path
        else:
            print("File not found in the current directory.")
            return ""
    else:
        return ""
