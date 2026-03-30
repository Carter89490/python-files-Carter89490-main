import subprocess

def run_shell_command(command):
    try:
        # Use subprocess to run the provided shell command
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )
        # Print the output and any errors
        print("Command Output:")
        print(result.stdout)
        # if error, print the error
        if result.stderr:
            print("Errors:")
            print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")