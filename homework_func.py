documents = [
{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
{"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
{"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
}

def get_name():
  number = input('Введите номер документа: ')
  for data in documents:
    if data.get("number") == number:
      return data.get('name')
  return 'Документа с таким номером нет!'

def get_shelf():
  number = input('Введите номер документа: ')
  for key in directories :
    if number in directories.get(key):
      return key
  return 'В полках документа с данным номером нет!'
 
def get_list(docs):
    for doc in docs:
        print(doc['type'], doc['number'], doc['name'])
 
 
def add_doc(doc_type, doc_number, doc_name, shelf_id):
    if shelf_id not in directories:
        return "Полки не существует!"
    new_doc = dict(type=doc_type, number=doc_number, name=doc_name)
    documents.append(new_doc)
    directories[shelf_id] += [doc_number]

    return "Документ успешно добавлен!"


 
HELP = '''
p/people - имя владельца по номеру документа,
s/shelf - номер полки по номеру документа,
l/list - список всех документов,
a/add - добавить новый документ,
q/quit - выход.
'''
 
while True:
  print(HELP)
  command = input('Введите название команды: ')
 
  if command == 'p':
    print(get_name())
    
  elif command == 's':
    print(get_shelf())
    
  elif command == 'l':
    print(get_list(documents))
    
  elif command == 'a':
    doc_type = input("Введите тип докемента: ")
    doc_number = input("Введите номер документа: ")
    doc_name = input("Введите имя владельца документа: ")
    shelf_id = input("Введит номер полки: ".format(directories.keys()))
    print(add_doc(doc_type, doc_number, doc_name, shelf_id))

  elif command == 'q':
    break
    
  else:
    print('Неверная команда!')