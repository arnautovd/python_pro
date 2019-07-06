from first_module import name, surname

print(name + " " + surname)



while True:

    word = input("Твое слово: ")

    def getLetter(word):
        index = input("Твой индекс: ")
        try:
            return word[int(index)]
        except IndexError:
            print("Словили ошибку")

    print(getLetter(word))