from typing import Union, Optional

from bicp_document_structure.app.App import App
from bicp_document_structure.workbook.WorkBook import Workbook
from bicp_document_structure.workbook.WorkbookImp import WorkbookImp


class SingleBookApp(App):

    def __init__(self):
        self.__book = WorkbookImp("Book1")
    @property
    def activeWorkbook(self) -> Optional[Workbook]:
        return self.__book

    def getWorkbookByIndex(self, index: int) -> Optional[Workbook]:
        return self.__book

    def hasNoWorkbook(self) -> bool:
        return False

    def setActiveWorkbook(self, indexOrName: Union[int, str]):
        return

    def createNewWorkBook(self, name: str):
        return

    def saveWorkbook(self, nameOrIndex: Union[int, str], filePath: str):
        return

    def loadWorkbook(self, filePath: str) -> bool:
        return False