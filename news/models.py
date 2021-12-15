from django.db import models

# Create your models

class Competition(models.Model):
    """Model definition for Competition."""

    # TODO: Define fields here
    name = models.CharField(max_length=200, null=True)
    
    status = models.BooleanField(default=True, blank=True, null=True)
    date_add = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_upd = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        """Meta definition for Competition."""

        verbose_name = 'Competition'
        verbose_name_plural = 'Competitions'

    def __str__(self):
        """Unicode representation of Competition."""
        return self.name



class New(models.Model):
    """Model definition for New."""

    # TODO: Define fields here
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name="newsCompetition")
    title = models.CharField(max_length=200, null=True)
    date_pub = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    short_description = models.TextField(null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="image_news",null=True)
    
    status = models.BooleanField(default=True, blank=True, null=True)
    date_add = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_upd = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        """Meta definition for New."""

        verbose_name = 'New'
        verbose_name_plural = 'News'

    def __str__(self):
        """Unicode representation of New."""
        return self.title
