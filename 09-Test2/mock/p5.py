def f(fl :str, ll :str):
    count = 0
    with open('09-Test2\\mock\\data.txt', encoding='utf8') as file:
        lines = file.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                word = str(word)
                if word[-1].isalpha() is False:
                    word = word[:-1]
                if word.startswith(fl) and word.endswith(ll):
                    count += 1
    return count
print(f("w","d"))

                