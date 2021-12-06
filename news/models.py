from django.db import models

# Create your models


class Competition(models.Model):
    """Model definition for Competition."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Competition."""

        verbose_name = 'Competition'
        verbose_name_plural = 'Competitions'

    def __str__(self):
        """Unicode representation of Competition."""
        pass



class Team(models.Model):
    """Model definition for Team."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Team."""

        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        """Unicode representation of Team."""
        pass


class TeamTransfert(models.Model):
    """Model definition for TeamTransfert."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for TeamTransfert."""

        verbose_name = 'TeamTransfert'
        verbose_name_plural = 'TeamTransferts'

    def __str__(self):
        """Unicode representation of TeamTransfert."""
        pass