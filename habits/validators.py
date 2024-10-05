from rest_framework.serializers import ValidationError


class HabitValidator:

    def __call__(self, data):
        self.validate_related_habit_or_reward(data)
        self.validate_related_habit(data)
        self.validate_sign_nice_habit(data)
        self.validate_periodicity(data)
        self.validate_time_to_complete(data)

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
        """ Накладывает ограничения в виде запрета выполнения привычки реже 1 раза в 7 дней."""
        if 1 <= data.get('periodicity') <= 7:
            raise ValidationError(
                'Привычка должна выполняться не реже 1 раза в течении 7 дней, не более 7 раз в неделю.'
            )

    def validate_time_to_complete(self, data):
        """ Накладывает ограничения на время выполнения привычки, до 120 секунд."""
        if data.get('time_to_complete', 0) > 120:
            raise ValidationError('Время выполнения привычки должно быть не более 120 сек.')
