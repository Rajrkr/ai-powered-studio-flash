from django.shortcuts import render, redirect
from .models import User, Booking


import pandas as pd
import joblib

price_model = joblib.load("price_model.pkl")
package_model = joblib.load("package_model.pkl")


def home(request):

    message = ""

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.filter(username=username, password=password).first()

        if user:
            request.session["username"] = username
            return render(request, "services.html")

        message = "Invalid Username or Password"

    return render(request, "index.html", {"message": message})


def services(request):
    return render(request, "services.html")


def register(request):

    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        User.objects.create(username=username, email=email, password=password)

        return render(request, "index.html")

    return render(request, "register.html")


def forgot_password(request):

    if request.method == "POST":

        username = request.POST["username"]

        user = User.objects.filter(username=username).first()

        if user:
            return render(request, "forgot.html", {"password": user.password})

    return render(request, "forgot.html")
def booking(request):

    if request.method == "POST":

        username = request.session.get("username")

        service = request.POST["service"]
        event_date = request.POST["event_date"]

        hours = int(request.POST["hours"])
        photos = int(request.POST["photos"])

        service_map = {
            "Wedding": 1,
            "Fashion": 2,
            "Studio": 3,
            "Birthday": 4,
            "Family": 5,
            "Commercial": 6
        }

        service_code = service_map[service]

        price_data = pd.DataFrame(
            {
                "Service": [service_code],
                "Hours": [hours],
                "Photos": [photos]
            }
        )

        predicted_price = round(
            price_model.predict(price_data)[0],
            2
        )

        package_data = pd.DataFrame(
            {
                "Budget": [predicted_price],
                "Event": [service_code]
            }
        )

        recommended_package = package_model.predict(
            package_data
        )[0]

        Booking.objects.create(
            username=username,
            service=service,
            event_date=event_date
        )

        return render(
            request,
            "booking.html",
            {
                "predicted_price": predicted_price,
                "recommended_package": recommended_package,
                "message": "Booking Successful"
            }
        )

    return render(request, "booking.html")

def booking_history(request):

    username = request.session.get("username")

    bookings = Booking.objects.filter(username=username)

    return render(request, "history.html", {"bookings": bookings})


def delete_booking(request, id):

    booking = Booking.objects.get(id=id)

    booking.delete()

    return redirect("/history/")



def recommend_package(request):

    package = None

    if request.method == "POST":

        budget = int(request.POST["budget"])
        event = int(request.POST["event"])

        data = pd.DataFrame({"Budget": [budget], "Event": [event]})

        package = package_model.predict(data)[0]

    return render(request, "recommend_package.html", {"package": package})
def predict_price(request):

    price = None

    if request.method == "POST":

        service = int(request.POST["service"])
        hours = int(request.POST["hours"])
        photos = int(request.POST["photos"])

        data = pd.DataFrame(
            {
                "Service": [service],
                "Hours": [hours],
                "Photos": [photos]
            }
        )

        price = round(
            price_model.predict(data)[0],
            2
        )

    return render(
        request,
        "predict_price.html",
        {"price": price}
    )

       

    




def dashboard(request):

    username = request.session.get("username")

    bookings = Booking.objects.filter(username=username)

    total_bookings = bookings.count()

    context = {"username": username, "total_bookings": total_bookings}

    return render(request, "dashboard.html", context)


def profile(request):

    username = request.session.get("username")

    user = User.objects.get(
        username=username
    )

    bookings = Booking.objects.filter(
        username=username
    ).count()

    return render(
        request,
        "profile.html",
        {
            "user": user,
            "bookings": bookings
        }
    )


def logout(request):

    request.session.flush()

    return redirect('/')
