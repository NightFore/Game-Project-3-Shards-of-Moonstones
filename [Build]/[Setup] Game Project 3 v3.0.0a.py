import cx_Freeze
import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

executables = [cx_Freeze.Executable("[Game Project 3] Shards of Moonstones v3.0.0a.py")]

cx_Freeze.setup(
    name="Shards of Moonstones",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["Data", "readme.txt",
                                             "0.0.0_None.txt", "0.0.1_Cutscene_Introduction.txt", "0.0.2_Cutscene_Introduction.txt",
                                             "0.1.1_Cutscene_Introduction_2.txt",
                                             "1.0.0_Victory.txt"]}},
    executables=executables,
    version="3.0.0"
)
