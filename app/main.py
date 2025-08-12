class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_list = [Person(p.get("name"), p.get("age")) for p in people]
    for person_data in people:
        person_instance = Person.people.get(person_data.get("name"))
        wife = person_data.get("wife")
        husband = person_data.get("husband")
        if wife:
            person_instance.wife = Person.people.get(wife)
        if husband:
            person_instance.husband = Person.people.get(husband)

    return person_list
