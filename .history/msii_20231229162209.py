import subprocess
import os

def install(msi_path="", progress_bar=True, disable_ui=False, restart_if_needed=False, log_file=""):
        
    if msi_path == "":
        # Path Missing
        return "Path Missing"
    
    args = "msiexec /i {} ".format(msi_path)

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
    
    if log_file != "":
        args += " /log {}".format(log_file)

    args_arr = args.split(" ")

    subprocess.run(args_arr, check=True)

    