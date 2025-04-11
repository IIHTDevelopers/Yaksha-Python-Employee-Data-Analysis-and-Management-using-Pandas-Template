import unittest
import pandas as pd
from mainclass import EmployeeAnalysis
from test.TestUtils import TestUtils
import os
class FunctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analysis = EmployeeAnalysis("employee_data.csv")
        cls.test_obj = TestUtils()

    def test_csv_loading(self):
        """Test if the CSV file is loaded correctly."""
        try:
            if not self.analysis:
                self.test_obj.yakshaAssert("TestCSVLoading", False, "functional")
                print("TestCSVLoading = Failed")
                return
            obj = not self.analysis.df.empty
            self.test_obj.yakshaAssert("TestCSVLoading", obj, "functional")
            print("TestCSVLoading = Passed" if obj else "TestCSVLoading = Failed")
        except:
            self.test_obj.yakshaAssert("TestCSVLoading", False, "functional")
            print("TestCSVLoading = Failed")
                
    def test_display_head(self):
        """Test if the first 5 rows are returned correctly."""
        try:
            head = self.analysis.display_head()
            if head is None:
                head = []
            obj = len(head) == 5
            self.test_obj.yakshaAssert("TestDisplayHead", obj, "functional")
            print("TestDisplayHead = Passed" if obj else "TestDisplayHead = Failed")
        except Exception as e:
            print("TestDisplayHead = Failed", str(e))

    def test_highest_age_employee(self):
        """Check if the employee with the highest age is identified correctly."""
        if not self.analysis:
            self.test_obj.yakshaAssert("TestHighestAgeEmployee", False, "functional")
            print("TestHighestAgeEmployee = Failed")
            return
        obj = self.analysis.highest_age_employee() == "Anna"
        self.test_obj.yakshaAssert("TestHighestAgeEmployee", obj, "functional")
        print("TestHighestAgeEmployee = Passed" if obj else "TestHighestAgeEmployee = Failed")

    def test_add_age_category_column(self):
        """Check if the Age Category column is created correctly."""
        try:
            self.analysis.add_age_category()
            obj = "Age Category" in self.analysis.df.columns
            self.test_obj.yakshaAssert("TestAddAgeCategoryColumn", obj, "functional")
            print("TestAddAgeCategoryColumn = Passed" if obj else "TestAddAgeCategoryColumn = Failed")
        except:
            self.test_obj.yakshaAssert("TestAddAgeCategoryColumn", False, "functional")
            print("TestAddAgeCategoryColumn = Failed")
        
    def test_export_updated_csv(self):
        """Check if the updated CSV file is saved correctly."""
        self.analysis.export_updated_csv()
        try:
            pd.read_csv("updated_employee_data.csv")
            obj = True
        except FileNotFoundError:
            obj = False
        self.test_obj.yakshaAssert("TestExportUpdatedCSV", obj, "functional")
        print("TestExportUpdatedCSV = Passed" if obj else "TestExportUpdatedCSV = Failed")
