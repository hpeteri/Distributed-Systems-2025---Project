# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import video_stream_pb2 as video__stream__pb2

GRPC_GENERATED_VERSION = '1.69.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in video_stream_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class VideoStreamStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSegment = channel.unary_unary(
                '/VideoStream/GetSegment',
                request_serializer=video__stream__pb2.VideoSegmentRequest.SerializeToString,
                response_deserializer=video__stream__pb2.VideoSegmentResponse.FromString,
                _registered_method=True)


class VideoStreamServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSegment(self, request, context):
        """
        Retrieved a specific video segment base on the request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VideoStreamServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSegment': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSegment,
                    request_deserializer=video__stream__pb2.VideoSegmentRequest.FromString,
                    response_serializer=video__stream__pb2.VideoSegmentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'VideoStream', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('VideoStream', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class VideoStream(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSegment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/VideoStream/GetSegment',
            video__stream__pb2.VideoSegmentRequest.SerializeToString,
            video__stream__pb2.VideoSegmentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)