from rest_framework.serializers import ValidationError
from habits.models import Habit


class HabitValidator:

    def __call__(self, data):
        self.validate_related_habit_or_reward(data)
        self.validate_related_habit(data)
        self.validate_sign_nice_habit(data)
        self.validate_periodicity(data)
        self.validate_time_to_complete(data)
        self.validate_related_habits(data)

    def validate_related_habit_or_reward(self, data):
        """Исключает одновременный выбор вознаграждения и связанной привычки."""
        if data.get('related_habit') and data.get('reward'):
            raise ValidationError('Нельзя одновременно указывать вознаграждение и связанную привычку.')

    def validate_related_habit(self, data):
        """Исключает попадание в связанные привычки привычек, без признака приятной привычки."""
        related_habit = data.get('related_habit')
        if related_habit and not related_habit.sign_nice_habit:
            raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки.')

    def validate_sign_nice_habit(self, data):
        """Исключает попадание в приятные привычки вознаграждения или связанной привычки."""
        if data.get('sign_nice_habit'):
            if data.get('reward') or data.get('related_habit'):
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')

    def validate_periodicity(self, data):
        """Накладывает ограничения в виде запрета выполнения привычки реже 1 раза в 7 дней."""
        periodicity = data.get('periodicity')
        if not all(0 <= day <= 6 for day in periodicity):
            raise ValidationError('Дни недели должны быть в диапазоне от 0 до 6.')

        if len(periodicity) < 1 or len(periodicity) > 7:
            raise ValidationError('Привычка должна выполняться не реже 1 раза '
                                  'в течении 7 дней, не более 7 раз в неделю.')

    def validate_time_to_complete(self, data):
        """ Накладывает ограничения на время выполнения привычки, до 120 секунд."""
        if data.get('time_to_complete', 0) > 120:
            raise ValidationError('Время выполнения привычки должно быть не более 120 сек.')

    def validate_related_habits(self, data):
        """Проверяет, не пытаемся ли мы изменить привычку на неприятную, если она связана с другими привычками."""
        if data.get('id'):
            habit_id = data['id']
            related_habits = Habit.objects.filter(related_habit=habit_id)
            if related_habits.exists() and not data.get('sign_nice_habit'):
                raise ValidationError('Нельзя сделать привычку неприятной, если она связана с другими привычками.')
