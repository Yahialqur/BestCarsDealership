from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import now

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Additional fields can be added as needed

    def __str__(self):
        return self.name  # Return the name as the string representation

# Car Model model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)
    dealer_id = models.IntegerField()  # Refers to a dealer ID in the external database
    
    # Define choices for car type
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ],
        default=2023
    )
    # Additional fields can be added as needed

    def __str__(self):
        return f"{self.car_make.name} {self.name}"  # Show both car make and model in string representation
