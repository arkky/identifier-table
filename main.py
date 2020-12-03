import random

class BinaryTree():
    def __init__(self, element):
        self.left = None
        self.right = None
        self.root = element

    def AddElement(self, data):
        if self.root == None:
            self.root = data
            print('Элемента {0} нет. Записываем'.format(data))
        elif data == self.root:
            print('Элемент {0} уже есть'.format(data))
        elif data > self.root:
            if self.right is None:
                # Можно разкомментировать нижний комментарий, чтобы посмотреть как идёт элемент
                #print('Значение {0} больше и правая ветвь пустая, поэтому записываем в правую ветвь.'.format(data))
                self.right = BinaryTree(data)
            else:
                # Можно разкомментировать нижний комментарий, чтобы посмотреть как идёт элемент
                #print('Значение {0} больше и правая ветвь не пустая, поэтому вставляем в неё'.format(data))
                self.right.AddElement(data)
        elif data < self.root:
            if self.left is None:
                # Можно разкомментировать нижний комментарий, чтобы посмотреть как идёт элемент
                #print('Значение {0} меньше и его нет в левой ветви, поэтому записываем в левую ветвь.'.format(data))
                self.left = BinaryTree(data)
            else:
                #Можно разкомментировать нижний комментарий, чтобы посмотреть как идёт элемент
                #print('Значение {0} меньше и левая ветвь не пустая, поэтому вставляем в неё'.format(data))
                self.left.AddElement(data)

    def SearchElement(self, element):
        if self.root == None:
            print('Элемент {0} не найден!'.format(element))
        elif self.root == element:
            print('Элемент {0} найден!'.format(element))
        elif element > self.root:
            if self.right:
                print('RIGHT')
                self.right.SearchElement(element)
            elif self.right is None:
                print('Элемент {0} не найден!'.format(element))
        elif element < self.root:
            if self.left:
                print('LEFT')
                self.left.SearchElement(element)
            elif self.left is None:
                print('Элемент {0} не найден!'.format(element))

class REHASHING:
    def __init__(self, list_):
        #self.n - число от которого будем узнавать остаток
        self.n = 509
        #Создаём таблицу пустых значинй от 0 до n, не включая n
        self.TABLE_ID = {x: None for x in range(self.n)}
        self.list_id = list_
        self.P = [444]
        self.B = 2
        self.C = 48
        #Заполняю список пвевдослучайными числами
        for i in range(1, self.n):
            self.P.append((self.B * self.P[i-1] + self.C) % self.n)

    #Функция, которая заполний таблицу self.TABLE_ID идентификаторами
    def create_id(self):
        #Создаю цикл, в котором прохожу список по идентификаторам
        for i in self.list_id:
            #вычисляю hash для первой буквы слова по mod n, где n == 509
            hash = ord(i[0]) % self.n
            #Если у нас пустая ячейка, то записываем слово в эту ячейку
            if self.TABLE_ID[hash] == None:
                self.TABLE_ID[hash] = i
            #Иначе, если у нас ячейка занята, использую ещё один цикл, где вычисляется rehash с добавлением целого числа (от 1 до n, не включая n) и по нему смотрим новую ячейку
            #Если эта ячейка будет пустой, то запишим в неё значение и выйдем из цикла
            else:
                for j in range(1, self.n):
                    rehash = (hash + self.P[j]) % self.n
                    if self.TABLE_ID[rehash] == None:
                        self.TABLE_ID[rehash] = i
                        break

    def search_id(self, id):
        hash = ord(id[0]) % self.n
        if self.TABLE_ID[hash] == None:
            print('Элемент {0} не найден!'.format(id))
        else:
            if self.TABLE_ID[hash] == id:
                print('Номер идентификатора: {0} \nЭлемент {1} найден!'.format(hash, id))
            else:
                for i in range(1, self.n):
                    rehash = (hash + self.P[i]) % self.n
                    if self.TABLE_ID[rehash] == None:
                        print('Элемент {0} не найден!'.format(id))
                        break
                    else:
                        if id == self.TABLE_ID[rehash]:
                            print('Номер идентификатора: {0} \nЭлемент {1} найден!'.format(rehash, id))
                            break

#Пустой список
list_id = []

print('Входные данные берутся с файла: data.txt')
print()

#Проверяю есть ли файл и, если есть, добавляю в список все значения из него
try:
    with open('data.txt', 'r') as id_words:
        for i in id_words:
            for j in i.split():
                list_id.append(j)
except Exception as E:
    print('Программа не видит файл: data.txt')
    exit()

#Объявляю экземпляр и даю 1-ое значение для бинарного дерева
Tree = BinaryTree(list_id[0])

#Записываю идентификаторы в бинарное дерево
for i in list_id[1:]:
    Tree.AddElement(i)

#Создаю экземпляр класса REHASHING и даю список id
table_id = REHASHING(list_id)
table_id.create_id()

print('Список идентификаторов в классе BinaryTree: {0}'.format(list_id))
print('Список идентификаторов в классе REHASHING: {0}'.format(table_id.list_id))
#Создаю цикл, где можно найти идентификатор, где можно добавить идентификатор, где можно выйти из цикла
while True:
    print()
    print('Возможные команды: search, list, exit')
    var = input('Введите команду: ')
    if var == 'exit':
        break
    elif var == 'search':
        in_var = input('Какой индификатор нужно найти? ')
        print('')
        print('Нахождение элемента через бинарное дерево:')
        Tree.SearchElement(in_var)
        print()
        print('Нахождение элемента через рехэширование:')
        table_id.search_id(in_var)
    elif var == 'list':
        print('Список идентификаторов в классе BinaryTree: {0}'.format(list_id))
        print('Список идентификаторов в классе REHASHING: {0}'.format(table_id.list_id))
    else:
        print('Такой команды нет')

    print('-'*20)