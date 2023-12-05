# -----------------------------------------------------------
# Utils module
#
# (C) 2021-2022 Juan-Francisco Reyes, Cottbus, Germany
# Brandenburg University of Technology, Germany.
# Released under MIT License
# email pacoreyes.zwei@gmail.com
# -----------------------------------------------------------
import pickle
import json
from enum import Enum
from typing import Any, Dict, List
import gspread


# Save data to a Pickle file
def save_pickle_file(data: Any, filename: str) -> None:
    """
  Save data to a Pickle file.

  Args:
      data: The data to be saved.
      filename (str): The filename of the Pickle file.
  """
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


# Load data from a Pickle file
def load_pickle_file(filename: str) -> Any:
    """
  Load data from a Pickle file.

  Args:
      filename (str): The filename of the Pickle file.

  Returns:
      The loaded data.
  """
    with open(filename, 'rb') as f:
        return pickle.load(f)


# Save data as JSON file
def save_json_file(data: Any, filename: str) -> None:
    """
  Save data as a JSON file.

  Args:
      data: The data to be saved.
      filename (str): The filename of the JSON file.
  """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


# Open the JSON file
def load_json_file(filename: str) -> Any:
    """
  Load data from a JSON file.

  Args:
      filename (str): The filename of the JSON file.

  Returns:
      The loaded data.
  """
    with open(filename) as json_file:
        return json.load(json_file)


# This function writes data to a Google Sheet
def write_to_google_sheet(spreadsheet: gspread.Spreadsheet, sheet_name: str, data: List[str]) -> gspread.Worksheet:
    sheet = spreadsheet.worksheet(sheet_name)  # Get the sheet
    # Convert list of strings to list of lists (one string per row)
    data_list = [[item] for item in data]
    # Write data to the sheet all at once, starting from the cell A2
    sheet.update('A2', data_list)
    return sheet


# This function reads data from a Google Sheet
def read_from_google_sheet(spreadsheet: gspread.Spreadsheet, sheet_name: str) -> List[Dict[str, str]]:
    sheet = spreadsheet.worksheet(sheet_name)  # Get the sheet
    # Get all values from the sheet
    values = sheet.get_all_values()
    # Extract keys from the first row
    keys = values[0]
    # Extract values from the remaining rows
    value_rows = values[1:]
    # Return a list of dictionaries, one for each row of values
    return [dict(zip(keys, value_row)) for value_row in value_rows]


# Enumerations for content type
class ContentType(Enum):
    """
  Enumerations for content types.

  Each enumeration represents a different content type.
  """
    SPEECH = "Speech"
    INTERVIEW = "Interview"
    REMARKS = "Remarks"
    STATEMENT = "Statement"
    TRANSCRIPT = "Transcript"
    PRESS_CONFERENCE = "Press Conference"
    PRESS_RELEASE = "Press Release"
    TALK = "Talk"
    DEBATE = "Debate"
    BRIEFING = "Briefing"
    UPDATE = "Update"
    READOUT = "Readout"
    OP_ED = "Op-Ed"
    MEETING = "Meeting"
    SPEAK = "Speak"
    VOW = "Vow"
    APPEARANCE = "Appearance"
    HEARING = "Hearing"
    ROUNDTABLE = "Roundtable"
    DISCUSSION = "Discussion"
    PANEL = "Panel"
    LETTER = "Letter"
    MEMORANDUM = "Memorandum"
    PROCLAMATION = "Proclamation"
    EXECUTIVE_ORDER = "Executive Order"
    LEGISLATIVE_PROPOSAL = "Legislative Proposal"
    RALLY = "Rally"
    TESTIMONY = "Testimony"
    ADDRESS = "Address"
    SUMMIT = "Summit"
    FORUM = "Forum"
    LIVESTREAM = "Livestream"
    ANNOUNCEMENT = "Announcement"
    INTRODUCE = "Introduce"
    PRESENT = "Present"
    ANNOUNCE = "Announce"
    ARGUE = "Argue"
    ARGUMENT = "Argument"
    TOWN_HALL = "Town Hall"
    QUESTION = "Question"
    ANSWER = "Answer"
    TELECONFERENCE = "Teleconference"
    MEET = "Meet"
    ASK = "Ask"
    SLAM = "Slam"
    DELIVER = "Deliver"
    HOLD = "Hold"
    APPROVE = "Approve"
    LAUNCH = "Launch"
    RESPOND = "Respond"


def read_position_from_google_sheet(spreadsheet: gspread.Spreadsheet, sheet_name: str, cell: str) -> int:
    sheet = spreadsheet.worksheet(sheet_name)  # Get the sheet
    value = sheet.acell(cell).value
    try:
        return int(value)
    except ValueError:
        return 0


def write_position_to_google_sheet(spreadsheet: gspread.Spreadsheet, sheet_name: str, data: int) -> gspread.Worksheet:
    sheet = spreadsheet.worksheet(sheet_name)  # Get the sheet
    # Convert the integer to a string
    data_str = str(data)
    # Write data to the sheet all at once, starting from the cell A2
    sheet.update('A1', [[data_str]])
    return sheet
