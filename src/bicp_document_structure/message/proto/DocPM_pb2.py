# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DocPM.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# import Common_pb2 as Common__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x44ocPM.proto\x12\x1d\x63om.github.xadkile.p6.app.msg\x1a\x0c\x43ommon.proto\",\n\x10\x43\x65llAddressProto\x12\x0b\n\x03\x63ol\x18\x01 \x01(\x05\x12\x0b\n\x03row\x18\x02 \x01(\x05\"}\n\tCellProto\x12\r\n\x05value\x18\x01 \x01(\t\x12\x0f\n\x07\x66ormula\x18\x02 \x01(\t\x12\x0e\n\x06script\x18\x03 \x01(\t\x12@\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32/.com.github.xadkile.p6.app.msg.CellAddressProto\"V\n\x0eWorksheetProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x36\n\x04\x63\x65ll\x18\x02 \x03(\x0b\x32(.com.github.xadkile.p6.app.msg.CellProto\"\x9c\x01\n\rWorkbookProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12;\n\x04path\x18\x02 \x01(\x0b\x32-.com.github.xadkile.p6.app.msg.NullableString\x12@\n\tworksheet\x18\x03 \x03(\x0b\x32-.com.github.xadkile.p6.app.msg.WorksheetProtob\x06proto3')



_CELLADDRESSPROTO = DESCRIPTOR.message_types_by_name['CellAddressProto']
_CELLPROTO = DESCRIPTOR.message_types_by_name['CellProto']
_WORKSHEETPROTO = DESCRIPTOR.message_types_by_name['WorksheetProto']
_WORKBOOKPROTO = DESCRIPTOR.message_types_by_name['WorkbookProto']
CellAddressProto = _reflection.GeneratedProtocolMessageType('CellAddressProto', (_message.Message,), {
  'DESCRIPTOR' : _CELLADDRESSPROTO,
  '__module__' : 'DocPM_pb2'
  # @@protoc_insertion_point(class_scope:com.github.xadkile.p6.app.msg.CellAddressProto)
  })
_sym_db.RegisterMessage(CellAddressProto)

CellProto = _reflection.GeneratedProtocolMessageType('CellProto', (_message.Message,), {
  'DESCRIPTOR' : _CELLPROTO,
  '__module__' : 'DocPM_pb2'
  # @@protoc_insertion_point(class_scope:com.github.xadkile.p6.app.msg.CellProto)
  })
_sym_db.RegisterMessage(CellProto)

WorksheetProto = _reflection.GeneratedProtocolMessageType('WorksheetProto', (_message.Message,), {
  'DESCRIPTOR' : _WORKSHEETPROTO,
  '__module__' : 'DocPM_pb2'
  # @@protoc_insertion_point(class_scope:com.github.xadkile.p6.app.msg.WorksheetProto)
  })
_sym_db.RegisterMessage(WorksheetProto)

WorkbookProto = _reflection.GeneratedProtocolMessageType('WorkbookProto', (_message.Message,), {
  'DESCRIPTOR' : _WORKBOOKPROTO,
  '__module__' : 'DocPM_pb2'
  # @@protoc_insertion_point(class_scope:com.github.xadkile.p6.app.msg.WorkbookProto)
  })
_sym_db.RegisterMessage(WorkbookProto)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CELLADDRESSPROTO._serialized_start=60
  _CELLADDRESSPROTO._serialized_end=104
  _CELLPROTO._serialized_start=106
  _CELLPROTO._serialized_end=231
  _WORKSHEETPROTO._serialized_start=233
  _WORKSHEETPROTO._serialized_end=319
  _WORKBOOKPROTO._serialized_start=322
  _WORKBOOKPROTO._serialized_end=478
# @@protoc_insertion_point(module_scope)
