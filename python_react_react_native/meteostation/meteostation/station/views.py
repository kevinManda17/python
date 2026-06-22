from rest_framework import generics, mixins, permissions, status
from .models import Station, Reading
from .serializers import StationSerializer, ReadingSerializer
import joblib
from rest_framework.views import APIView
from rest_framework.response import Response


MODEL_PATH = "station/ml/model_store/latest_model.joblib"


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user

# Station list/create
class StationListCreateView(mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             generics.GenericAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # attach owner
        request.data["created_by"] = request.user.pk
        return self.create(request, *args, **kwargs)

# Station detail (retrieve / update / delete) using mixin + CBV
class StationDetailView(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class PredictView(APIView):
    permission_classes = [permissions.AllowAny]  # ou IsAuthenticated si tu veux restreindre

    def post(self, request):
        features = request.data.get("features")
        if not features:
            return Response({"error":"no features"}, status=status.HTTP_400_BAD_REQUEST)

        model = joblib.load(MODEL_PATH)
        # features doit être formaté comme array 2D
        pred = model.predict([features])
        return Response({"prediction": pred[0]})


