import os
import subprocess
import sys

subprocess.run(['bash','sudo apt-get install -y fonts-nanum', 'sudo fc-cache -fv', 'rm ~/.cache/matplotlib -rf'])