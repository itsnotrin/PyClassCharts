import requests

baseURL = "https://www.classcharts.com/apiv2student"


def fetchAuthtoken(code: int, dob: str):
    url = "https://www.classcharts.com/apiv2student/login"
    response = requests.post(url, data = {"code": code, "dob": dob, "remember_me": 1, "recaptcha-token": "no-token-available"}).json()
    token = response["meta"]["session_id"]
    return "Basic " + token

def urlConstructor(endpoint: str, userid: int):
    match endpoint:
        case "timetable":
            return f"{baseURL}/timetable/{userid}"
        case "homework":
            return f"{baseURL}/homeworks/{userid}"
        case "homeworks":
            return f"{baseURL}/homeworks/{userid}"
        case "behaviour":
            return f"{baseURL}/activity/{userid}"


