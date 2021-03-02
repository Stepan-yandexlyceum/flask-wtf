user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"
user.hashed_password = "cap"
session.add(user)
session.commit()

user = User()
user.surname = "John"
user.name = "Wattson"
user.age = 35
user.position = "praporshik"
user.speciality = "sanitar"
user.address = "palata 1"
user.email = "jwattson@mars.org"
user.hashed_password = "durka"
session.add(user)
session.commit()

user = User()
user.surname = "Dmitry"
user.name = "Puchkov"
user.age = 70
user.position = "main shizik"
user.speciality = "kommunist engineer"
user.address = "soviet russia"
user.email = "puchkov@mars.org"
user.hashed_password = "puchok"
session.add(user)
session.commit()

user = User()
user.surname = "Druzhko"
user.name = "Sergey"
user.age = 42
user.position = "haiper"
user.speciality = "content maker"
user.address = "no info"
user.email = "sdruzhko@mars.org"
user.hashed_password = "haip"
session.add(user)
session.commit()
