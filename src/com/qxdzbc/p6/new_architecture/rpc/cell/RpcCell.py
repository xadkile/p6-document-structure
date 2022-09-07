from typing import Optional

from com.qxdzbc.p6.document_structure.cell.Cell import Cell
from com.qxdzbc.p6.document_structure.cell.CellContent import CellContent
from com.qxdzbc.p6.document_structure.cell.address.CellAddress import CellAddress
from com.qxdzbc.p6.document_structure.communication.event.data_structure.SingleSignalResponse import \
    SingleSignalResponse
from com.qxdzbc.p6.document_structure.util.report.error.ErrorReport import ErrorReport
from com.qxdzbc.p6.document_structure.util.result.Result import Result
from com.qxdzbc.p6.document_structure.util.result.Results import Results
from com.qxdzbc.p6.document_structure.workbook.key.WorkbookKey import WorkbookKey
from com.qxdzbc.p6.new_architecture.common.RpcUtils import RpcUtils
from com.qxdzbc.p6.new_architecture.rpc.StubProvider import RpcStubProvider
from com.qxdzbc.p6.new_architecture.rpc.cell.msg.CopyCellRequest import CopyCellRequest
from com.qxdzbc.p6.new_architecture.rpc.data_structure.CellId import CellId
from com.qxdzbc.p6.new_architecture.rpc.data_structure.CellValue import CellValue
from com.qxdzbc.p6.new_architecture.rpc.data_structure.StrMsg import StrMsg
from com.qxdzbc.p6.proto.rpc.cell.service.CellService_pb2_grpc import CellServiceStub


class RpcCell(Cell):
    @property
    def displayValue(self) -> str:
        def f()->str:
            oProto = self._cellSv.getDisplayValue(request = self.id.toProtoObj())
            o = StrMsg.fromProto(oProto)
            return o.v
        return self._onCellSvOk(f)

    @property
    def wsName(self) -> Optional[str]:
        return self._wsName

    @property
    def wbKey(self) -> Optional[WorkbookKey]:
        return self._wbk

    @property
    def formula(self) -> str:
        def f() -> str:
            oProto = self._cellSv.getFormula(request = self.id.toProtoObj())
            o = StrMsg.fromProto(oProto)
            return o.v
        return self._onCellSvOk(f)

    @property
    def bareValue(self):
        cv:CellValue = self.cellValue
        return cv.value

    @property
    def value(self):
        return self.bareValue

    def isEmpty(self):
        return self.cellValue.isEmpty()

    def reRunRs(self) ->Result[None,ErrorReport]:
        def f():
            oProto = self._cellSv.reRun(request = self.id.toProtoObj())
            o = SingleSignalResponse.fromProto(oProto)
            return o.toRs()
        return self._onCellSvOkRs(f)

    def copyFromRs(self, anotherCell: "Cell")->Result[None,ErrorReport]:
        def f():
            request = CopyCellRequest(
                fromCell = anotherCell.id,
                toCell = self.id
            )
            oProto = self._cellSv.copyFrom(request=request.toProtoObj())
            o = SingleSignalResponse.fromProto(oProto)
            return o.toRs()
        return self._onCellSvOkRs(f)

    @property
    def rootCell(self) -> 'Cell':
        return self

    @property
    def content(self) -> CellContent:
        def f() -> CellContent:
            oProto = self._cellSv.getCellContent(request = self.id.toProtoObj())
            o = CellContent.fromProto(oProto)
            return o
        return self._onCellSvOk(f)

    @property
    def address(self) -> CellAddress:
        return self._address

    def __init__(
            self,
            cellAddress: CellAddress,
            wbKey: WorkbookKey,
            wsName: str,
            stubProvider: RpcStubProvider,
    ):
        self._address = cellAddress
        self._wbk = wbKey
        self._wsName = wsName
        self._sp = stubProvider

    @property
    def _cellSv(self) -> Optional[CellServiceStub]:
        return self._sp.cellService

    def _onCellSvOk(self, f):
        return RpcUtils.onServiceOk(self._cellSv, f)

    def _onCellSvOkRs(self, f):
        return RpcUtils.onServiceOkRs(self._cellSv, f)

    @property
    def cellValue(self) -> CellValue:
        def f() -> CellValue:
            oProto = self._cellSv.getCellValue(request = self.id.toProtoObj())
            o = CellValue.fromProto(oProto)
            return o
        return self._onCellSvOk(f)


