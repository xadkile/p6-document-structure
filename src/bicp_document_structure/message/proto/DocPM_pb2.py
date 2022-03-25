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


from . import Common_pb2 as Common__pb2
z = Common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x44ocPM.proto\x12\x1d\x63om.github.xadkile.p6.app.msg\x1a\x0c\x43ommon.proto\",\n\x10\x43\x65llAddressProto\x12\x0b\n\x03\x63ol\x18\x01 \x01(\x05\x12\x0b\n\x03row\x18\x02 \x01(\x05\"}\n\tCellProto\x12\r\n\x05value\x18\x01 \x01(\t\x12\x0f\n\x07\x66ormula\x18\x02 \x01(\t\x12\x0e\n\x06script\x18\x03 \x01(\t\x12@\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32/.com.github.xadkile.p6.app.msg.CellAddressProto\"V\n\x0eWorksheetProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x36\n\x04\x63\x65ll\x18\x02 \x03(\x0b\x32(.com.github.xadkile.p6.app.msg.CellProto\"\x9c\x01\n\rWorkbookProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12;\n\x04path\x18\x02 \x01(\x0b\x32-.com.github.xadkile.p6.app.msg.NullableString\x12@\n\tworksheet\x18\x03 \x03(\x0b\x32-.com.github.xadkile.p6.app.msg.WorksheetProto\"]\n\x10WorkbookKeyProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12;\n\x04path\x18\x02 \x01(\x0b\x32-.com.github.xadkile.p6.app.msg.NullableString\"\x8f\x01\n\x16RenameWorksheetOkProto\x12\x44\n\x0bworkbookKey\x18\x01 \x01(\x0b\x32/.com.github.xadkile.p6.app.msg.WorkbookKeyProto\x12\x0f\n\x07oldName\x18\x02 \x01(\t\x12\r\n\x05index\x18\x03 \x01(\x05\x12\x0f\n\x07newName\x18\x04 \x01(\t\"y\n\x17\x43reateNewWorksheetProto\x12\x44\n\x0bworkbookKey\x18\x01 \x01(\x0b\x32/.com.github.xadkile.p6.app.msg.WorkbookKeyProto\x12\x18\n\x10newWorksheetName\x18\x02 \x01(\tb\x06proto3')



_CELLADDRESSPROTO = DESCRIPTOR.message_types_by_name['CellAddressProto']
_CELLPROTO = DESCRIPTOR.message_types_by_name['CellProto']
_WORKSHEETPROTO = DESCRIPTOR.message_types_by_name['WorksheetProto']
_WORKBOOKPROTO = DESCRIPTOR.message_types_by_name['WorkbookProto']
_WORKBOOKKEYPROTO = DESCRIPTOR.message_types_by_name['WorkbookKeyProto']
_RENAMEWORKSHEETOKPROTO = DESCRIPTOR.message_types_by_name['RenameWorksheetOkProto']
_CREATENEWWORKSHEETPROTO = DESCRIPTOR.message_types_by_name['CreateNewWorksheetProto']
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

WorkbookKeyProto = _reflection.GeneratedProtocolMessageType('WorkbookKeyProto', (_message.Message,), {
  'DESCRIPTOR' : _WORKBOOKKEYPROTO,
  '__module__' : 'DocPM_pb2'
  # @@protoc_insertion_point(class_scope:com.github.xadkile.p6.app.msg.WorkbookKeyProto)
  })
_sym_db.RegisterMessage(WorkbookKeyProto)

RenameWorksheetOkProto = _reflection.GeneratedProtocolMessageType('RenameWorksheetOkProto', (_message.Message,), {
  'DESCRIPTOR' : _RENAMEWORKSHEETOKPROTO,
  '__module__' : 'DocPM_pb2'
  # @@protoc_insertion_point(class_scope:com.github.xadkile.p6.app.msg.RenameWorksheetOkProto)
  })
_sym_db.RegisterMessage(RenameWorksheetOkProto)

CreateNewWorksheetProto = _reflection.GeneratedProtocolMessageType('CreateNewWorksheetProto', (_message.Message,), {
  'DESCRIPTOR' : _CREATENEWWORKSHEETPROTO,
  '__module__' : 'DocPM_pb2'
  # @@protoc_insertion_point(class_scope:com.github.xadkile.p6.app.msg.CreateNewWorksheetProto)
  })
_sym_db.RegisterMessage(CreateNewWorksheetProto)

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
  _WORKBOOKKEYPROTO._serialized_start=480
  _WORKBOOKKEYPROTO._serialized_end=573
  _RENAMEWORKSHEETOKPROTO._serialized_start=576
  _RENAMEWORKSHEETOKPROTO._serialized_end=719
  _CREATENEWWORKSHEETPROTO._serialized_start=721
  _CREATENEWWORKSHEETPROTO._serialized_end=842
# @@protoc_insertion_point(module_scope)
