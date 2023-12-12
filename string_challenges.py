# Вывести последнюю букву в слове
word = 'Архангельск'
last_letter=word[-1]
print(last_letter)


# Вывести количество букв "а" в слове
word = 'Архангельск'
word_lower=word.lower()
print(word_lower.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vse_gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
word_lower=word.lower()
num_gls=0
for letter in word_lower:
    if letter in vse_gls:
        num_gls+=1
    else:
        num_gls
print(num_gls)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
num_words=sentence.split(' ')
print(len(num_words))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence_list=sentence.split(' ')
for word in sentence_list:
    print(word[0])



# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sentence=sentence.split()
length = sum(len(word) for word in sentence)
avg_len=length/len(sentence)
print(avg_len)