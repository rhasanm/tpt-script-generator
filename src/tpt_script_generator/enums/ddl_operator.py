from enum import Enum

class DataEncryptionOption(Enum):
    ON = "ON"
    OFF = "OFF"

class LogSQLOption(Enum):
    YES = "Yes"
    NO = "No"

class TraceLevelOption(Enum):
    NONE = "None"
    CLI = "CLI"
    PX = "PX"
    OPER = "OPER"
    ALL = "All"

class TreatDBSRestartAsFatalOption(Enum):
    YES = "Yes"
    NO = "No"

class UnicodePassThroughOption(Enum):
    ON = "On"
    OFF = "Off"

class RestartAtFirstDMLGroupOption(Enum):
    YES = "Yes"
    NO = "No"