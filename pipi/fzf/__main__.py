from subprocess import call
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

call(f"{dir_path}/run.sh", shell=True)
