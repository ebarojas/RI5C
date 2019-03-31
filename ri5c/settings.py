"""
Settings file for ri5c project.

Pretty simple, but with room to grow
"""

# For ENV vars
import os
import ast

# This might removed if local SQL implementation does not move forward
DATABASE_URL = os.environ['DATABASE_URL']
