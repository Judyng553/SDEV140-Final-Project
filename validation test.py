import unittest
from tkinter import Tk
from EventPlannerApp import EventPlannerApp 

class TestEventPlannerApp(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.app = EventPlannerApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_valid_event(self):
        # Test case: Valid Event
        self.app.event_name_entry.insert(0, "Birthday Party")
        self.app.event_date_entry.insert(0, "2023-12-25")
        self.app.event_time_entry.insert(0, "15:30")
        self.app.event_location_entry.insert(0, "My House")

        result = self.app.save_event()
        print(result)  # Add this line

        # Assert that the result is True
        self.assertTrue(result)  # Assuming your save_event method returns True on success

        # Check that the features logo pop-up appears
        self.assertTrue(self.app.show_features_popup_called)

    def test_empty_event_name(self):
        # Test case: Empty Event Name
        self.app.event_name_entry.insert(0, "")        
        self.app.event_date_entry.insert(0, "2023-12-25")
        self.app.event_time_entry.insert(0, "15:30")
        self.app.event_location_entry.insert(0, "My House")

        result = self.app.save_event()
        self.assertFalse(result)  # Assuming your save_event method returns False on failure
        # Check that an error message is displayed (you may need to add a method/property to check this)

    def test_invalid_date_format(self):
        # Test case: Invalid Date Format
        self.app.event_name_entry.insert(0, "Birthday Party")        
        self.app.event_date_entry.insert(0, "2023-2-25")
        self.app.event_time_entry.insert(0, "15:30")
        self.app.event_location_entry.insert(0, "My House")

        result = self.app.save_event()
        self.assertFalse(result)  # Assuming your save_event method returns False on failure
        # Check that an error message is displayed

    def test_missing_event_time(self):
        # Test case: Missing Event Time
        self.app.event_name_entry.insert(0, "Birthday Party")        
        self.app.event_date_entry.insert(0, "2023-12-25")
        self.app.event_time_entry.insert(0, "")
        self.app.event_location_entry.insert(0, "My House")

        result = self.app.save_event()
        self.assertFalse(result)  # Assuming your save_event method returns False on failure
        # Check that an error message is displayed

if __name__ == '__main__':
    unittest.main()
