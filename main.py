from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware # CORS
#from mangum import Mangum
#python3 -m uviconr main:app --reload


app = FastAPI()
#handler = Mangum(app)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def index():
    msg = {
        "message" : "hello, world",
        "name" : "hogeta"
    }
    return msg

@app.get("/get_item")
def test2(q):
    print(q)
    msg = {
        "name" : q
    }
    return msg

