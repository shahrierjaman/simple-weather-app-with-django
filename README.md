# 🌦️ Django Weather App

A simple Django-based weather application that fetches real-time weather
data using the OpenWeather API.\
Users can enter any city name and instantly see temperature,
description, weather icon, and date.

## 🚀 Features

-   Search weather by city name\
-   Displays temperature, description, city, icon, date\
-   Minimalist UI\
-   Uses OpenWeather API

## 🛠️ Installation & Setup

###  Clone the Repository

    git clone https://github.com/your-username/weatherapp.git
    cd weatherapp


###  Install Dependencies

    pip install -r requirements.txt

## ⚙️ Configure API Key

Edit `views.py` and add:

    apiID = 'YOUR_API_KEY_HERE'

## ▶️ Run the Project

    python manage.py runserver

Visit:

    http://127.0.0.1:8000/home/

## 📁 Project Structure

    project/
     ├── weatherApp/
     │    ├── templates/
     │    ├── views.py
     │    └── urls.py
     ├── project/
     └── manage.py


