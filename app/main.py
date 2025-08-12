class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    for person in people:
        name = person.get("name")
        age = person.get("age")
        Person(name, age)
    for person in people:
        name = person.get("name")
        wife = person.get("wife")
        husband = person.get("husband")
        person_instance = Person.people[name]
        if wife:
            person_instance.wife = Person.people[wife]
        if husband:
            person_instance.husband = Person.people[husband]
    return list(Person.people.values())
