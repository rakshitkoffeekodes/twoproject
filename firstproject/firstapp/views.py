# import mysql.connector
# from django.contrib.auth.models import User
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
#
#
# @api_view(['POST'])
# def create_user(request):
#     try:
#         username = request.data.get('username')
#         password = request.data.get('password')
#         email = request.data.get('email')
#
#         user = User.objects.create_user(username=username, email=email, password=password)
#
#         cnx = mysql.connector.connect(user='root', password='', host='localhost', database='secondproject')
#         cursor = cnx.cursor()
#         add_user = "INSERT INTO secondproject.users (username, email, password) VALUES (%s, %s, %s)"
#         cursor.execute(add_user, (username, email, password))
#         cnx.commit()
#
#         cursor.close()
#         cnx.close()
#
#         return Response({'message': 'User created successfully.'}, status=status.HTTP_201_CREATED)
#
#     except Exception as e:
#         # Handle any exceptions (e.g., database connection error, validation error)
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
