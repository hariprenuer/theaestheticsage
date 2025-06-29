"""
{"latitude": 11.6643,
  "longitude": 78.1460,
  "date": 9,
  "month": 6,
  "year" : 2005,
  "hour" : 14,
 "minutes" : 3}
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Birthdata
from .serializer import Birthserializer
import json
from birthdata.prognostics.data import sample_gen
from birthdata.prognostics.predictions.basic import manager
from birthdata.intelligence.gpr_model import gpr_adjusted_curve  # This should be your GPR module

class BirthDataAPIView(APIView):
    def get(self, request):
        print("GET / - Fetching existing birth data...")
        queryset = Birthdata.objects.all()
        if not queryset.exists():
            return Response({"ERROR": "No birth data found."}, status=status.HTTP_404_NOT_FOUND)

        data_list = [
            {
                "latitude": entry.latitude,
                "longitude": entry.longitude,
                "date": entry.date,
                "month": entry.month,
                "year": entry.year,
                "hour": entry.hour,
                "minutes": entry.minutes
            } for entry in queryset
        ]

        print("Running horoscope manager...")
        result = manager.horoscope(data_list).detials
        return Response(result)

    def post(self, request):
        print("POST / - New birth data received")
        format_keys = ["latitude", "longitude", "date", "month", "year", "hour", "minutes"]
        data_dict = {k: request.data[k] for k in format_keys if k in request.data}

        serializer = Birthserializer(data=data_dict)
        if serializer.is_valid():
            serializer.save()
            birthdata = serializer.data
            horoscope = manager.horoscope(birthdata).horoscope
            horoscope["sample_val"] = sample_gen.sample_gen(
                birthdata["date"],
                birthdata["month"],
                birthdata["year"]
            )
            return Response(horoscope)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdjustGraphAPIView(APIView):
    def post(self, request):
        print("#################################tried")
        try:
            # print(request.data)
            original_data = request.data.get("original_data", [])
            user_edits = request.data.get("edited_points", [])
            x_range = request.data.get("x_range", [])

            # Fix if accidentally sent as strings
            if isinstance(original_data, str):
                original_data = json.loads(original_data)
            if isinstance(user_edits, str):
                user_edits = json.loads(user_edits)
            if isinstance(x_range, str):
                x_range = json.loads(x_range)

            if not original_data or not x_range:
                return Response(
                    {"error": "Missing required fields"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            from birthdata.intelligence.gpr_model import gpr_adjusted_curve
            adjusted_result = gpr_adjusted_curve(original_data, user_edits, x_range)
            return Response({"adjusted_data": adjusted_result})

        except Exception as e:
            print("Error in /adjust:", e)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)