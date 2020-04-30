class Pessoa:
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade

    def get_nome(self) -> str:
        return self._nome

    def get_idade(self) -> int:
        return self._idade

    def envelhece(self) -> None:
        self._idade += 1


class Aluno:
    def __init__(self, nome: str, idade: int, curso: str, ra: int):
        self._nome = nome
        self._idade = idade
        self._ra = ra
        self._curso = curso
    
    def get_ra(self) -> int:
        return self._ra

    def get_curso(self) -> str:
        return self._curso

    def set_curso(self, novo_curso: str) -> None:
        self._curso = novo_curso


class Professor(Pessoa):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.disciplina = None

    def get_nome(self) -> str:
        return 'Prof. ' + super().get_nome()
    
    def ministrar(self, disciplina: str) -> None:
        self.disciplina = disciplina

    def disciplinas(self):
        return self.disciplina

    def envelhece(self):
        super().envelhece()
        super().envelhece()
    


if __name__ == '__main__':
    prof_lp2 = Professor('Fulano', 28)
    prof_tecweb = Professor('Cicrano', 50)
    prof_lp2.ministrar('LpII')

    print(prof_lp2.disciplinas())
    print(prof_tecweb.disciplinas())

    prof_lp2.envelhece()
    print(prof_lp2.get_idade())
    print(prof_lp2.get_nome())
 