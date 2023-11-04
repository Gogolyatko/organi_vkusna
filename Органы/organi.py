with open('Мухохрюйка.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line)
author = input('Vveditye avtora:')
with open('Мухохрюйка.txt', 'a', encoding='utf-8') as file:
  file.write(author)
while True:
    answer = input('Dobavit citatu. Auf. (da/nye):')
    if answer == 'da':
        quote = input('Vvedit citatu. Auf:')
        author = input('Vvedit avtora:')
        file = open('Мухохрюйка.txt', 'a', encoding='utf-8')
        file.write(quote +'\n' + author)
        file.close()
    else:
        break
with open('Мухохрюйка.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line)