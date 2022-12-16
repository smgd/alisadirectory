from servicedb.db import get_db

app = FastAPI()


@app.get("/appeals/", response_model=...)
def read_appeals():
    db = get_db()
