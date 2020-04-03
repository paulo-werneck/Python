def replace_special_character(text):
    dict_char = {
        'a': list('áàâãäå'), 'A': list('ÁÀÂÃÄÅ'),
        'e': list('éèêẽë'), 'E': list('ÉÈÊẼË'),
        'i': list('íìîĩï'), 'I': list('ÍÌÎĨÏ'),
        'o': list('óòôõö'), 'O': list('ÓÒÔÕÖ'),
        'u': list('úùûũü'), 'U': list('ÚÙÛŨÜ')
    }
    for k, v in dict_char.items():
        for letter in v:
            if letter in text:
                text = text.replace(letter, k)
    return text


fn = replace_special_character('páulo gômés wÉrneck júnior')

print(fn)
