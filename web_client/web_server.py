from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, StreamingResponse
from pathlib import Path

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

@app.get("/video", response_class=StreamingResponse)
def video_endpoint():
    def stream():
        #video_path = "C:\\Users\\Allu\\Desktop\\Ohjelmointi\\DS\\ex1\\Distributed-Systems-2025---Project\\web_client\\vids\\testvid.mp4"
        video_path = Path("/vids/testvid.mp4")
        with open(video_path, mode="rb") as file_like:
            yield from file_like
        
    return StreamingResponse(stream(), media_type="video/mp4", status_code=206)

app.mount("/", StaticFiles(directory="www", html=True), name="Main Site")
app.mount("/video", video_endpoint())