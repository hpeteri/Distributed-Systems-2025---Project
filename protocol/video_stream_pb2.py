# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: video_stream.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'video_stream.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12video_stream.proto\"&\n\x13VideoSegmentRequest\x12\x0f\n\x07_unused\x18\x01 \x01(\r\"@\n\x14VideoSegmentResponse\x12\x12\n\nchunk_data\x18\x01 \x01(\x0c\x12\x14\n\x0c\x63hunk_number\x18\x02 \x01(\r2J\n\x0bVideoStream\x12;\n\nGetSegment\x12\x14.VideoSegmentRequest\x1a\x15.VideoSegmentResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'video_stream_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_VIDEOSEGMENTREQUEST']._serialized_start=22
  _globals['_VIDEOSEGMENTREQUEST']._serialized_end=60
  _globals['_VIDEOSEGMENTRESPONSE']._serialized_start=62
  _globals['_VIDEOSEGMENTRESPONSE']._serialized_end=126
  _globals['_VIDEOSTREAM']._serialized_start=128
  _globals['_VIDEOSTREAM']._serialized_end=202
# @@protoc_insertion_point(module_scope)
