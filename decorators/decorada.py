from cap7.decorador import replace_special_character


@replace_special_character
def count_characters(*args):
    if args:
        phrase = ' '.join(args)
    l = {i: phrase.count(i) for i in phrase}
    return l


print(count_characters('Olá Meu nome é Paulo Gomes Werneck Junior, eu tenho 27 anos.'))


a = replace_special_character(lambda x: x)
print(a('Páulo Gômes Wernèck Jr'))
