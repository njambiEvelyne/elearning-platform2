from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Quiz, Question, Submission, Answer
from .serializers import QuizSerializer, QuestionSerializer, SubmissionSerializer, AnswerSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class =AnswerSerializer
    permission_classes = [IsAuthenticated]