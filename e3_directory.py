import os
import shutil

def create_directory_and_copy_files(source_dir, destination_dir):
    try:
        # Ensure destination exists (safe even if it already exists)
        os.makedirs(destination_dir, exist_ok=True)

        # Loop through files in source directory
        for file_name in os.listdir(source_dir):
            source_file = os.path.join(source_dir, file_name)
            destination_file = os.path.join(destination_dir, file_name)

            # Copy only files
            if os.path.isfile(source_file):
                shutil.copy(source_file, destination_file)

        print(f"Files copied from '{source_dir}' to '{destination_dir}'.")

    except Exception as e:
        print(f"An error occurred: {e}")