from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

STATIC_DIR = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/", response_class=HTMLResponse)
async def main_page():
    index_file = STATIC_DIR / "index.html"
    return index_file.read_text(encoding="utf-8")

@app.post("/submit")
async def submit_form(
    owner_name: str = Form(...),
    pet_name: str = Form(...),
    breed: str = Form(...),
    problem: str = Form("")
):
    print("📌 Новая заявка:")
    print("Владелец:", owner_name)
    print("Питомец:", pet_name)
    print("Порода:", breed)
    print("Проблема:", problem)

    return JSONResponse({
        "status": "OK",
        "message": "Заявка успешно отправлена!",
        "data": {
            "owner": owner_name,
            "pet": pet_name,
            "breed": breed,
            "problem": problem
        }
    })

@app.get("/api/info")
async def api_info():
    return {"message": "FastAPI работает. HTML доступен по /static/index.html или по /"}
