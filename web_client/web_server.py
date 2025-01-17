from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI(title="Web Client for Video Streaming")

def generate_html_response():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/video/", response_class=HTMLResponse)
async def read_items():
    return generate_html_response()

app.mount("/", StaticFiles(directory="www", html=True), name="Main Site")
app.mount("/video/", read_items())