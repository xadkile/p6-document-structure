# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/emeraldblast/p6/proto/service/workbook/GetAllWorksheets.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.emeraldblast.p6.proto import CommonProtos_pb2 as com_dot_emeraldblast_dot_p6_dot_proto_dot_CommonProtos__pb2
from com.emeraldblast.p6.proto import DocProtos_pb2 as com_dot_emeraldblast_dot_p6_dot_proto_dot_DocProtos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAcom/emeraldblast/p6/proto/service/workbook/GetAllWorksheets.proto\x12*com.emeraldblast.p6.proto.service.workbook\x1a,com/emeraldblast/p6/proto/CommonProtos.proto\x1a)com/emeraldblast/p6/proto/DocProtos.proto\"\xb5\x01\n\x1dGetAllWorksheetsResponseProto\x12=\n\nworksheets\x18\x01 \x03(\x0b\x32).com.emeraldblast.p6.proto.WorksheetProto\x12\x45\n\x0b\x65rrorReport\x18\x02 \x01(\x0b\x32+.com.emeraldblast.p6.proto.ErrorReportProtoH\x00\x88\x01\x01\x42\x0e\n\x0c_errorReportb\x06proto3')



_GETALLWORKSHEETSRESPONSEPROTO = DESCRIPTOR.message_types_by_name['GetAllWorksheetsResponseProto']
GetAllWorksheetsResponseProto = _reflection.GeneratedProtocolMessageType('GetAllWorksheetsResponseProto', (_message.Message,), {
  'DESCRIPTOR' : _GETALLWORKSHEETSRESPONSEPROTO,
  '__module__' : 'com.emeraldblast.p6.proto.service.workbook.GetAllWorksheets_pb2'
  # @@protoc_insertion_point(class_scope:com.emeraldblast.p6.proto.service.workbook.GetAllWorksheetsResponseProto)
  })
_sym_db.RegisterMessage(GetAllWorksheetsResponseProto)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETALLWORKSHEETSRESPONSEPROTO._serialized_start=203
  _GETALLWORKSHEETSRESPONSEPROTO._serialized_end=384
# @@protoc_insertion_point(module_scope)
