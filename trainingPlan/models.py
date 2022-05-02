from django.db import models
from django.utils import timezone
from accounts.models import User, Coach, Client
# from safedelete.managers import SafeDeleteManager
# from safedelete.queryset import SafeDeleteQueryset

# class PlanQuerySet(models.Manager):
#     # query sets for plan
#     def get_queryset(self):
#         return super().get_queryset().filter(status='published')




class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Plan(models.Model):


    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )


    category = models.ForeignKey(Category, on_delete=models.PROTECT, default = 1, related_name='plan_category')

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, db_index=True)
    desc = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published = models.DateTimeField(default = timezone.now)
    # pdf = models.FileField()
    # image = models.ImageField(upload_to='products/%Y/%m/%d',
    #                           blank=True)

    coach = models.ForeignKey(
        Coach, on_delete=models.CASCADE, related_name='plan_coach')
    status = models.CharField(max_length=10, choices=options, default='published')

    # objects = models.Manager() # default manager
    # planobjects = PlanObjects() # custom manager

    # objects = models.Manager.from_queryset(PlanQuerySet)()


    class Meta:
        ordering = ('-published',)
        index_together = (('id', 'slug'),)

        def __str__(self):
            return self.title