import subprocess
import os

def install(msi_path="", progress_bar=True, restart_if_needed=False, log_file=""):
    
    args = ""
    
    if msi_path == "":
        # Path Missing
        return "Path Missing"
    
    