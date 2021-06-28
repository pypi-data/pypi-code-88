from glob import glob
import os
import fnmatch
import json
import pyvista as pv
import pandas as pd
import numpy as np
import sqlite3

class Nastja():
  def __init__(self, path):
    """
    Constructs a new instance.

    :param path:  The path.
    """
    self.__basename = "output_cells-"
    self.__hasVTI = False
    self.__hasCSV = False
    self.__hasSQL = False
    self.__frames = 0
    self.__configname = "config_save.json"
    self.__con = 0
    self.path = path

  @property
  def path(self):
    return self.__path

  @path.setter
  def path(self, path):
    self.__path = os.path.expanduser(path)
    self.reload()

  @property
  def hasVTI(self):
    return self.__hasVTI

  @property
  def hasCSV(self):
    return self.__hasCSV

  @property
  def hasSQL(self):
    return self.__hasSQL

  @property
  def frames(self):
    return self.__frames

  def __maximumFrame(self, files):
    """
    Determine the maximum available frame from a filelist. Checks also if the frames are continues.

    :param files:  The files.

    :returns: The maximum available frames
    """
    if len(files) != int(files[-1][-9:-4]) + 1:
      raise NameError("Frame numbers are not complete")

    return len(files)

  def reload(self):
    """
    Reload vti, csv file from path and determine the largest frames.
    This function is called when the path is set.
    """
    files = os.listdir(self.path)

    vti = fnmatch.filter(files, self.__basename + "[0-9][0-9][0-9][0-9][0-9].vti")
    csv = fnmatch.filter(files, self.__basename + "[0-9][0-9][0-9][0-9][0-9].csv")
    sql = fnmatch.filter(files, "*.sqlite")

    framesvti = 0
    if vti:
      vti.sort()
      self.__hasVTI = True
      framesvti = self.__maximumFrame(vti)

    framescsv = 0
    if csv:
      csv.sort()
      self.__hasCSV = True
      framescsv = self.__maximumFrame(csv)

    framessql = 0
    if sql:
      self.__hasSQL = True
      if len(sql) > 1:
        print("Found more than one database. Loading", sql[0])

      self.__con = sqlite3.connect(self.__path + "/" + sql[0])
      cur = self.__con.cursor()
      row = cur.execute("SELECT MAX(frame) FROM cells").fetchone()
      framessql = row[0] + 1

    self.__frames = max(framesvti, framescsv, framessql)

    if (self.hasVTI and self.__frames != framesvti) or (self.hasCSV and self.__frames != framescsv) or (self.hasSQL and self.__frames != framessql) :
      raise NameError("Data types vary in frame numbers")

  def __createFilename(self, frame, extension):
    return self.path + "/" + self.__basename + "%05d"%frame + extension

  def readVTI(self, frame):
    """
    Reads a vti file.

    :param frame:  The frame.
    """
    return pv.read(self.__createFilename(frame, ".vti"))

  def readCSV(self, frame):
    """
    Reads a csv file.

    :param frame:  The frame.
    """
    data = pd.read_csv(self.__createFilename(frame, ".csv"), sep=" ")
    return data.rename(columns={"#CellID" : "CellID"})

  def readSQL(self, frame):
    """
    Reads a sql file.

    :param frame:  The frame.
    """
    if not self.__con:
      raise NameError("No database connection found")

    data = pd.read_sql_query("SELECT CellID, CenterX, CenterY, CenterZ, Volume, Surface, Typ, Signal0, Signal1, Signal2, Age from cells WHERE frame=" + str(frame) + ";", self.__con)
    return data

  def query(self, query):
    """
    Queries a sql file.

    :param query:  The query.
    """
    if not self.__con:
      raise NameError("No database connection found")

    data = pd.read_sql_query(query, self.__con)
    return data

  def readConfig(self):
    """
    Reads a configuration.
    """
    with open(self.path + "/" + self.__configname) as json_file:
      return json.load(json_file)

  def mappedArray(self, array, df, column):
    """
    Create a mapped array, replace cellID with the value of the given column.

    :param array:   The numpy array.
    :param df:      The data frame.
    :param column:  The name of the column.

    :returns: mapped array.
    """
    ret = np.empty(array.shape)
    for index, row in df.iterrows():
      ret[array == row["CellID"]] = row[column]
    return ret
