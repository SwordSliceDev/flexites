1) Регистрация нового пользователя:
POST /users/
{
    "email": "example@example.com",
    "password": "password123",
    "first_name": "Имя",
    "last_name": "Фамилия",
    "phone": "1234567890"
}

2) Авторизация пользователя:
POST /auth/
{
    "email": "example@example.com",
    "password": "password123"
}

3) Редактирование профиля:
PUT /users/{id}/
{
    "phone": "0987654321",
    "avatar": "new_avatar.jpg"  # Если требуются изменения аватара
}

4) Получение списка пользователей:
GET /users/

5) Получение одного пользователя по ID:
GET /users/{id}/

6) Добавление новой организации:
POST /organizations/
{
    "name": "Название организации",
    "description": "Краткое описание"
}

7) Получение списка всех организаций:
GET /organizations/
