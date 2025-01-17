import grpc
import re

from protocol import video_stream_pb2_grpc

class VideoStreamService(video_stream_pb2_grpc.VideoStreamServicer):
    def GetSegment(self, request, context):
        context.set_code(grpc.StatusCode.INTERNAL)
        context.set_details(f"EvalFailure: {str(e)}")
        return grpc.RpcError("EvalEquationFailure")
