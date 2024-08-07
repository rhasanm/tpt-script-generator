from enum import Enum


class AttributeType(Enum):
    """Enum for attribute types used in TPT scripts."""

    VARCHAR = "VARCHAR"
    INTEGER = "INTEGER"
    VARCHAR_ARRAY = "VARCHAR_ARRAY"


from tpt_script_generator.enums.update_operator import (
    LogonMech,
    LogSQL,
    NotifyLevel,
    NotifyMethod,
    PauseAcq,
    ReplicationOverride,
    RoleName,
    TASMFASTFAIL,
    TimeZoneSessInfo,
    TraceLevel,
    TransformGroup,
    TreatDBSRestartAsFatal,
    UnicodePassThrough,
)
