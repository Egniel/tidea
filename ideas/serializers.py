from rest_framework import serializers

from ideas.models import *


class ChallengeModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Challenge


class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Comment


class CommentVoteModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CommentVote


class FeedbackModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Feedback


class FeedbackItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = FeedbackItem


class FeedbackTitleModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = FeedbackTitle


class IdeaModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Idea


class TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Tag


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User


class ViewModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = View


class VoteModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Vote
