from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, lista):
        simple_rep = super().generate(lista)
        industries = Counter([ind["nome_da_empresa"] for ind in lista])
        # complete_rep = [f'- {a}: {b}\n' for a, b in industries.items()]
        complete_rep = ''
        for a, b in industries.items():
            complete_rep += f"- {a}: {b}\n"
        return (
          f'{simple_rep}\n'
          f'Produtos estocados por empresa:\n'
          f'{complete_rep}'
        )
