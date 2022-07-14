from django.db import models
from user.models import User
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

class BaseShapeModel(models.Model):
	name = models.CharField(max_length=150)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)

	class Meta:
		abstract = True
	
	@property
	def area(self):
		raise NotImplementedError

	@property
	def perimeter(self):
		raise NotImplementedError


class Triangle(BaseShapeModel):
	side1 = models.FloatField(validators=[MinValueValidator(0)])
	side2 = models.FloatField(validators=[MinValueValidator(0)])
	side3 = models.FloatField(validators=[MinValueValidator(0)])

	@property
	def area(self):
		s = (self.side1 + self.side2 + self.side3) / 2
		return (s*(s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

	@property
	def perimeter(self):
		return self.side1 + self.side2 + self.side3


class Rectangle(BaseShapeModel):
	length = models.FloatField(validators=[MinValueValidator(0)])
	width = models.FloatField(validators=[MinValueValidator(0)])

	@property
	def area(self):
		return self.length * self.width

	@property
	def perimeter(self):
		return 2 * (self.length + self.width)


class Diamond(BaseShapeModel):
	diagonal1 = models.FloatField(validators=[MinValueValidator(0)])
	diagonal2 = models.FloatField(validators=[MinValueValidator(0)])
	side = models.FloatField(validators=[MinValueValidator(0)])

	@property
	def area(self):
		return (self.diagonal1 * self.diagonal2) / 2

	@property
	def perimeter(self):
		return self.side * 4