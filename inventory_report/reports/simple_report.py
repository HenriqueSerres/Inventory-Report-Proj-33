from collections import Counter
from datetime import date


class SimpleReport:
    @staticmethod
    def generate(lista):
        today = date.today().strftime("%Y-%m-%d")
        fab = [data["data_de_fabricacao"] for data in lista]
        older_fab = min(fab)
        venc = [
            data["data_de_validade"]
            for data in lista
            if data["data_de_validade"] >= today
        ]
        newest_venc = min(venc)
        industries = Counter([ind["nome_da_empresa"] for ind in lista])

        return (
            f"Data de fabricação mais antiga: {older_fab}\n"
            f"Data de validade mais próxima: {newest_venc}\n"
            f"Empresa com mais produtos: {industries.most_common(1)[0][0]}"
        )
