import os
import sys

os.environ['TCL_LIBRARY'] = r'C:\Users\my\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\my\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":  
    base = "Win32GUI"  

executables = [Executable("dframe.py", base=base)]

packages = ["idna"]
addtional_mods = ['numpy.core._methods', 'numpy.lib.format', 'tkinter.filedialog']
options = {
    'build_exe': {
        'packages': packages, "include_files": ["tcl86t.dll", "tk86t.dll"], 'includes': addtional_mods
    },

}

setup(
    name = "dataframe",
    options = options,
    version = "1.0",
    description = 'plot the excel data',
    executables = executables
)