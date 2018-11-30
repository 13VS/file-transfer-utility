import os
from shutil import copyfile
def copy(name):
    script_dir = os.path.dirname(__file__)
    rel_path1 = "REPORTS/CDW/EMEA/"+name
    rel_path2 = "ACNIL/REPORTS/CDW/EMEA/"+name
    abs_file_path1 = os.path.join(script_dir, rel_path1)
    abs_file_path2 = os.path.join(script_dir, rel_path2)
    copyfile(abs_file_path1,abs_file_path2)
    return