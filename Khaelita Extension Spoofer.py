import os

def apply_rlo(file_name, new_extension):
    """
    This function takes a file name and a new extension,
    then applies the RLO (Right-to-Left Override) character
    to change the file extension.
    """
    # Unicode RLO character
    rlo_char = '\u202E'
    
    # Split the file name into name and extension
    name, old_extension = os.path.splitext(file_name)
    
    # Reverse the new extension
    new_extension_reversed = new_extension[::-1]
    
    # Construct the new file name with RLO character
    new_file_name = f"{name}{rlo_char}{new_extension_reversed}{old_extension}"
    
    return new_file_name

def rename_file(original_file_path, new_file_name):
    """
    This function renames the file at the given original file path
    to the new file name.
    """
    # Get the directory of the original file
    dir_name = os.path.dirname(original_file_path)
    
    # Construct the full path for the new file
    new_file_path = os.path.join(dir_name, new_file_name)
    
    # Rename the file
    os.rename(original_file_path, new_file_path)
    
    return new_file_path

# Main function to get user input and apply RLO
def main():
    print("RLO (Right-to-Left Override) File Extension Changer")
    print("This tool changes the appearance of file extensions using the RLO character.")
    
    original_file_path = input("Enter the full path of the original file (with extension): ")
    new_extension = input("Enter the new extension (without dot): ")
    
    # Check if the input is valid
    if not os.path.isfile(original_file_path):
        print("The specified file does not exist.")
    else:
        original_file_name = os.path.basename(original_file_path)
        modified_file_name = apply_rlo(original_file_name, new_extension)
        
        # Rename the file
        new_file_path = rename_file(original_file_path, modified_file_name)
        print(f"File has been renamed to: {new_file_path}")

# Run the main function
if __name__ == "__main__":
    main()
