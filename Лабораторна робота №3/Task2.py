def find_unique_letters(word1, word2):
    letters1 = set(word1)
    letters2 = set(word2)

    unique_letters = letters1.symmetric_difference(letters2)

    if unique_letters:
        print("Літери, які зустрічаються у обох словах тільки один раз:", unique_letters)
    else:
        print("В обох словах відсутні літери, які зустрічаються тільки один раз")

word1 = input("Введіть перше слово: ")
word2 = input("Введіть друге слово: ")

find_unique_letters(word1, word2)
