# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cloud_storage.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'cloud_storage.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x63loud_storage.proto\x12\x0c\x63loudstorage\"7\n\rUploadRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x14\n\x0c\x66ile_content\x18\x02 \x01(\x0c\"2\n\x0eUploadResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"#\n\x0f\x44ownloadRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\"J\n\x10\x44ownloadResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x14\n\x0c\x66ile_content\x18\x02 \x01(\x0c\x12\x0f\n\x07message\x18\x03 \x01(\t\"!\n\rDeleteRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\"2\n\x0e\x44\x65leteResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x12\n\x10ListFilesRequest\"\"\n\x11ListFilesResponse\x12\r\n\x05\x66iles\x18\x01 \x03(\t2\xcc\x02\n\x13\x43loudStorageService\x12I\n\nUploadFile\x12\x1b.cloudstorage.UploadRequest\x1a\x1c.cloudstorage.UploadResponse\"\x00\x12O\n\x0c\x44ownloadFile\x12\x1d.cloudstorage.DownloadRequest\x1a\x1e.cloudstorage.DownloadResponse\"\x00\x12I\n\nDeleteFile\x12\x1b.cloudstorage.DeleteRequest\x1a\x1c.cloudstorage.DeleteResponse\"\x00\x12N\n\tListFiles\x12\x1e.cloudstorage.ListFilesRequest\x1a\x1f.cloudstorage.ListFilesResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cloud_storage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_UPLOADREQUEST']._serialized_start=37
  _globals['_UPLOADREQUEST']._serialized_end=92
  _globals['_UPLOADRESPONSE']._serialized_start=94
  _globals['_UPLOADRESPONSE']._serialized_end=144
  _globals['_DOWNLOADREQUEST']._serialized_start=146
  _globals['_DOWNLOADREQUEST']._serialized_end=181
  _globals['_DOWNLOADRESPONSE']._serialized_start=183
  _globals['_DOWNLOADRESPONSE']._serialized_end=257
  _globals['_DELETEREQUEST']._serialized_start=259
  _globals['_DELETEREQUEST']._serialized_end=292
  _globals['_DELETERESPONSE']._serialized_start=294
  _globals['_DELETERESPONSE']._serialized_end=344
  _globals['_LISTFILESREQUEST']._serialized_start=346
  _globals['_LISTFILESREQUEST']._serialized_end=364
  _globals['_LISTFILESRESPONSE']._serialized_start=366
  _globals['_LISTFILESRESPONSE']._serialized_end=400
  _globals['_CLOUDSTORAGESERVICE']._serialized_start=403
  _globals['_CLOUDSTORAGESERVICE']._serialized_end=735
# @@protoc_insertion_point(module_scope)
