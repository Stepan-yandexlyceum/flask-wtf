from data.users import User

user = db_sess.query(User).first()
print(user.name)
for user in db_sess.query(User).all():
    print(user)
