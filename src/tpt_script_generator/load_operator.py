from typing import List, Optional, Union
from tpt_script_generator.enums.load_operator import (
    TASMFASTFAIL,
    BufferSizeUnit,
    CheckpointRowCount,
    DataEncryption,
    DateForm,
    DropErrorTable,
    DropLogTable,
    LogSQL,
    NotifyExitIsDLL,
    NotifyLevel,
    NotifyMethod,
    PauseAcq,
    UnicodePassThrough,
    WildcardInsert,
)
from tpt_script_generator.base_operator import Operator
from tpt_script_generator.enums import AttributeType


class LoadOperator(Operator):
    def __init__(self):
        super().__init__("LoadOperator", "LOAD")

    def with_account_id(self, account_id: Optional[str]) -> "LoadOperator":
        return self.with_attribute(AttributeType.VARCHAR, "AccountId", account_id)

    def with_buffer_size(
        self, buffer_size: Optional[int], unit: BufferSizeUnit = BufferSizeUnit.KB
    ) -> "LoadOperator":
        if buffer_size is not None and (buffer_size < 1 or buffer_size > 16384):
            raise ValueError("BufferSize must be between 1 and 16384.")
        buffer_size_str = f"{buffer_size}" if buffer_size is not None else None
        return self.with_attribute(AttributeType.INTEGER, "BufferSize", buffer_size_str)

    def with_checkpoint_row_count(self, option: CheckpointRowCount) -> "LoadOperator":
        return self.with_attribute(
            AttributeType.VARCHAR, "CheckpointRowCount", option.value
        )

    def with_connect_string(self, connect_string: Optional[str]) -> "LoadOperator":
        return self.with_attribute(
            AttributeType.VARCHAR, "ConnectString", connect_string
        )

    def with_data_encryption(self, option: DataEncryption) -> "LoadOperator":
        return self.with_attribute(
            AttributeType.VARCHAR, "DataEncryption", option.value
        )

    def with_date_form(self, option: DateForm) -> "LoadOperator":
        return self.with_attribute(AttributeType.VARCHAR, "DateForm", option.value)

    def with_drop_error_table(self, option: DropErrorTable) -> "LoadOperator":
        return self.with_attribute(
            AttributeType.VARCHAR, "DropErrorTable", option.value
        )

    def with_drop_log_table(self, option: DropLogTable) -> "LoadOperator":
        return self.with_attribute(AttributeType.VARCHAR, "DropLogTable", option.value)

    def with_error_limit(self, error_limit: Optional[int]) -> "LoadOperator":
        if error_limit is not None and error_limit < 1:
            raise ValueError("ErrorLimit must be greater than 0.")
        return self.with_attribute(AttributeType.INTEGER, "ErrorLimit", error_limit)

    def with_error_table1(self, error_table1: Optional[str]) -> "LoadOperator":
        return self.with_attribute(AttributeType.VARCHAR, "ErrorTable1", error_table1)

    def with_error_table2(self, error_table2: Optional[str]) -> "LoadOperator":
        return self.with_attribute(AttributeType.VARCHAR, "ErrorTable2", error_table2)

    def with_logon_mech(self, logon_mech: Optional[str]) -> "LoadOperator":
        if logon_mech is not None and len(logon_mech) > 8:
            raise ValueError("LogonMech must not exceed 8 bytes.")
        return self.with_attribute(AttributeType.VARCHAR, "LogonMech", logon_mech)

    def with_logon_mech_data(self, logon_mech_data: Optional[str]) -> "LoadOperator":
        return self.with_attribute(
            AttributeType.VARCHAR, "LogonMechData", logon_mech_data
        )

    def with_log_sql(self, option: LogSQL) -> "LoadOperator":
        return self.with_attribute(AttributeType.VARCHAR, "LogSQL", option.value)

    def with_log_table(self, log_table: Optional[str]) -> "LoadOperator":
        return self.with_attribute(AttributeType.VARCHAR, "LogTable", log_table)

    def with_max_sessions(self, max_sessions: Optional[int]) -> "LoadOperator":
        if max_sessions is not None and max_sessions < 1:
            raise ValueError("MaxSessions must be greater than 0.")
        return self.with_attribute(AttributeType.INTEGER, "MaxSessions", max_sessions)

    def with_min_sessions(self, min_sessions: Optional[int]) -> "LoadOperator":
        if min_sessions is not None and min_sessions < 1:
            raise ValueError("MinSessions must be greater than 0.")
        return self.with_attribute(AttributeType.INTEGER, "MinSessions", min_sessions)

    def with_notify_exit(self, notify_exit: Optional[str]) -> "LoadOperator":
        return self.with_attribute(AttributeType.VARCHAR, "NotifyExit", notify_exit)

    def with_notify_exit_is_dll(self, option: NotifyExitIsDLL) -> "LoadOperator":
        return self.with_attribute(
            AttributeType.VARCHAR, "NotifyExitIsDLL", option.value
        )

    def with_notify_level(self, notify_level: NotifyLevel) -> "LoadOperator":
        return self.with_attribute(
            AttributeType.VARCHAR, "NotifyLevel", notify_level.value
        )

    def with_notify_method(self, notify_method: NotifyMethod) -> "LoadOperator":
        return self.with_attribute(
            AttributeType.VARCHAR, "NotifyMethod", notify_method.value
        )

    def with_notify_string(self, notify_string: Optional[str]) -> "LoadOperator":
        if notify_string is not None and len(notify_string) > 80:
            raise ValueError("NotifyString must not exceed 80 bytes.")
        return self.with_attribute(AttributeType.VARCHAR, "NotifyString", notify_string)

    def with_pause_acq(self, option: PauseAcq) -> "LoadOperator":
        return self.with_attribute(AttributeType.VARCHAR, "PauseAcq", option.value)

    def with_private_log_name(self, log_name: Optional[str]) -> "LoadOperator":
        return self.with_attribute(AttributeType.VARCHAR, "PrivateLogName", log_name)

    def with_query_band_sess_info(
        self, query_band_expression: Optional[Union[str, List[str]]]
    ) -> "LoadOperator":
        return self.with_attribute(
            AttributeType.VARCHAR, "QueryBandSessInfo", query_band_expression
        )

    def with_role_name(
        self, role_name: Optional[Union[str, List[str]]]
    ) -> "LoadOperator":
        return self.with_attribute(AttributeType.VARCHAR, "RoleName", role_name)

    def with_target_table(self, target_table_name: str) -> "LoadOperator":
        return self.with_attribute(
            AttributeType.VARCHAR, "TargetTable", target_table_name
        )

    def with_tasm_fast_fail(self, option: TASMFASTFAIL) -> "LoadOperator":
        return self.with_attribute(AttributeType.VARCHAR, "TASMFASTFAIL", option.value)

    def with_tenacity_hours(self, hours: Optional[int]) -> "LoadOperator":
        if hours is not None and hours < 0:
            raise ValueError("TenacityHours must be greater than or equal to 0.")
        return self.with_attribute(AttributeType.INTEGER, "TenacityHours", hours)

    def with_tenacity_sleep(self, minutes: Optional[int]) -> "LoadOperator":
        if minutes is not None and minutes < 1:
            raise ValueError("TenacitySleep must be greater than or equal to 1.")
        return self.with_attribute(AttributeType.INTEGER, "TenacitySleep", minutes)

    def with_tdp_id(self, dbc_name: Optional[str]) -> "LoadOperator":
        return self.with_attribute(AttributeType.VARCHAR, "TdpId", dbc_name)

    def with_time_zone_sess_info(
        self, time_zone_value: Optional[str]
    ) -> "LoadOperator":
        return self.with_attribute(
            AttributeType.VARCHAR, "TimeZoneSessInfo", time_zone_value
        )

    def with_trace_level(
        self, trace_level: Optional[Union[str, List[str]]]
    ) -> "LoadOperator":
        return self.with_attribute(
            AttributeType.VARCHAR, "TraceLevel", trace_level.value
        )

    def with_transform_group(
        self, transform_group_name: Optional[Union[str, List[str]]]
    ) -> "LoadOperator":
        return self.with_attribute(
            AttributeType.VARCHAR, "TransformGroup", transform_group_name
        )

    def with_unicode_pass_through(self, option: UnicodePassThrough) -> "LoadOperator":
        return self.with_attribute(
            AttributeType.VARCHAR, "UnicodePassThrough", option.value
        )

    def with_user_name(self, user_name: Optional[str]) -> "LoadOperator":
        return self.with_attribute(AttributeType.VARCHAR, "UserName", user_name)

    def with_user_password(self, password: Optional[str]) -> "LoadOperator":
        return self.with_attribute(AttributeType.VARCHAR, "UserPassword", password)

    def with_wildcard_insert(self, option: WildcardInsert) -> "LoadOperator":
        return self.with_attribute(
            AttributeType.VARCHAR, "WildcardInsert", option.value
        )

    def with_working_database(self, database_name: Optional[str]) -> "LoadOperator":
        return self.with_attribute(
            AttributeType.VARCHAR, "WorkingDatabase", database_name
        )
