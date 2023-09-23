from fastapi import FastAPI, Query, Depends
import uvicorn
from typing import Optional
from datetime import date
from pydantic import BaseModel

app = FastAPI()


class SHotel(BaseModel):
    address: str
    name: str
    star: int


class HotelsSearchArgs:
    def __int__(self,
                location: str,
                date_from: str,
                date_to: str,
                has_spa: Optional[bool] = False,
                star: Optional[int] = Query(None, ge=1, le=5)):
        self.location = location,
        self.date_from = date_from,
        self.date_to = date_to,
        self.has_spa = has_spa,
        self.star = star


@app.get("/hotels")
def get_hotels(
        search_args: HotelsSearchArgs = Depends()) -> list[SHotel]:
    hotels = [
        {
        "address": "г.Сочи, ул. Гагарина, д.5",
        "name": "Сочи СПА Резорт",
        "star": 5
        },
    ]
    return search_args

class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/booking")
def add_booking(booking: SBooking):
    pass


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)