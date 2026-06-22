from rest_framework.views import APIView
from rest_framework.response import Response
from .predictor import EnergyPredictor

class EnergyPredictView(APIView):
    def post(self, request):
        predictor = EnergyPredictor()
        prediction = predictor.predict(request.data)
        return Response({'predicted_consumption': prediction})
