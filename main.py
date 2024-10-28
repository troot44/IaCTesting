# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28, 2024

@author: Thomas Root (for W9)
"""
from util import Util
from iac_testing_antipatterns import IaCTestingAntipatterns

def main():
    
    
    
    base_dir= input("Please enter the directory: ")
    print("\n")
    
    
    project_name = input ("Please enter the project name: ")
    print(project_name)
    
    print("Testing branch")
    
    files = Util().get_files(base_dir)
#    print(files)
    
#    quit()
    
    iac_testing_antipatterns = IaCTestingAntipatterns(files, project_name)
#    
    iac_testing_antipatterns.get_anti_pattern_list()
#    
if __name__ == "__main__":
    main()
