import subprocess
import os

def install(msi_path="", progress_bar=True, restart_if_needed=False, log_file=""):
    if msi_path == "":
        # 