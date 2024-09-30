from rest_framework import serializers
from .models import Person, Bill, VoteResult


class SupportedBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id', 'title']


class SupportingPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name']


class PersonSerializer(serializers.ModelSerializer):
    supported_bills = serializers.SerializerMethodField()
    opposed_bills = serializers.SerializerMethodField()  # Corrected here

    class Meta:
        model = Person
        fields = ['id', 'name', 'supported_bills', 'opposed_bills']

    def get_supported_bills(self, obj):  # Also corrected typo in method name
        supported_vote_results = VoteResult.objects.filter(legislator=obj, vote_type=VoteResult.YES)
        bills = [result.vote.bill for result in supported_vote_results]
        return SupportedBillSerializer(bills, many=True).data
    
    def get_opposed_bills(self, obj):
        supported_vote_results = VoteResult.objects.filter(legislator=obj, vote_type=VoteResult.NO)
        bills = [result.vote.bill for result in supported_vote_results]
        return SupportedBillSerializer(bills, many=True).data


class BillSerializer(serializers.ModelSerializer):
    supporters = serializers.SerializerMethodField()
    opposers = serializers.SerializerMethodField()

    class Meta:
        model = Bill
        fields = ['id', 'title', 'supporters', 'opposers']

    def get_supporters(self, obj):
        supported_vote_results = VoteResult.objects.filter(vote__bill=obj, vote_type=VoteResult.YES)
        legislators = [result.legislator for result in supported_vote_results]
        return SupportingPersonSerializer(legislators, many=True).data

    def get_opposers(self, obj):
        supported_vote_results = VoteResult.objects.filter(vote__bill=obj, vote_type=VoteResult.NO)
        legislators = [result.legislator for result in supported_vote_results]
        return SupportingPersonSerializer(legislators, many=True).data
