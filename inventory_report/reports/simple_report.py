from collections import Counter
from datetime import date


class SimpleReport:
    @staticmethod
    def generate(list):
        today = date.today().strftime("%Y-%m-%d")
        fab = [data["data_de_fabricacao"] for data in list]
        older_fab = min(fab)
        venc = [
            data["data_de_validade"]
            for data in list
            if data["data_de_validade"] < today
        ]
        newest_venc = max(venc)
        industries = Counter([ind["nome_da_empresa"] for ind in list])

        return (
            f"Data de fabricação mais antiga: {older_fab}\n"
            f"Data de validade mais próxima: {newest_venc}\n"
            f"Empresa com mais produtos: {industries.most_common(1)[0][0]}"
        )
