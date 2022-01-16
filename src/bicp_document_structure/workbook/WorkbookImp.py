from collections import OrderedDict as ODict
from pathlib import Path
from typing import Union, Optional, OrderedDict, Callable, List

from bicp_document_structure.cell.Cell import Cell
from bicp_document_structure.mutation.CellMutationEvent import CellMutationEvent
from bicp_document_structure.util.Util import typeCheck
from bicp_document_structure.workbook.WorkBook import Workbook
from bicp_document_structure.workbook.WorkbookKey import WorkbookKey
from bicp_document_structure.workbook.WorkbookKeyImp import WorkbookKeyImp
from bicp_document_structure.worksheet.Worksheet import Worksheet
from bicp_document_structure.worksheet.WorksheetImp import WorksheetImp


class WorkbookImp(Workbook):

    def __init__(self, name: str,
                 path: Path = None,
                 sheetDict: OrderedDict = None,
                 onCellMutation: Callable[[WorkbookKey, str, Cell, CellMutationEvent], None] = None,
                 ):
        self.__name = name
        self.__onCellMutation:Optional[Callable[[WorkbookKey, str, Cell, CellMutationEvent], None]] = onCellMutation
        self.__key = WorkbookKeyImp(self.__name, path)
        if sheetDict is None:
            sheetDict = ODict()
        else:
            typeCheck(sheetDict, "sheetDict", OrderedDict)
        self.__sheetDict = sheetDict

        self.__activeSheet = None
        if self.sheetCount != 0:
            self.__activeSheet = list(self.__sheetDict.values())[0]

    @staticmethod
    def __makeOrderDict(sheetDict: dict) -> dict:
        o = 0
        rt = {}
        for k, v in list(sheetDict.items()):
            rt[o] = k
            o += 1
        return rt

    ### >> Workbook << ###

    def sheets(self) -> List[Worksheet]:
        return list(self.__sheetDict.values())

    @property
    def workbookKey(self) -> WorkbookKey:
        return self.__key

    @workbookKey.setter
    def workbookKey(self, newKey: WorkbookKey):
        self.__key = newKey
        self.__name = newKey.fileName

    def setActiveSheet(self, indexOrName: Union[int, str]):
        sheet = self.getSheet(indexOrName)
        if sheet is not None:
            self.__activeSheet = sheet
        else:
            raise ValueError("{n} is invalid workbook index or workbook".format(n=indexOrName))

    @property
    def activeSheet(self) -> Optional[Worksheet]:
        return self.__activeSheet

    def isEmpty(self) -> bool:
        return self.sheetCount == 0

    def getSheetByName(self, name: str) -> Optional[Worksheet]:
        typeCheck(name, "name", str)
        if name in self.__sheetDict.keys():
            return self.__sheetDict[name]
        else:
            return None

    def getSheetByIndex(self, index: int) -> Optional[Worksheet]:
        typeCheck(index, "index", int)
        if 0 <= index < self.sheetCount:
            rt: Worksheet = list(self.__sheetDict.items())[index][1]
            return rt
        else:
            return None

    def getSheet(self, nameOrIndex: Union[str, int]) -> Optional[Worksheet]:
        if isinstance(nameOrIndex, str):
            return self.getSheetByName(nameOrIndex)
        elif isinstance(nameOrIndex, int):
            return self.getSheetByIndex(nameOrIndex)
        else:
            raise ValueError(
                "nameOrIndex is of type {t}. nameOrIndex must be string or int.".format(t=str(type(nameOrIndex))))

    @property
    def sheetCount(self) -> int:
        return len(self.__sheetDict)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, newName: str):
        self.__name = newName

    def createNewSheet(self, newSheetName) -> Worksheet:
        if newSheetName in self.__sheetDict.keys():
            raise ValueError(
                "Can't create new sheet {sname} because sheet {sname} already exist".format(sname=newSheetName))
        else:
            newSheet = WorksheetImp(name=newSheetName,
                                    onCellMutation=self.__mutationEventCallback)
            self.__sheetDict[newSheetName] = newSheet
            return newSheet

    def __mutationEventCallback(self,
                                worksheetName: str,
                                cell: Cell,
                                mutationEvent: CellMutationEvent):
        self.__onCellMutation(self.workbookKey, worksheetName, cell, mutationEvent)

    def removeSheetByName(self, sheetName: str) -> Optional[Worksheet]:
        typeCheck(sheetName, "sheetName", str)
        if sheetName in self.__sheetDict.keys():
            rt: Worksheet = self.__sheetDict[sheetName]
            del self.__sheetDict[sheetName]
            return rt
        else:
            return None

    def removeSheetByIndex(self, index: int) -> Optional[Worksheet]:
        typeCheck(index, "index", int)
        if 0 <= index < len(self.__sheetDict):
            name: str = list(self.__sheetDict.items())[index][0]
            return self.removeSheetByName(name)
        else:
            return None

    def removeSheet(self, nameOrIndex: Union[str, int]) -> Optional[Worksheet]:
        if isinstance(nameOrIndex, str):
            return self.removeSheetByName(nameOrIndex)

        if isinstance(nameOrIndex, int):
            return self.removeSheetByIndex(nameOrIndex)

        raise ValueError("nameOrIndex must either be a string or a number")
