import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from votes.models import Person, Bill, Vote, VoteResult


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def sample_data(db):
    legislator1 = Person.objects.create(name="Rep. John Doe")
    legislator2 = Person.objects.create(name="Rep. Jane Roe")

    bill1 = Bill.objects.create(title="H.R. 3684: Infrastructure Investment and Jobs Act", primary_sponsor=legislator1)
    bill2 = Bill.objects.create(title="H.R. 5376: Build Back Better Act", primary_sponsor=legislator2)

    vote1 = Vote.objects.create(bill=bill1)
    vote2 = Vote.objects.create(bill=bill2)

    VoteResult.objects.create(legislator=legislator1, vote=vote1, vote_type=VoteResult.YES)
    VoteResult.objects.create(legislator=legislator2, vote=vote2, vote_type=VoteResult.NO)

    return {
        "legislators": [legislator1, legislator2],
        "bills": [bill1, bill2]
    }


def test_get_persons(api_client, sample_data):
    response = api_client.get(reverse('person-list'))
    assert response.status_code == 200
    assert len(response.json()) == 2

    legislator = response.json()[0]
    assert 'id' in legislator
    assert 'name' in legislator
    assert 'supported_bills' in legislator
    assert 'opposed_bills' in legislator


def test_get_bills(api_client, sample_data):
    response = api_client.get(reverse('bill-list'))
    assert response.status_code == 200
    assert len(response.json()) == 2
    
    bill = response.json()[0]
    assert 'id' in bill
    assert 'title' in bill
    assert 'supporters' in bill
    assert 'opposers' in bill
