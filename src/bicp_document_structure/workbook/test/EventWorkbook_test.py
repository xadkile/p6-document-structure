import unittest
from collections import OrderedDict

from bicp_document_structure.formula_translator.FormulaTranslators import FormulaTranslators
from bicp_document_structure.workbook.EventWorkbook import EventWorkbook
from bicp_document_structure.workbook.WorkbookImp import WorkbookImp
from bicp_document_structure.worksheet.WorksheetImp2 import WorksheetImp2


class EventWorkbook_test(unittest.TestCase):
    @staticmethod
    def transGetter(name):
        return FormulaTranslators.mock()

    def makeTestObj(self):
        s1 = WorksheetImp2(name = "s1", translatorGetter = self.transGetter)
        s2 = WorksheetImp2(name = "s2", translatorGetter = self.transGetter)
        s3 = WorksheetImp2(name = "s3", translatorGetter = self.transGetter)
        d = OrderedDict({
            s1.name: s1,
            s2.name: s2,
            s3.name: s3
        })
        w1 = WorkbookImp("w1", sheetDict = d)
        return s1, s2, s3, w1, d

    def test_constructor(self):
        w = WorkbookImp("w1")
        self.a=0
        def cb(wb,ws,cell,e):
            self.a+=1
        eventWb = EventWorkbook(w,cb)
        s1 =eventWb.createNewWorksheet("s1")
        c1 =s1.cell("@A1")
        c1.value=123
        self.assertEqual(1,self.a)

        for ws in eventWb.worksheets:
            cell = ws.cell("@B1")
            cell.value = 456

        self.assertEqual(2,self.a)

        c2 = eventWb.activeWorksheet.cell("@Z1")
        c2.value="abc"
        self.assertEqual(3, self.a)

        c3 = eventWb.getWorksheetByIndex(0).cell("@K1")
        c3.value="qwe"
        self.assertEqual(4, self.a)

        c4 = eventWb.getWorksheetByName("s1").cell("@h1")
        c4.value="mmm"
        self.assertEqual(5, self.a)

        c4 = eventWb.getWorksheet(0).cell("@h1")
        c4.value = "mmm"
        self.assertEqual(6, self.a)