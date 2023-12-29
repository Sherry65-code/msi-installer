import subprocess
import os

def install(msi_path="", progress_bar=True, disable_ui=False restart_if_needed=False, log_file=""):
    
    args = ""
    
    if msi_path == "":
        # Path Missing
        return "Path Missing"
    
    if progress_bar:
        args += "/passive"
    else:
        args += "/quiet"
    
    if disable_ui:
        args += "/"