from django.db import models

class Member(models.Model):
    name = models.CharField("氏名", max_length=50)

    def __str__(self):
        return self.name

class Theme(models.Model):
    theme = models.CharField("お題", max_length=50)

    def __str__(self):
        return self.theme

class History(models.Model):
    member = models.ForeignKey(
        Member, verbose_name="氏名", on_delete=models.CASCADE,
    )
    theme = models.ForeignKey(
        Theme, verbose_name="お題", on_delete=models.CASCADE,
    )
    date = models.DateTimeField("日時", auto_now_add=True)

    def __str__(self):
        return str(self.date.strftime("%Y/%m/%d")) + " : " + str(self.member) + " : " + str(self.theme)