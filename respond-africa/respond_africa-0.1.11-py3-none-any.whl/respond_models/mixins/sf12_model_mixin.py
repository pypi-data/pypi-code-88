from django.db import models

EXCELLENT = "excellent"
VERY_GOOD = "very_good"
GOOD = "good"
FAIR = "fair"

DESCRIBE_HEALTH_CHOICES = (
    (EXCELLENT, "Excellent"),
    (VERY_GOOD, "Very Good"),
    (GOOD, "Good"),
    (FAIR, "Fair"),
)


class Sf12ModelMixin(models.Model):

    """Version ?"""

    how_describe_health = models.CharField(
        verbose_name="In general, would you say your health is",
        choices=DESCRIBE_HEALTH_CHOICES,
    )
