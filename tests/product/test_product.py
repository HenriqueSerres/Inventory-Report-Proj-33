from inventory_report.inventory.product import Product


def test_cria_produto():
    fake_product = Product(
        1,
        "xablau",
        "Xablau S/A",
        "09-20-2021",
        "10-20-2022",
        "turma17",
        "estude muito",
    )

    assert fake_product.id == 1
    assert fake_product.nome_do_produto == "xablau"
    assert fake_product.nome_da_empresa == "Xablau S/A"
    assert fake_product.data_de_fabricacao == "09-20-2021"
    assert fake_product.data_de_validade == "10-20-2022"
    assert fake_product.numero_de_serie == "turma17"
    assert fake_product.instrucoes_de_armazenamento == "estude muito"
