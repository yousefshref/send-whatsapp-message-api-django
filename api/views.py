
import pywhatkit as kit

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def send_whatsapp_message(request):
  phone_number = request.GET.get('phone')  # replace with the recipient's phone number
  message = request.GET.get('message')

  kit.sendwhatmsg_instantly(f"+20{phone_number}", message, tab_close=True)
  return Response({"":""})





