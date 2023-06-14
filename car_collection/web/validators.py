from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class CustomMinLengthValidator:
    def __init__(self, min_value):
        self.min_value = min_value

    def __call__(self, value):
        if value < self.min_value:
            raise ValidationError(f"The username must be a minimum of {self.min_value} chars")
    def __eq__(self, other):
        return (
                isinstance(other, self.__class__)
                and self.min_value == other.min_value)

@deconstructible
class YearValidator:
    def __init__(self, min_year, max_year):
        self.min_year = min_year
        self.max_year = max_year

    def __call__(self, value):
        if not self.min_year <= value <= self.max_year:
            raise ValidationError(f'Year must be between {self.min_year} and {self.max_year}')

    def __eq__(self, other):
        return (
                isinstance(other, self.__class__)
                and self.min_year == other.min_year
                and self.max_year == other.max_year)