from shared.views import BaseListView
from users import serializers
from users import models


class EmployeeListView(BaseListView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer
