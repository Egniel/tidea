from django.shortcuts import render

from rest_framework import viewsets

from ideas.serializers import *


class ChallengeModelViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeModelSerializer


class CommentModelViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer


class CommentVoteModelViewSet(viewsets.ModelViewSet):
    queryset = CommentVote.objects.all()
    serializer_class = CommentVoteModelSerializer


class FeedbackModelViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackModelSerializer


class FeedbackItemModelViewSet(viewsets.ModelViewSet):
    queryset = FeedbackItem.objects.all()
    serializer_class = FeedbackItemModelSerializer


class FeedbackTitleModelViewSet(viewsets.ModelViewSet):
    queryset = FeedbackTitle.objects.all()
    serializer_class = FeedbackTitleModelSerializer


class IdeaModelViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaModelSerializer


class TagModelViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class ViewModelViewSet(viewsets.ModelViewSet):
    queryset = View.objects.all()
    serializer_class = ViewModelSerializer


class VoteModelViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteModelSerializer


