class person:
    count_instance = 0
    def __init__(self, first_name, last_name, age):
        person.count_instance  += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = person('pratik','vaishnani', 20 )
p1 = person('pratik','vaishnani', 20 )
p1 = person('pratik','vaishnani', 20 )