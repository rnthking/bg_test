from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World, bigluo good Bigluo tt dd"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8555, reload=True) 