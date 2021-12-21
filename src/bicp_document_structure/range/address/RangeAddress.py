from abc import ABC

from bicp_document_structure.cell.address.CellAddress import CellAddress


class RangeAddress(ABC):

    @property
    def firstRowIndex(self)->int:
        return self.firstAddress.rowIndex
    @property
    def lastRowIndex(self)->int:
        return self.lastAddress.rowIndex

    @property
    def firstColIndex(self)->int:
        return self.firstAddress.colIndex
    @property
    def lastColIndex(self)->int:
        return self.lastAddress.colIndex

    def containCellAddress(self,cellAddress:CellAddress):
        colOk = self.firstColIndex <= cellAddress.colIndex <= self.lastColIndex
        rowOk = self.firstRowIndex <= cellAddress.rowIndex <= self.lastRowIndex
        return colOk and rowOk

    @property
    def firstAddress(self) -> CellAddress:
        raise NotImplementedError()

    @property
    def lastAddress(self) -> CellAddress:
        raise NotImplementedError()

    def rowCount(self) -> int:
        raise NotImplementedError()

    def colCount(self) -> int:
        raise NotImplementedError()


