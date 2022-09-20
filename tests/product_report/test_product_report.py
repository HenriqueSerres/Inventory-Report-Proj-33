from inventory_report.inventory.product import Product


def test_relatorio_produto():
    fake_product = Product(
        1,
        "xablau",
        "Xablau S/A",
        "09-20-2021",
        "10-20-2022",
        "turma17",
        "estude muito",
    )
    assert fake_product.__repr__() == (
        "O produto xablau"
        " fabricado em 09-20-2021"
        " por Xablau S/A com validade"
        " até 10-20-2022"
        " precisa ser armazenado estude muito."
    )
