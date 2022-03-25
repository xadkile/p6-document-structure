from functools import partial
from typing import Callable, Optional, Union

from bicp_document_structure.cell.Cell import Cell
from bicp_document_structure.message.event.P6Event import P6Event
from bicp_document_structure.message.event.P6Events import P6Events
from bicp_document_structure.message.event.reactor.eventData.WorkbookEventData import WorkbookEventData
from bicp_document_structure.message.event.reactor.eventData.WorksheetEventData import WorksheetEventData
from bicp_document_structure.message.proto.DocPM_pb2 import CreateNewWorksheetProto
from bicp_document_structure.range.Range import Range
from bicp_document_structure.util.report.error.ErrorReport import ErrorReport
from bicp_document_structure.util.result.Ok import Ok
from bicp_document_structure.util.result.Result import Result
from bicp_document_structure.workbook.WorkBook import Workbook
from bicp_document_structure.workbook.WorkbookWrapper import WorkbookWrapper
from bicp_document_structure.worksheet.EventWorksheet import EventWorksheet
from bicp_document_structure.worksheet.Worksheet import Worksheet


class EventWorkbook(WorkbookWrapper):
    def __init__(self, innerWorkbook: Workbook,
                 onCellEvent: Callable[[Workbook, Worksheet, Cell, P6Event], None] = None,
                 onWorksheetEvent: Callable[[WorksheetEventData], None] = None,
                 onRangeEvent: Callable[[Workbook, Worksheet, Range, P6Event], None] = None,
                 onWorkbookEvent: Callable[[WorkbookEventData], None] = None,
                 ):
        super().__init__(innerWorkbook)
        self.__onCellChange: Callable[[Workbook, Worksheet, Cell, P6Event], None] = onCellEvent
        self.__onWorksheetEvent: Callable[[WorksheetEventData], None] = onWorksheetEvent
        self.__onRangeEvent: Callable[[Workbook, Worksheet, Range, P6Event], None] = onRangeEvent
        self.__onWorkbookEvent: Callable[[WorkbookEventData], None] = onWorkbookEvent
        self._iwb = self._innerWorkbook

    @property
    def worksheets(self) -> list[Worksheet]:
        """wrap the result worksheets in event worksheet, so that they can propagate event"""
        sheets = self._innerWorkbook.worksheets
        rt = list(map(lambda s: self.__wrapInEventWorksheet(s), sheets))
        return rt

    @property
    def activeWorksheet(self) -> Optional[Worksheet]:
        """wrap the result worksheet in event worksheet, so that it can propagate event"""
        activeSheet = self._innerWorkbook.activeWorksheet
        return self.__wrapInEventWorksheet(activeSheet)

    def getWorksheetByName(self, name: str) -> Optional[Worksheet]:
        """wrap the result worksheet in event worksheet, so that it can propagate event"""
        sheet = self._innerWorkbook.getWorksheetByName(name)
        if sheet is not None:
            return self.__wrapInEventWorksheet(sheet)
        else:
            return sheet

    def getWorksheetByIndex(self, index: int) -> Optional[Worksheet]:
        """wrap the result worksheet in event worksheet, so that it can propagate event"""
        s = self._innerWorkbook.getWorksheetByIndex(index)
        if s is not None:
            return self.__wrapInEventWorksheet(s)
        else:
            return s

    def getWorksheet(self, nameOrIndex: Union[str, int]) -> Optional[Worksheet]:
        """wrap the result worksheet in event worksheet, so that it can propagate event"""
        s = self._innerWorkbook.getWorksheet(nameOrIndex)
        if s is not None:
            return self.__wrapInEventWorksheet(s)
        else:
            return s

    def createNewWorksheet(self, newSheetName: Optional[str]) -> Worksheet:
        rs = self.createNewWorksheetRs(newSheetName)
        if rs.isOk():
            return rs.value
        else:
            raise rs.err.toException()

    def createNewWorksheetRs(self, newSheetName: Optional[str] = None) -> Result[Worksheet, ErrorReport]:
        rs = self._iwb.createNewWorksheetRs(newSheetName)
        if rs.isOk():
            newWorksheet = rs.value
            data = P6Events.Workbook.CreateNewWorksheet.Data(self.workbookKey, newWorksheet.name)
            wbEventData = WorkbookEventData(
                workbook = self,
                event = P6Events.Workbook.CreateNewWorksheet.event,
                data = data)
            if self.__onWorkbookEvent is not None:
                self.__onWorkbookEvent(wbEventData)
            # wrap the result worksheet in event worksheet, so that it can propagate event
            return Ok(self.__wrapInEventWorksheet(newWorksheet))
        else:
            return rs

    def reRun(self):
        self._innerWorkbook.reRun()
        if self.__onWorkbookEvent is not None:
            self.__onWorkbookEvent(WorkbookEventData(self._iwb,P6Events.Workbook.ReRun))

    def __wrapInEventWorksheet(self, sheet: Worksheet) -> Worksheet:
        onCellEvent = self.__partialWithNoneCheck(self.__onCellChange)
        onSheetEvent = self.__partialWithNoneCheck(self.__onWorksheetEvent)
        onRangeEvent = self.__partialWithNoneCheck(self.__onRangeEvent)
        return EventWorksheet(sheet,
                              onCellEvent = onCellEvent,
                              onWorksheetEvent = onSheetEvent,
                              onRangeEvent = onRangeEvent)

    def __partialWithNoneCheck(self, callback):
        if callback is not None:
            return partial(callback, self._innerWorkbook)
        else:
            return None

    def renameWorksheet(self, oldSheetNameOrIndex: str | int, newSheetName: str):
        rs = self.renameWorksheetRs(oldSheetNameOrIndex, newSheetName)
        if rs.isOk():
            oldName = oldSheetNameOrIndex
            index = self.getIndexOfWorksheet(newSheetName)
            supportData = P6Events.Worksheet.RenameOk.Data(self.workbookKey, oldName, newSheetName, index)
            data = WorksheetEventData(
                workbook = self,
                worksheet = self.getWorksheet(newSheetName),
                event = P6Events.Worksheet.RenameOk.event,
                supportData = supportData)
            self.__onWorksheetEvent(data)
        else:
            data = WorksheetEventData(self, self.getWorksheet(newSheetName), P6Events.Worksheet.RenameFail)
            self.__onWorksheetEvent(data)

    def renameWorksheetRs(self, oldSheetNameOrIndex: str | int, newSheetName: str) -> Result[None, ErrorReport]:
        rs = self._innerWorkbook.renameWorksheetRs(oldSheetNameOrIndex, newSheetName)
        return rs