import json
import uuid
from typing import Any

from bicp_document_structure.message.P6MessageHeader import P6MessageHeader
from bicp_document_structure.message.proto.P6MsgPM_pb2 import P6MessageProto
from bicp_document_structure.util.ToProto import ToProto


class P6Message(ToProto[P6MessageProto]):

    def __init__(self, header: P6MessageHeader, data: ToProto | str | bytes):
        self._content: ToProto | str | bytes = data
        self._header: P6MessageHeader = header

    @staticmethod
    def create(event, data: Any):
        msg = P6Message(
            header = P6MessageHeader(
                msgId = str(uuid.uuid4()),
                eventType = event,
            ),
            data = data)
        return msg
    @staticmethod
    def fromProto(proto:P6MessageProto)->'P6Message':
        rt = P6Message(
            header = P6MessageHeader.fromProto(proto.header),
            data = proto.data
        )
        return rt

    @property
    def data(self):
        return self._content

    @property
    def header(self):
        return self._header

    def toProtoObj(self):
        rt = P6MessageProto()
        rt.header.CopyFrom(self.header.toProtoObj())
        content = self.data
        if isinstance(self.data, ToProto):
            content = self.data.toProtoBytes()
        rt.data = content
        return rt
