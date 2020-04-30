import conta_palavras_livro as cpl


def test_dict_len():
    assert len(cpl.conta_palavra_por_livro()) == 3


def test_prim_chave():
    dic = cpl.conta_palavra_por_livro()
    assert dic[1] == ['Este', 1]


def test_seg_chave():
    dic = cpl.conta_palavra_por_livro()
    assert dic[2] == ['cachorro', 4]


def test_ter_chave():
    dic = cpl.conta_palavra_por_livro()
    assert dic[3] == ['Python', 3]
