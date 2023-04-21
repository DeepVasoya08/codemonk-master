import datetime
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Paragraph, User, Word
from .utils import decrypt, encrypt, generateToken, verifyToken


@csrf_exempt
def signup(request):
    if request.method == "POST":
        try:
            jsonData = json.loads(request.body)
            name = jsonData["name"]
            password = jsonData["password"]
            email = jsonData["email"]
            dob = jsonData["dob"]

            if User.objects.filter(email=email).exists():
                return JsonResponse({"message": "Email already exists"}, status=400)

            hashedPass = encrypt(password)

            user = User(name=name, email=email, password=hashedPass.decode(), dob=dob)
            user.save()
        except Exception as e:
            return JsonResponse({"message": e}, status=500)

        return JsonResponse({"message": "Signup successful"}, status=201)
    else:
        return JsonResponse({"message": "Invalid request method"}, status=500)


@csrf_exempt
def login(request):
    try:
        if request.method == "POST":
            jsonData = json.loads(request.body)
            email = jsonData["email"]
            password = jsonData["password"]

            user = (
                User.objects.filter(email=email)
                .values("id", "name", "email", "password")
                .first()
            )
            if user is None:
                return JsonResponse({"message": "user not found."}, status=404)

            validPass = decrypt(password, user["password"])
            if not validPass:
                return JsonResponse(
                    {"message": "Invalid username or password"}, status=401
                )
            payload = {
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
            }
            token = generateToken(payload)
            return JsonResponse({"message": token}, status=200)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=500)


@csrf_exempt
def postParagraph(request):
    try:
        if request.method == "POST":
            token = request.headers.get("Authorization").split(" ")[1]
            isValidToken = verifyToken(token, request)

            if isValidToken == "Token Expierd":
                return JsonResponse({"message": isValidToken}, status=401)

            if request.user:
                jsonData = json.loads(request.body)
                paragraph = Paragraph(text=jsonData["text"].lower())
                paragraph.save()
                words = paragraph.text.split()
                for i, word in enumerate(words):
                    word_obj, created = Word.objects.get_or_create(
                        word=word, paragraph=paragraph, position=i
                    )
                    if created:
                        word_obj.save()
                return JsonResponse({"message": "done"}, status=200)

            return JsonResponse({"message": "invalid token"}, status=500)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=500)


@csrf_exempt
def searchWord(request):
    try:
        if request.method == "POST":
            token = request.headers.get("Authorization").split(" ")[1]
            isValidToken = verifyToken(token, request)

            if isValidToken == "Token Expierd":
                return JsonResponse({"message": isValidToken}, status=401)

            if request.user:
                jsonData = json.loads(request.body)
                search_word = jsonData["word"].lower()

                word = Word.objects.filter(word__iexact=search_word)
                paragraphID = set([w.paragraph.id for w in word])
                return JsonResponse({"paragraphs": str(paragraphID)}, status=200)

            return JsonResponse({"message": "invalid token"}, status=500)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=500)


@csrf_exempt
def getParagraph(request):
    try:
        if request.method == "GET":
            paragraph = list(Paragraph.objects.all().values("id", "text"))
            return JsonResponse({"message": paragraph}, status=200)
        return JsonResponse({"message": "invalid method"}, status=500)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=500)
