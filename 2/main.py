import requests
import os
from fastapi import FastAPI

app = FastAPI()


def api_v1() -> dict:
    return (requests.get("http://ip-api.com/json/")).json()["query"]

def api_v2() -> dict:
    return ((requests.get("https://jsonip.com")).json())["ip"]

def _get_ip():
    api_version = os.getenv("API_VERSION")
    
    match api_version:
        case "1":
            ip = api_v1()
        case "2":
            ip = api_v2()
        case None:
            ip = "No API_VERSION found in env"

    q = {"myIP": ip}

    return q


@app.get("/get_ip")
def get_ip():
    return _get_ip()

