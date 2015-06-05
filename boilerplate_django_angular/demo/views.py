from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def message_list(request):
    """
    Respond with demo api message
    """
    if request.method == 'GET':
        return Response({"message":"API call works!"}, status=status.HTTP_200_OK)




