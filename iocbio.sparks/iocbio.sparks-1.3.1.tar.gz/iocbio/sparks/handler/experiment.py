# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  Copyright (C) 2018
#   Laboratory of Systems Biology, Department of Cybernetics,
#   School of Science, Tallinn University of Technology
#  Authors: Martin Laasmaa and Marko Vendelin
#  This file is part of project: IOCBIO Sparks
#
# UNITS: Time in the database is stored in milliseconds. Analysis range is kept
# in the program in seconds. Hence unit transformation between loading and
# storing data.

from iocbio.sparks.constants import database_table_experiment, database_table_roi, database_table_spark, database_table_stage

import PyQt5.QtCore as QC
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject
from collections import namedtuple
import numpy as np

PDesc = namedtuple("PDesc", ["human", "default", "sqltype", "pytype"])
Parameters = {
    "name": PDesc("Name of the stage", "", "TEXT", str),
    "start": PDesc("Start of the experiment stage [ms]", 0.0, "DOUBLE PRECISION", float),
    "end": PDesc("End of the experiment stage [ms]", 0.0, "DOUBLE PRECISION", float),
}

RDesc = namedtuple("RDesc", ["human", "unit"])
Results = {
    "min": RDesc("Minimum", "AU"),
    "max": RDesc("Maximum", "AU"),
    "mean": RDesc("Mean", "AU"),
    "percentile001": RDesc("Percentile 0.1%", "AU"),
    "percentile999": RDesc("Percentile 99.9%", "AU"),
}
ResultsOrder = ["min", "max", "mean", "percentile001", "percentile999"]

