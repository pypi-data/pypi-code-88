# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

import json
from restclients_core import models
from uw_attest.utils import str_to_datetime, date_to_str


class Covid19Attestation(models.Model):
    regid = models.CharField(max_length=32)
    is_student = models.BooleanField(default=False)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    def __init__(self, *args, **kwargs):
        super(Covid19Attestation, self).__init__(*args, **kwargs)
        self.vaccinated = None
        self.exemption = None

    @staticmethod
    def from_json(json_data):
        ca_obj = Covid19Attestation()
        ca_obj.regid = json_data.get("regId")
        ca_obj.is_student = json_data.get("isStudent")
        ca_obj.created = str_to_datetime(json_data.get("created"))
        ca_obj.updated = str_to_datetime(json_data.get("updated"))
        if json_data.get("vaccinated"):
            ca_obj.vaccinated = Vaccinated.from_json(
                json_data.get("vaccinated"))
        if json_data.get("exemption"):
            ca_obj.exemption = Exemption.from_json(
                json_data.get("exemption"))
        return ca_obj

    def json_data(self):
        return {
            "regid": self.regid,
            "is_student": self.is_student,
            "created": date_to_str(self.created),
            "updated": date_to_str(self.updated),
            "vaccinated": (
                self.vaccinated.json_data() if self.vaccinated else None),
            "exemption": (
                self.exemption.json_data() if self.exemption else None),
        }

    def __str__(self):
        return json.dumps(self.json_data(), default=str)


class Vaccinated(models.Model):
    vaccine = models.CharField(max_length=64)
    country_code = models.CharField(max_length=2, default="US")
    dose1_date = models.DateTimeField()
    dose2_date = models.DateTimeField(null=True, default=None)
    other_text = models.CharField(max_length=100, null=True)

    @staticmethod
    def from_json(json_data):
        vac_obj = Vaccinated()
        vac_obj.vaccine = json_data.get("vaccine")
        vac_obj.country_code = json_data.get("country")
        vac_obj.dose1_date = str_to_datetime(json_data.get("dose1Date"))
        vac_obj.dose2_date = str_to_datetime(json_data.get("dose2Date"))
        vac_obj.other_text = json_data.get("otherText")
        return vac_obj

    def json_data(self):
        return {
            "vaccine": self.vaccine,
            "country_code": self.country_code,
            "dose1_date": date_to_str(self.dose1_date),
            "dose2_date": date_to_str(self.dose2_date),
            "other_text": self.other_text,
        }


class Exemption(models.Model):
    type = models.CharField(max_length=64)

    @staticmethod
    def from_json(json_data):
        exe_obj = Exemption()
        exe_obj.type = json_data.get("type")
        return exe_obj

    def json_data(self):
        return {"type": self.type}
