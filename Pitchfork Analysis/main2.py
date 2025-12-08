import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import numpy as np

con = sqlite3.connect(r"C:\Users\seanandrew\Desktop\datasets\archive (4)\database.sqlite")

reviews = pd.read_sql("SELECT * FROM reviews", con)
artists = pd.read_sql("SELECT * FROM artists", con)
genres = pd.read_sql("SELECT * FROM genres", con)

def __init__ (self, db_path):
    """Initialize with database path"""
    self.db_path = r"C:\Users\seanandrew\Desktop\datasets\archive (4)\database.sqlite"
    self.reviews = None
    self.artists = None
    self.genres = None
    self.