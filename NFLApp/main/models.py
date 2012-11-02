from django.db import models

# Create your models here.
class Game(models.Model):
    Date = models.DateField()
    TeamName = models.CharField(max_length=25)
    ScoreOff = models.IntegerField()
    #FirstDownOff = models.IntegerField()
    #ThirdDownPctOff = models.DecimalField(max_digits=5, decimal_places=2)
    #RushAttOff = models.IntegerField()
    #RushYdsOff = models.IntegerField()
    #PassAttOff = models.IntegerField()
    #PassCompOff = models.IntegerField()
    #PassYdsOff = models.IntegerField()
    #PassIntOff = models.IntegerField()
    #FumblesOff = models.IntegerField()
    #SackYdsOff = models.IntegerField()
    #PenYdsOff = models.IntegerField()
    #TimePossOff = models.TimeField()
    #PuntAvgOff = models.IntegerField()
    Opponent = models.CharField(max_length=25)
    ScoreDef = models.IntegerField()
    #FirstDownDef = models.IntegerField()
    #ThirdDownPctDef = models.DecimalField(max_digits=5, decimal_places=2)
    #RushAttDef = models.IntegerField()
    #RushYdsDef = models.IntegerField()
    #PassAttDef = models.IntegerField()
    #PassCompDef = models.IntegerField()
    #PassYdsDef = models.IntegerField()
    #PassIntDef = models.IntegerField()
    #FumblesDef = models.IntegerField()
    #SackYdsDef = models.IntegerField()
    #PenYdsDef = models.IntegerField()
    #TimePossDef = models.TimeField()
    
    def __unicode__(self):
        return self.TeamName + " vs. " + self.Opponent + " on " + str(self.Date)

    def won(self):
        return self.ScoreOff > self.ScoreDef
