import grpc
import re
import os

from protocol import video_stream_pb2_grpc
from protocol import video_stream_pb2
from .config import VIDEO_CHUNK_SIZE

class VideoStreamService(video_stream_pb2_grpc.VideoStreamServicer):
    def GetSegment(self, request, context):

        try:
            video_path = os.path.join(os.path.dirname(__file__), "../data/testvid.mp4")
            chunk_number = 0
            print(video_path)
            with open(video_path, 'rb') as video_file:
                while True:
                    chunk_data = video_file.read(VIDEO_CHUNK_SIZE)
                    if not chunk_data:
                        break
                    chunk_number += 1
                    yield video_stream_pb2.VideoSegmentResponse(chunk_data=chunk_data, chunk_number=chunk_number)
        except FileNotFoundError:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Video not found')
            return

