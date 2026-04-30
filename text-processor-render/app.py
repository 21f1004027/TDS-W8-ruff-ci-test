from fastapi import FastAPI, Request
import hashlib

app = FastAPI()


@app.post("/")
async def process_text(request: Request):
    data = await request.json()

    if "text" not in data:
        return {"error": "Missing text"}

    text = data["text"]

    uppercase = text.upper()
    char_count = len(text.replace("-", "").replace(" ", ""))
    word_count = len(text.replace("-", " ").split())
    sha = hashlib.sha256(text.encode()).hexdigest()[:16]
    verify = hashlib.sha256(
        f"upper:{uppercase}:chars:{char_count}:words:{word_count}".encode()
    ).hexdigest()[:12]

    return {
        "uppercase": uppercase,
        "char_count": char_count,
        "word_count": word_count,
        "sha256": sha,
        "verify": verify,
    }
