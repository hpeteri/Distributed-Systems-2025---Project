import grpc
import os

from protocol import video_stream_pb2
from protocol import video_stream_pb2_grpc
from .config import SERVER_PORT

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = video_stream_pb2_grpc.VideoStreamStub(channel)
        request = video_stream_pb2.VideoSegmentRequest(_unused = 0)

        response_stream = stub.GetSegment(request)
        output_file = os.path.join(os.path.dirname(__file__), "../output/stream.mp4")
        with open(output_file, 'wb') as video_file:
            for chunk in response_stream:
                video_file.write(chunk.chunk_data)
                print(f"Received chunk {chunk.chunk_number}")

if __name__ == "__main__":
    run()
