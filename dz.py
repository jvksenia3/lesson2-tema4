class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._users_list = []

    def add_user(self, user):
        if isinstance(user, User):
            self._users_list.append(user)
            print(f"User {user.get_name()} added.")
        else:
            print("Invalid user.")

    def remove_user(self, user_id):
        for user in self._users_list:
            if user.get_user_id() == user_id:
                self._users_list.remove(user)
                print(f"User {user.get_name()} removed.")
                return
        print("User not found.")

    def get_users_list(self):
        return self._users_list

    def set_users_list(self, users_list):
        if all(isinstance(user, User) for user in users_list):
            self._users_list = users_list
        else:
            print("Invalid users list.")


# Пример использования
admin = Admin(1, 'Admin1')

# Создаем пользователей
user1 = User(2, 'User1')
user2 = User(3, 'User2')

# Добавляем пользователей
admin.add_user(user1)
admin.add_user(user2)

# Просмотр списка пользователей
for user in admin.get_users_list():
    print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")

# Удаляем пользователя
admin.remove_user(2)

# Просмотр списка пользователей после удаления
for user in admin.get_users_list():
    print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")
