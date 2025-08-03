from fastapi import FastAPI, Query
import httpx

app = FastAPI()

FREE_API_URL = "https://api.exchangerate.host/convert"

@app.get("/convert")
async def convert_currency(from_currency: str = Query(..., alias="from"),
                           to_currency: str = Query(..., alias="to"),
                           amount: float = 1.0):
    async with httpx.AsyncClient() as client:
        response = await client.get(FREE_API_URL, params={
            "from": from_currency,
            "to": to_currency,
            "amount": amount
        })
        data = response.json()

    return {
        "from": from_currency,
        "to": to_currency,
        "original_amount": amount,
        "converted_amount": data.get("result")
    }
