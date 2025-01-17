import grpc
import sys
import os

from concurrent import futures
from .config import SERVER_PORT
from .services import VideoStreamService

from protocol import video_stream_pb2_grpc

def run():

    try:
        # Create a gRPC server
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        # Register the CalculatorService
        video_stream_pb2_grpc.add_VideoStreamServicer_to_server(VideoStreamService(), server)

        # Bind to the specified port
        print(f"[vid_cache] Server is starting on port {SERVER_PORT}...")
        server.add_insecure_port(f'[::]:{SERVER_PORT}')

        server.start()
        server.wait_for_termination()

    except Exception as e:
        print(e);
        return

if __name__ == '__main__':
    run()
