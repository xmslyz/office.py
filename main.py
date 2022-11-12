import datetime
import os
import pathlib
import re
import pandas as pd

import DatabaseLayer
import gui.InsertTab.UpdateMassRecord
import gui.InsertTab.DeleteMassRecord
import gui.InsertTab.InsertNewMassRecord
import gui.SettingsTab.Button_BuildNewDatabase
import buissnes.Statements.ManageMonthlyStmt
import buissnes.Statements.ManageGeneralStmt
from buissnes.Database import Builder
import gui.InsertTab.UpdateStmts

import unittest
import sqlite3
from unittest import TestCase, mock
from unittest.mock import patch, MagicMock


class Foo:
    def checkActive(self):
        conn = sqlite3.connect('lll.db')
        cur = conn.execute("SELECT * FROM SQLITE_MASTER")
        value = cur.fetchone()
        return value


class test_Foo(TestCase):

    @patch('sqlite3.connect')
    def test_shortTest(self, mock_sql):
        mock_sql.return_value.execute.return_value.fetchone.return_value = ('Test',)
        test_class = Foo()
        return_mock = test_class.checkActive()
        print(return_mock)


    def main():
        pass
        # gui.SettingsTab.Button_BuildNewDatabase.Build_DB_Button().build_database()
        # gui.InsertTab.InsertNewMassRecord.Button_Add_New_Record().add_new_mass_record()
        # gui.InsertTab.UpdateMassRecord.Button_Update_Mass_Record().update_intention_row()
        # gui.InsertTab.DeleteMassRecord.Button_Delete_Mass_Record().delete_intention_row()
        # gui.InsertTab.DeleteMassRecord.Button_Delete_Mass_Record().delete_last()
        # gui.InsertTab.UpdateStmts.ButtonUpdateMonthlyStmt().update_monthly_stmt('2022-10')
        # gui.InsertTab.UpdateStmts.ButtonUpdateGeneralStmt().update_general_stmt('2022-10')

        ####gui.SettingsTab.Button_BuildNewDatabase.Build_DB_Button().build_database()
        ####gui.SettingsTab.Button_BuildNewDatabase.Drop_DB_Button().drop_database()
        ####gui.SettingsTab.Button_BuildNewDatabase.Remove_DB_Files.remove_db_file()



if __name__ == '__main__':
    unittest.main()
