import grimoire

while True:
    text = input('Grimoire> ')
    result, error = grimoire.run('<stdin>',text)

    if error:print(error.as_string())
    else:print(result)