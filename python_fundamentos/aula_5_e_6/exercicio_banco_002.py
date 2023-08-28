# Neste exercício, você criará uma hierarquia de classes envolvendo uma classe abstrata Pessoa, com subclasses Aluno e Professor.
# Cada classe deve implementar métodos específicos, usando conceitos de abstração, herança e programação orientada a objetos (POO).
# Crie uma classe abstrata chamada Pessoa com o método abstrato exibir_info() e calcular_salario().
# Implemente o método exibir_info() para exibir informações básicas da pessoa, como nome e idade.
# Implemente o método calcular_salario() como um método abstrato, que será diferente para cada subclasse.
# Crie uma subclasse Aluno que herde da classe Pessoa.
# Implemente o método exibir_info() para exibir informações específicas de um aluno, como nome, idade e número de matrícula.
# Implemente o método calcular_salario() para alunos, que, neste caso, não se aplica. Pode ser um método vazio.
# Crie uma subclasse Professor que herde da classe Pessoa.
# Implemente o método exibir_info() para exibir informações específicas de um professor, como nome, idade e disciplina lecionada.
# Implemente o método calcular_salario() para professores, calculando o salário com base na carga horária e valor por hora.
# Crie instâncias de Aluno e Professor.
# Chame o método exibir_info() para cada instância para verificar a exibição correta das informações.
# Chame o método calcular_salario() para o professor e exiba o valor calculado.
# Utilize a biblioteca sqlite3 para criar uma tabela chamada Pessoas com os campos tipo (para distinguir entre aluno e professor),
# nome, idade, info_extra (número de matrícula para aluno, disciplina para professor) e salario (nullable para aluno).
# Implemente métodos para adicionar instâncias de Aluno e Professor à tabela Pessoas, extraindo as informações dos métodos exibir_info()
# e calcular_salario() e outros métodos que trabalhem comandos SQL atráves de métodos / funções em Python.

