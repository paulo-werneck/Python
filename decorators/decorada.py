from cap7.decorador import replace_special_character


@replace_special_character
def count_characters(*args):
    """
        Funcao para contar a quantidade de cada caracteres de uma determinada palavra / frase ou tupla de strings.
        
        param1: *args - Parametros variados, aceita varias strings separadas por virgula ou uma tupla de strings desempacotada
        return: dicionario, sendo chave = caracter a ser contado / valor = a quantidade de vezes que o caracter aparece
    """
    if args:
        phrase = ' '.join(args)
    l = {i: phrase.count(i) for i in phrase}
    return l


print(count_characters('Olá Meu nome é Paulo Gomes Werneck Junior, eu tenho 27 anos.'))


a = replace_special_character(lambda x: x)
print(a('Páulo Gômes Wernèck Jr'))
