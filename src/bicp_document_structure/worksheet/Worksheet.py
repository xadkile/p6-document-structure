from abc import ABC

from bicp_document_structure.cell_container.MutableCellContainer import MutableCellContainer
from bicp_document_structure.cell_container.UserFriendlyCellContainer import UserFriendlyCellContainer
from bicp_document_structure.column.MutableColumnContainer import MutableColumnContainer
from bicp_document_structure.worksheet.UserFriendlyWorksheet import UserFriendlyWorksheet
from bicp_document_structure.worksheet.WorksheetJson import WorksheetJson


class Worksheet(UserFriendlyCellContainer,
                UserFriendlyWorksheet,
                MutableCellContainer,
                MutableColumnContainer, ABC):
    @property
    def name(self) -> str:
        raise NotImplementedError()

    def toJson(self)->WorksheetJson:
        raise NotImplementedError()