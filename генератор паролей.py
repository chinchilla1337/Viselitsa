import random
digits= "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation="!#$%&*+-=?@^_"

num = int(input("Количество паролей: "))


def generate_password(l,chars):
    return "".join((random.sample(chars, l)))


for _ in range(num):
    included,includeu,includel,includep,includee = input("Включать ли в пароль цифры?"), input("Включать ли в пароль строчные буквы?"), input("Включать ли в пароль закглавные буквы?"), input("Включать ли в пароль знаки?"), input("Исключать ли неоднозначные символы?")
    li = [included,includeu,includel,includep,includee, digits, uppercase_letters, lowercase_letters, punctuation, "il1Lo0O"]
    chars = ""
    for i in range(4):
        if li[i].lower()=="да":
            chars+= li[i+5]
    if includee.lower()=="да":
        for j in chars:
            if j in "il1Lo0O":
                chars = chars.replace(j, " ")
    chars = chars.replace(" ", "")
    l=int(input("Введите длину пароля: "))
    print(generate_password(l,chars))



