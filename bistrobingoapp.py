from person_dao import getAllPersonen, getPerson, createPerson


def main():
    createSomePersons()


def createSomePersons():
    #createPerson("Bob", "Andrews")
    #createPerson("Justus", "Jonas")
    #createPerson("Peter", "Shaw")
    for person in getAllPersonen():
        print(person.serialize())


if __name__ == '__main__':
    main()