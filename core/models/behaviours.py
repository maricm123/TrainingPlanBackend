class Namable(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=512, verbose_name=_("name"))


class TimeStampable(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_("creations"))
    modified = models.DateTimeField(auto_now=True, verbose_name=_("last modification"))


class UUIDable(models.Model):
    class Meta:
        abstract = True

    uuid = UUIDField(default=uuid.uuid4, unique=True, editable=False)



class AppLogFormatable(models.Model):
    class Meta:
        # doesnt make a table for this model
        abstract = True

    @cached_property
    def as_app_log(self):
        """display an object with a suitable format for logging actions"""
        # TODO: unit test
        return f"{self.__str__()} ({self.pk})"