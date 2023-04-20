from fastapi import FastAPI
import langchainprompts

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Advenure Sherpa is here to help you find the best adventure for you!"}

@app.get("/suggestions/")
async def get_suggestions(activity: str, user_location: str, difficulty_level: str, trip_duration: str):
    return langchainprompts.get_suggestions(activity, user_location, difficulty_level, trip_duration)