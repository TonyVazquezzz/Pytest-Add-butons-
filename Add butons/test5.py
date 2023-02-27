import requests


def test_weather_api():
    
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Madrid&appid=API_KEY")

   
    assert response.status_code == 200

   
    data = response.json()

    assert data["name"] == "Madrid"
    assert data["sys"]["country"] == "ES"
    assert "temp" in data["main"]
    assert "humidity" in data["main"]
    assert "description" in data["weather"][0]
