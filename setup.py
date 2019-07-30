# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 22:36:37 2019

@author: akile
"""

from cx_Freeze import setup, Executable

base = None    

executables = [Executable("C:\Users\akile\OneDrive\Documents\github\Random-Groups-Generator", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<any name>",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)