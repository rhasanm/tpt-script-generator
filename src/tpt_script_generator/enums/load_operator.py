from enum import Enum


class BufferSizeUnit(Enum):
    KB = "KBytes"


class CheckpointRowCount(Enum):
    NO = "No"
    YES = "Yes"


class DataEncryption(Enum):
    ON = "On"
    OFF = "Off"


class DateForm(Enum):
    INTEGER_DATE = "integerDate"
    ANSI_DATE = "ansiDate"


class DropErrorTable(Enum):
    YES = "Yes"
    NO = "No"


class DropLogTable(Enum):
    YES = "Yes"
    NO = "No"


class LogSQL(Enum):
    YES = "Yes"
    NO = "No"


class NotifyExitIsDLL(Enum):
    YES = "Yes"
    NO = "No"


class NotifyLevel(Enum):
    OFF = "Off"
    LOW = "Low"
    MED = "Med"
    HIGH = "High"


class NotifyMethod(Enum):
    NONE = "None"
    MSG = "Msg"
    EXIT = "Exit"
    EXIT64 = "Exit64"
    EXITEON = "ExitEON"


class PauseAcq(Enum):
    NO = "No"
    YES = "Yes"


class TASMFASTFAIL(Enum):
    YES = "Yes"
    NO = "No"


class TreatDBSRestartAsFatal(Enum):
    NO = "No"
    YES = "Yes"


class UnicodePassThrough(Enum):
    ON = "On"
    OFF = "Off"


class WildcardInsert(Enum):
    YES = "Yes"
    NO = "No"


class TraceLevelOption(Enum):
    NONE = "None"
    CLI = "CLI"
    PX = "PX"
    OPER = "OPER"
    ALL = "All"


class DataEncryptionOption(Enum):
    ON = "On"
    OFF = "Off"


class LogSQLOption(Enum):
    YES = "Yes"
    NO = "No"
