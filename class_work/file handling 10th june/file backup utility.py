# Prompt the user to enter the name of the file they want to copy
source_file = input("Enter Source File Name  : ")

# Prompt the user to enter the name of the new backup file
destination_file = input("Enter Destination File Name : ")

try:
    # Open the source file in 'read' mode ('r')
    with open(source_file, 'r') as src:
        # Read the entire content of the source file into a variable
        content = src.read()

    # Open the destination file in 'write' mode ('w')
    # This will create the file if it doesn't exist or overwrite it if it does
    with open(destination_file, 'w') as dest:
        # Write the stored content into the destination file
        dest.write(content)

    # Print a blank line and the success messages as per the expected output
    print(f"\nFile copied successfully.")
    print(f"All contents from '{source_file}' have been copied to '{destination_file}'.")

except FileNotFoundError:
    # Handle the error if the source file name entered does not exist
    print(f"Error: The file '{source_file}' was not found.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"An error occurred: {e}")