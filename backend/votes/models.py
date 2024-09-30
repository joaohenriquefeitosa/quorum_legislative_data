from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Bill(models.Model):
    title = models.CharField(max_length=255)
    primary_sponsor = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name='sponsored_bills')

    def __str__(self):
        return self.title

class Vote(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='votes')

    def __str__(self):
        return f"Vote on {self.bill.title}"

class VoteResult(models.Model):
    YES = 1
    NO = 2

    VOTE_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]
    
    legislator = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='vote_results')
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name='vote_results')
    vote_type = models.IntegerField(choices=VOTE_CHOICES)

    def __str__(self):
        return f"{self.legislator.name} voted {self.get_vote_type_display()} on {self.vote.bill.title}"