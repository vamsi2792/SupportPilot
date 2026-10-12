from fastapi import FastAPI

app = FastAPI(title="SupportPilot")


@app.get("/health")
def health():
    return {"status": "ok"}