import classcharts.utils as utils
import requests

def getTimetable(code: str, dob: str, userid: int, day: int, month: int, year: int):
    authToken = utils.fetchAuthtoken(code, dob)
    print(authToken)
    if len(str(month)) == 1:
        month = f"0{month}" # Hacky workaround for Python not allowing leading zeroes in integers
    url = utils.urlConstructor("timetable", userid)
    url += f"?date={year}-{month}-{day}"
    response = requests.get(url, headers = {"Authorization": authToken}).json()
    print(response)
    return response

def getHomework(code: str, dob: str, userid: int, day:int, month: int, year: int):
    authToken = utils.fetchAuthtoken(code, dob)
    if len(str(month)) == 1:
        month = f"0{month}"
    url = utils.urlConstructor("homework", userid)
    url += f"?date={year}-{month}-{day}"
    response = requests.get(url, headers = {"Authorization": authToken}).json()
    print(response)
    return response

def getBehaviour(code: str, dob: str, userid: int, fromDay: int, fromMonth: int, fromYear: int, toDay: int, toMonth: int, toYear: int):
    authToken = utils.fetchAuthtoken(code, dob)
    if len(str(fromMonth)) == 1:
        fromMonth = f"0{fromMonth}"
    if len(str(toMonth)) == 1:
        toMonth = f"0{toMonth}"
    if len(str(fromDay)) == 1:
        fromDay = f"0{fromDay}"
    if len(str(toDay)) == 1:
        toDay = f"0{toDay}"
    url = utils.urlConstructor("behaviour", userid)
    url += f"?from={fromYear}-{fromMonth}-{fromDay}&to={toYear}-{toMonth}-{toDay}" 
    response = requests.get(url, headers={"Authorization": authToken}).json()
    print(response)
    return response


