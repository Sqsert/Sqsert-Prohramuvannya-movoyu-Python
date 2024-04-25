def find_words_with_o(sentence):
    words = sentence.split()

    words_with_o = [word for word in words if 'о' in word.lower()]

    if words_with_o:
        print("Слова, які містять літеру 'о':", words_with_o)
    else:
        print("У реченні відсутні слова, які містять літеру 'о'.")

sentence = input("Введіть речення: ")

find_words_with_o(sentence)
