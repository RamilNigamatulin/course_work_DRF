## Описание проекта

Habit Tracker API — это RESTful API, разработанное на Django и Django REST Framework, которое позволяет пользователям создавать, управлять и отслеживать свои ежедневные привычки. API также поддерживает отправку уведомлений в Telegram о предстоящих привычках.

## Основные функции

- **Создание и управление привычками**: Пользователи могут создавать новые привычки, указывая действие, место, время и периодичность выполнения.
- **Отправка уведомлений в Telegram**: API автоматически отправляет уведомления в Telegram о предстоящих привычках.
- **Фильтрация и сортировка привычек**: Пользователи могут фильтровать привычки по различным параметрам, таким как время, место и периодичность.
- **Публикация привычек**: Пользователи могут публиковать свои привычки, чтобы другие пользователи могли их видеть.

## Требования

- Python 3.10
- Docker
- Docker Compose
- PostgreSQL
## Установка
1. Клонируйте репозиторий: https://github.com/RamilNigamatulin/home_work_DRF.git
2. Создайте виртуальное окружение:
- python -m venv venv
- source venv/bin/activate
3. Переименуйте файл ".env.sample" в ".env" и заполните его. 
4. Запустите проект:
- docker-compose up -d --build
5. Откройте приложение в браузере:
http://localhost:8000/ или http://0.0.0.0:8000/