class ExperimentHandler(QObject):
    """General information regarding experiment"""

    database_table = database_table_experiment
    settings_group = "Experiment"

    database_table_stages = database_table_stage

    database_table_extended = database_table_experiment + "_extended"

    sigStages = pyqtSignal(dict, list)
    sigIntesityChanged = pyqtSignal(np.ndarray)

    @staticmethod
    def database_schema(db, create_view=True):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(ExperimentHandler.database_table) +
                 "(experiment_id text not null PRIMARY KEY, " +
                 "filename text, comment text, duration DOUBLE PRECISION, length DOUBLE PRECISION, " +
                 "pixels_time INTEGER, pixels_space INTEGER, space_x0_pixels INTEGER, space_x1_pixels INTEGER, " +
                 "transposed INTEGER DEFAULT 0)")

        if create_view and not db.has_view(ExperimentHandler.database_table_extended):
            db.query("CREATE VIEW " + db.table(ExperimentHandler.database_table_extended) +
                     " AS SELECT *, (SELECT COUNT(*) FROM " + db.table(database_table_spark) +  " s JOIN " +
                     db.table(database_table_roi) + " r ON s.roi_id=r.roi_id WHERE r.experiment_id=e.experiment_id) AS spark_count FROM " +
                     db.table(ExperimentHandler.database_table) + " e")

        # stages table
        psql = ""
        keys = list(Parameters.keys())
        keys.sort()
        for k in keys:
            psql += '"' + k + '"' + " " + Parameters[k].sqltype +","

        keys = list(Results.keys())
        keys.sort()
        for k in keys:
            psql += k + " DOUBLE PRECISION,"

        db.query("CREATE TABLE IF NOT EXISTS " + db.table(ExperimentHandler.database_table_stages) +
                 "(experiment_id text, stage_id text PRIMARY KEY, spark_analysis INTEGER, " + psql +
                 "FOREIGN KEY (experiment_id) REFERENCES " + db.table(ExperimentHandler.database_table) + "(experiment_id) ON DELETE CASCADE)")

    @staticmethod
    def database_schema_update_6_7(db):
        db.query("ALTER TABLE " + db.table(ExperimentHandler.database_table) + " ADD space_x0_pixels INTEGER")
        db.query("ALTER TABLE " + db.table(ExperimentHandler.database_table) + " ADD space_x1_pixels INTEGER")
        db.query("UPDATE "  + db.table(ExperimentHandler.database_table) + " SET space_x0_pixels=0, space_x1_pixels=pixels_space")

    @staticmethod
    def set_defaults(defaults):
        settings = QC.QSettings()
        if "bg" in defaults:
            settings.setValue(ExperimentHandler.settings_group + "/bg", defaults["bg"])

    @staticmethod
    def delete(db, experiment_id):
        if db is not None:
            db.query("DELETE FROM " + db.table(ExperimentHandler.database_table) +
                     " WHERE experiment_id=:eid",
                     eid=experiment_id)

    @staticmethod
    def has_record(db, experiment_id):
        return db.has_record(ExperimentHandler.database_table, experiment_id=experiment_id)


    def __init__(self, experiment_id, filename, comment, database, image, transposed):
        QObject.__init__(self)

        settings = QC.QSettings()

        self.experiment_id = experiment_id
        self.comment = comment
        self.filename = filename
        self.database = database
        self.image = image
        pixTime, pixX = self.image.raw.shape
        self.dx, self.dt = self.image.dx, self.image.dt
        self.duration = self.dt*pixTime
        self.length = self.dx*pixX
        self.tdata = self.dt*np.arange(0, pixTime)
        self.background = float(settings.value(ExperimentHandler.settings_group + "/bg", 0.0))
        self.analysis_range = [0.05*self.duration, 0.95*self.duration]
        self.analysis_range_space = [0, self.length]
        self.update_xdata()
        self.stages = {}
        self.spark_stage_id = None
        self.stage_name_counter = 0

        if self.database is not None:
            record_found = False
            for row in self.database.query("SELECT comment FROM " +
                                           self.database.table(ExperimentHandler.database_table) +
                                           " WHERE experiment_id=:eid", eid=self.experiment_id):
                self.comment = row['comment']
                record_found = True

            if not record_found:
                sx0, sx1 = self.analysis_range_pixels[1]
                self.database.query("INSERT INTO " + self.database.table(ExperimentHandler.database_table) +
                                    "(experiment_id, filename, comment, duration, length, pixels_time, pixels_space, space_x0_pixels, space_x1_pixels, transposed) " +
                                    "VALUES(:eid, :fname, :comm, :dur, :l, :pt, :px, :sx0, :sx1, :transp)",
                                    eid=self.experiment_id, fname=self.filename, comm=self.comment,
                                    dur=self.duration*1e3, l=self.length*1e6, pt=pixTime, px=pixX, sx0=sx0, sx1=sx1, transp=transposed)

            # load stages
            psql = "stage_id, spark_analysis, "
            kfull = ["stage_id", "spark_analysis"]
            keys = list(Parameters.keys())
            for k in keys:
                psql += '"' + k + '",'
            psql = psql[:-1]
            kfull.extend(keys)
            keys = kfull
            for row in self.database.query("SELECT " + psql + " FROM " +
                                           self.database.table(ExperimentHandler.database_table_stages) +
                                           ' WHERE experiment_id=:eid ORDER BY "start", "end"', eid=self.experiment_id):
                stage = {}
                for i in range(len(keys)):
                    stage[keys[i]] = row[i]
                stage["start"]/=1e3
                stage["end"]/=1e3
                if stage["spark_analysis"] > 0:
                    self.spark_stage_id = stage["stage_id"]
                self.stages[stage["stage_id"]] = stage

            if self.spark_stage_id is None:
                self.add_stage(name="Spark analysis",
                               spark_analysis_stage = True,
                               rng = self.analysis_range)
            else:
                stage = self.stages[self.spark_stage_id]
                self.analysis_range = [stage["start"], stage["end"]]

            row = self.database.query("SELECT space_x0_pixels, space_x1_pixels FROM " + self.database.table(ExperimentHandler.database_table) +
                                      " WHERE experiment_id=:eid", eid=self.experiment_id)[0]

            self.analysis_range_space = [self.dx*row['space_x0_pixels'], self.dx*row['space_x1_pixels']]

        self.update_xdata()

    def set(self, analysis_range=None, analysis_range_space=None, comment=None):
        if analysis_range is not None:
            self.analysis_range = analysis_range
            self.update_stage_range(self.spark_stage_id, self.analysis_range)

        if analysis_range_space is not None:
            self.analysis_range_space = analysis_range_space
            if self.database is not None:
                sx0, sx1 = self.analysis_range_pixels[1]
                self.database.query("UPDATE " + self.database.table(ExperimentHandler.database_table) +
                                    " SET space_x0_pixels=:sx0, space_x1_pixels=:sx1 WHERE experiment_id=:eid",
                                    sx0=sx0, sx1=sx1, eid=self.experiment_id)
        if comment is not None:
            self.comment = comment
            if self.database is not None:
                self.database.query("UPDATE " + self.database.table(ExperimentHandler.database_table) +
                                    " SET comment=:comm WHERE experiment_id=:eid", comm=self.comment, eid=self.experiment_id)

    def set_analysis_range(self, rng):
        self.set(analysis_range=rng)
        self.update_image()

    def set_analysis_range_space(self, rng):
        self.set(analysis_range_space=rng)
        self.update_xdata()
        self.update_image()

    def update_image(self):
        self.image.normalize(*self.analysis_range, *self.analysis_range_space)

    def add_stage(self, name = None, spark_analysis_stage = False, rng = None):
        import uuid
        if name is None:
            self.stage_name_counter+=1
            name = "stage-%d" % self.stage_name_counter
        if rng is None:
            rng = [0.05*self.duration, 0.10*self.duration]
        stage_id = str(uuid.uuid4())

        analysis = 1 if spark_analysis_stage else 0

        self.stages[stage_id] = {
            "stage_id": stage_id,
            "name": name,
            "start": rng[0],
            "end": rng[1],
            "spark_analysis": analysis,
        }

        if spark_analysis_stage:
            self.spark_stage_id = stage_id

        if self.database is not None:
            self.database.query("INSERT INTO " + self.database.table(ExperimentHandler.database_table_stages) +
                                '(experiment_id, stage_id, spark_analysis, name, "start", "end") VALUES(:eid,:sid,:ana,:name,:s,:e)',
                                eid=self.experiment_id, sid=stage_id, ana=analysis, name=name, s=rng[0]*1e3, e=rng[1]*1e3)

        self.analyze_stage(stage_id)

    def update_xdata(self):
        x0, x1 = self.analysis_range_pixels[1]
        self.xdata = self.image.raw[:,x0:x1].mean(axis=1).astype(np.float64)
        if hasattr(self, 'stages'):
            self.analyze_all_stages()
        self.sigIntesityChanged.emit(self.xdata)

    def update_stage_range(self, stage_id, rng):
        if stage_id not in self.stages: return

        stage = self.stages[stage_id]
        stage["start"], stage["end"] = rng[0], rng[1]
        if self.database is not None:
            self.database.query("UPDATE " + self.database.table(ExperimentHandler.database_table_stages) +
                                ' SET "start"=:s, "end"=:e ' +
                                "WHERE experiment_id=:eid AND stage_id=:sid",
                                s=stage["start"]*1e3, e=stage["end"]*1e3,
                                eid=self.experiment_id, sid=stage["stage_id"])
        self.stages[stage_id] = stage
        self.analyze_stage(stage_id)

    def update_stage_name(self, stage_id, name):
        if stage_id not in self.stages: return
        self.stages[stage_id]["name"] = name
        if self.database is not None:
            self.database.query("UPDATE " + self.database.table(ExperimentHandler.database_table_stages) +
                                " SET name=:name " +
                                "WHERE experiment_id=:eid AND stage_id=:sid",
                                name=name, eid=self.experiment_id, sid=stage_id)

        self.sigStages.emit(self.stages, self.sorted_stage_list)

    def remove_stage(self, stage_id):
        if stage_id not in self.stages: return
        del self.stages[stage_id]
        if self.database is not None:
            self.database.query("DELETE FROM " + self.database.table(ExperimentHandler.database_table_stages) +
                                " WHERE experiment_id=:eid AND stage_id=:sid",
                                eid=self.experiment_id, sid=stage_id)
        self.sigStages.emit(self.stages, self.sorted_stage_list)

    def analyze_stage(self, stage_id):
        stage = self.stages[stage_id]
        t0 = stage["start"]
        t1 = stage["end"]
        i0 = np.argmin(np.abs(self.tdata-t0))
        i1 = np.argmin(np.abs(self.tdata-t1))
        stage["min"] = self.xdata[i0:i1].min()
        stage["max"] = self.xdata[i0:i1].max()
        stage["mean"] = self.xdata[i0:i1].mean()
        stage["percentile999"] = np.percentile(self.xdata[i0:i1],99.9)
        stage["percentile001"] = np.percentile(self.xdata[i0:i1],0.1)
        self.stages[stage_id] = stage

        if self.database is not None:
            self.database.query("UPDATE " + self.database.table(ExperimentHandler.database_table_stages) +
                                " SET min=:mn, max=:mx, mean=:mean, percentile001=:p001, percentile999=:p999 " +
                                "WHERE experiment_id=:eid AND stage_id=:sid",
                                mn=stage["min"], mx=stage["max"], mean=stage["mean"], p001=stage["percentile001"], p999=stage["percentile999"],
                                eid=self.experiment_id, sid=stage["stage_id"])

        self.sigStages.emit(self.stages, self.sorted_stage_list)

    def analyze_all_stages(self):
        for key in self.stages.keys():
            self.analyze_stage(key)

    def trigger_updates(self):
        self.sigStages.emit(self.stages, self.sorted_stage_list)

    @property
    def analysis_range_pixels(self):
        t = [int(i) for i in np.round(np.array(self.analysis_range)/self.dt, 0)]
        x = [int(i) for i in np.round(np.array(self.analysis_range_space)/self.dx, 0)]
        return t, x

    @property
    def sorted_stage_list(self):
        if self.database is None:
            return []
        else:
            l = self.database.query("SELECT stage_id FROM " +
                                    self.database.table(ExperimentHandler.database_table_stages) +
                                    ' WHERE experiment_id=:eid AND stage_id<>:sid ORDER BY "start","end" ASC',
                                    eid=self.experiment_id,sid=self.spark_stage_id)

            s = [el[0] for el in l]
            if self.spark_stage_id is not None:
                s = [self.spark_stage_id] + s
            return s
