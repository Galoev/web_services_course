# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eservices.proto\"E\n\x05Image\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\r\n\x05width\x18\x02 \x01(\x03\x12\x0f\n\x07\x63hannel\x18\x03 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\"R\n\x07Request\x12\x1a\n\nlogo_image\x18\x01 \x01(\x0b\x32\x06.Image\x12\x1a\n\nmain_imgae\x18\x02 \x01(\x0b\x32\x06.Image\x12\x0f\n\x07opacity\x18\x03 \x01(\x03\x32\x39\n\x10WatermarkService\x12%\n\x11\x61\x64\x64ImageWatermark\x12\x08.Request\x1a\x06.Imageb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _IMAGE._serialized_start=18
  _IMAGE._serialized_end=87
  _REQUEST._serialized_start=89
  _REQUEST._serialized_end=171
  _WATERMARKSERVICE._serialized_start=173
  _WATERMARKSERVICE._serialized_end=230
# @@protoc_insertion_point(module_scope)
