import csv
import os
from django.core.management.base import BaseCommand
from votes.models import Person, Bill, Vote, VoteResult

class Command(BaseCommand):
    help = 'Seed database with initial data from CSV files'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Seeding database...'))

        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        data_dir = os.path.join(base_dir, '..', 'data')

        legislators_csv = os.path.join(data_dir, 'legislators.csv')
        self.import_legislators(legislators_csv)

        bills_csv = os.path.join(data_dir, 'bills.csv')
        self.import_bills(bills_csv)

        votes_csv = os.path.join(data_dir, 'votes.csv')        
        self.import_votes(votes_csv)

        vote_results_csv = os.path.join(data_dir, 'vote_results.csv')
        self.import_vote_results(vote_results_csv)

        self.stdout.write(self.style.SUCCESS('Database seeding completed!'))

    def import_legislators(self, file_path):
        """Import legislators from a CSV file."""
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                legislator, created = Person.objects.get_or_create(
                    id=row['id'],
                    defaults={'name': row['name']}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Inserted {legislator.name} into Person"))

    def import_bills(self, file_path):
        """Import bills from a CSV file."""
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                sponsor = Person.objects.get(id=row['sponsor_id'])
                bill, created = Bill.objects.get_or_create(
                    id=row['id'],
                    defaults={'title': row['title'], 'primary_sponsor': sponsor}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Inserted {bill.title} into Bill"))

    def import_votes(self, file_path):
        """Import votes from a CSV file."""
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                bill = Bill.objects.get(id=row['bill_id'])
                vote, created = Vote.objects.get_or_create(
                    id=row['id'],
                    defaults={'bill': bill}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Inserted Vote for {vote.bill.title}"))

    def import_vote_results(self, file_path):
        """Import vote results from a CSV file."""
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                legislator = Person.objects.get(id=row['legislator_id'])
                vote = Vote.objects.get(id=row['vote_id'])
                vote_result, created = VoteResult.objects.get_or_create(
                    id=row['id'],
                    defaults={'legislator': legislator, 'vote': vote, 'vote_type': row['vote_type']}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Inserted VoteResult for {legislator.name} on {vote.bill.title}"))
