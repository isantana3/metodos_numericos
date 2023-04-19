# Metodos Numéricos

## Repositório com a implementação e documentação de calculo numérico.

### Teoria por trás:

Neste repositório não pretendo me aprofundar muito na teoria, mas o arquivo "Relatório das implementações" deve ajudar em algo, por mais que a ideia dele seja explicar como fiz e não a teoria por trás de cada método.

### Para rodar:

#### Pacotes externos:

Meu projeto, até o momento tonta com somente uma lib extenar, a **Sympy**, para instalá-la, basta executar:
''' pip install sympy'''
ou
''' pip3 install sympy'''

#### Executando:

O repositório já conta com arquivos de input e output, porém nada te impede de dita-lo e usar seus prórpios inputs e outputs. Isso não deve ser difícil, tendo em vista que cada arquivo já tem de certo modo um exemplo da formatação dos dados, as funções de leitura de arquivo também, e até no relatório tem explicando com exemplos.
Para usuários de linux, basta usar os comandos do makefile para executar cada método.
Para usuários do windows, aconselho copiar e colar os comandos do makefile no cmd ou powershell.
Importante ressaltar que independente do método utilizado apra executar o código, a execução deverá ser feita na pasta raiz do projeto, caso execute diretamnete na pasta do método, o programa retornará erro.
Exemplo de como rodar:
''' python3 implementations/metodo_desejado.py '''
