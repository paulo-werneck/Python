def replace_special_character(func):
    """
        Funcao decoradora para remover caracteres especiais
        
        param1: func - funcao a ser decorada
        return: funcao decorada com caracteres especiais removidos
    """
    def fn_decorada_characters(*args):
        fnc = func(*args)
        dict_char = {
            'a': list('áàâãäå'), 'A': list('ÁÀÂÃÄÅ'),
            'e': list('éèêẽë'), 'E': list('ÉÈÊẼË'),
            'i': list('íìîĩï'), 'I': list('ÍÌÎĨÏ'),
            'o': list('óòôõö'), 'O': list('ÓÒÔÕÖ'),
            'u': list('úùûũü'), 'U': list('ÚÙÛŨÜ')
        }
        if args:
            text = ' '.join(args)
        for k, v in dict_char.items():
            for letter in v:
                if letter in text:
                    text = text.replace(letter, k)
        return func(text)
    return fn_decorada_characters
