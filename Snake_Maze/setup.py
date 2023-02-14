from distutils.core import setup
import py2exe
import readchar
import os
import random

setup(zipfile=None,
      options={"py2exe": {"bundle_files": 1}},
      console=['Snake_Maze.py'])
