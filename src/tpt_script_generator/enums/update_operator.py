from enum import Enum

class LogonMech(Enum):
    TERADATA = 'TERADATA'
    LDAP = 'LDAP'
    KERBEROS = 'KERBEROS'
    NTLM = 'NTLM'
    NO_AUTH = 'NO_AUTH'
    EXTERNAL = 'EXTERNAL'

class LogSQL(Enum):
    NONE = 'NONE'
    SQL = 'SQL'
    DETAIL = 'DETAIL'

class NotifyMethod(Enum):
    NONE = 'None'
    MSG = 'Msg'
    EXIT = 'Exit'
    EXIT64 = 'Exit64'
    EXITEON = 'ExitEON'

class NotifyLevel(Enum):
    NONE = 'None'
    ERRORS = 'Errors'
    WARNINGS = 'Warnings'
    ALL = 'All'

class ReplicationOverride(Enum):
    ON = 'On'
    OFF = 'Off'
    NONE = 'None'

class RoleName(Enum):
    ADMIN = 'Admin'
    USER = 'User'
    GUEST = 'Guest'

class TASMFASTFAIL(Enum):
    YES = 'Yes'
    NO = 'No'

class TransformGroup(Enum):
    JSON = 'JSON CHARACTER SET LATIN TD_JSON_VARCHAR'
    ST_GEOMETRY = 'ST_GEOMETRY TD_GEO_VARCHAR'

class TreatDBSRestartAsFatal(Enum):
    YES = 'Yes'
    NO = 'No'

class UnicodePassThrough(Enum):
    ON = 'On'
    OFF = 'Off'

class TraceLevel(Enum):
    NONE = 'None'
    CLI = 'CLI'
    PX = 'PX'
    OPER = 'Oper'
    NOTIFY = 'Notify'
    ALL = 'All'

class PauseAcq(Enum):
    YES = 'Yes'
    NO = 'No'

class TimeZoneSessInfo(Enum):
    LOCAL = 'LOCAL'
    USER = 'USER'
    PACIFIC = 'America Pacific'