import os
import subprocess

def install(msi_path="", progress_bar=True, disable_ui=False, restart_if_needed=False, log_file=""):
    """
    Install an MSI file with optional parameters.

    Parameters:
    - msi_path (str): Path to the MSI file.
    - progress_bar (bool): Show progress bar if True, otherwise use quiet mode.
    - disable_ui (bool): Disable UI completely if True, otherwise use basic UI.
    - restart_if_needed (bool): Prompt for restart if needed if True, otherwise do not restart.
    - log_file (str): Path to the log file for installation logs.

    Returns:
    - int: Return code of the installation process.
    """
    if os.name != "nt":
        return -1

    if not os.path.isfile(msi_path):
        # Invalid MSI path
        return -2

    # Use double quotes for paths in CMD
    msi_path = '"{}"'.format(msi_path)
    log_file = '"{}"'.format(log_file) if log_file else ""

    args = 'msiexec /i {} '.format(msi_path)

    if progress_bar:
        args += "/passive"
    else:
        args += "/quiet"
    
    if disable_ui:
        args += " /qn"
    else:
        args += " /qb"

    if restart_if_needed:
        args += " /promptrestart"
    else:
        args += " /norestart"
    
    if log_file:
        if not os.path.exists(os.path.dirname(log_file)):
            # Invalid log file path
            return -3
        args += ' /log {}'.format(log_file)

    result = subprocess.run(args, shell=True, check=True)

    return result.returncode

if __name__ == "__main__":
    # Get input from the user
    msi_path = input("Enter the path to the MSI file: ")
    progress_bar = input("Show progress bar? (y/n): ").lower() == 'y'
    disable_ui = input("Disable UI completely? (y/n): ").lower() == 'y'
    restart_if_needed = input("Prompt for restart if needed? (y/n): ").lower() == 'y'
    log_file = input("Enter the path to the log file (leave empty for no log): ")

    # Call the install function with user input
    return_code = install(msi_path=msi_path, progress_bar=progress_bar, disable_ui=disable_ui, restart_if_needed=restart_if_needed, log_file=log_file)
    print(f"Installation completed with return code: {return_code}")
