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


class Classment(models.Model):
    """Model definition for Classment."""

    # TODO: Define fields here
    
    #Fk team and competition

    class Meta:
        """Meta definition for Classment."""

        verbose_name = 'Classment'
        verbose_name_plural = 'Classments'

    def __str__(self):
        """Unicode representation of Classment."""
        pass

class Actu(models.Model):
    """Model definition for Actu."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Actu."""

        verbose_name = 'Actu'
        verbose_name_plural = 'Actus'

    def __str__(self):
        """Unicode representation of Actu."""
        pass

class CommentActu(models.Model):
    """Model definition for CommentActu."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for CommentActu."""

        verbose_name = 'CommentActu'
        verbose_name_plural = 'CommentActus'

    def __str__(self):
        """Unicode representation of CommentActu."""
        pass
    

class Result(models.Model):
    """Model definition for Result."""

    # TODO: Define fields here
    
    #Fk team and competition

    class Meta:
        """Meta definition for Result."""

        verbose_name = 'Result'
        verbose_name_plural = 'Results'

    def __str__(self):
        """Unicode representation of Result."""
        pass
    
class BestGoaler(models.Model):
    """Model definition for BestGoaler."""

    # TODO: Define fields here
    
    #Fk competition

    class Meta:
        """Meta definition for BestGoaler."""

        verbose_name = 'BestGoaler'
        verbose_name_plural = 'BestGoalers'

    def __str__(self):
        """Unicode representation of BestGoaler."""
        pass

class Calendar(models.Model):
    """Model definition for Calendar."""

    # TODO: Define fields here
    
    #Fk team and competition

    class Meta:
        """Meta definition for Calendar."""

        verbose_name = 'Calendar'
        verbose_name_plural = 'Calendars'

    def __str__(self):
        """Unicode representation of Calendar."""
        pass

