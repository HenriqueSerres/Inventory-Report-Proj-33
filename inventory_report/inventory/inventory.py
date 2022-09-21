import csv
import json
import xmltodict

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def read_file(cls, path: str):
        data_report = []
        with open(path) as file:
            if path.endswith(".csv"):
                return list(csv.DictReader(file, delimiter=",", quotechar='"'))
            if path.endswith(".json"):
                return json.load(file)
            if path.endswith(".xml"):
                content = file.read()
                return xmltodict.parse(content)["dataset"]["record"]

        return data_report

    # vídeo do youtube que assisti para ler arquivo xml:
    # https://www.youtube.com/watch?v=1FBckemKu1Q

    @classmethod
    def import_data(cls, path: str, report_type: str):
        data_report = cls.read_file(path)
        if report_type == "simples":
            return SimpleReport.generate(data_report)
        if report_type == "completo":
            return CompleteReport.generate(data_report)
        else:
            raise ValueError("Algo deu errado")
