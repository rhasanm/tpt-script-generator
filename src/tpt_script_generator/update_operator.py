from typing import List, Union
from tpt_script_generator.enums import AttributeType
from tpt_script_generator.base_operator import Operator
from tpt_script_generator.enums.update_operator import LogSQL, LogonMech, NotifyLevel, NotifyMethod, ReplicationOverride, RoleName, TraceLevel, TransformGroup, UnicodePassThrough

class UpdateOperator(Operator):
    def __init__(self):
        super().__init__("UpdateOperator", "Update")

    def with_account_id(self, account_id: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "AccountId", account_id)
        return self

    def with_amp_check(self, option: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "AmpCheck", option)
        return self

    def with_buffer_size(self, kbytes: int) -> 'UpdateOperator':
        self.with_attribute(AttributeType.INTEGER, "BufferSize", kbytes)
        return self

    def with_checkpoint_row_count(self, option: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "CheckpointRowCount", option)
        return self

    def with_connect_string(self, connect_string: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "ConnectString", connect_string)
        return self

    def with_data_encryption(self, option: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "DataEncryption", option)
        return self

    def with_date_form(self, option: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "DateForm", option)
        return self
        
    def with_delete_lob_data_files(self, option: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "DeleteLobDataFiles", option)
        return self

    def with_delete_task(self, option: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "DeleteTask", option)
        return self

    def with_drop_error_table(self, option: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "DropErrorTable", option)
        return self

    def with_drop_log_table(self, option: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "DropLogTable", option)
        return self

    def with_drop_work_table(self, option: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "DropWorkTable", option)
        return self

    def with_error_limit(self, limit: int) -> 'UpdateOperator':
        self.with_attribute(AttributeType.INTEGER, "ErrorLimit", limit)
        return self

    def with_error_table1(self, error_table1_name: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "ErrorTable1", error_table1_name)
        return self

    def with_error_table2(self, error_table2_name: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "ErrorTable2", error_table2_name)
        return self

    def with_logon_mech(self, logon_mech: LogonMech) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "LogonMech", logon_mech.value)
        return self

    def with_logon_mech_data(self, logon_mech_data: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "LogonMechData", logon_mech_data)
        return self

    def with_log_sql(self, option: LogSQL) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "LogSQL", option.value)
        return self

    def with_log_table(self, log_table_name: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "LogTable", log_table_name)
        return self

    def with_max_sessions(self, max_sessions: int) -> 'UpdateOperator':
        self.with_attribute(AttributeType.INTEGER, "MaxSessions", max_sessions)
        return self

    def with_min_sessions(self, min_sessions: int) -> 'UpdateOperator':
        self.with_attribute(AttributeType.INTEGER, "MinSessions", min_sessions)
        return self

    def with_notify_exit(self, inmod_name: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "NotifyExit", inmod_name)
        return self

    def with_notify_exit_is_dll(self, option: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "NotifyExitIsDLL", option)
        return self

    def with_notify_level(self, notify_level: NotifyLevel) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "NotifyLevel", notify_level.value)
        return self

    def with_notify_method(self, notify_method: NotifyMethod) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "NotifyMethod", notify_method.value)
        return self

    def with_notify_string(self, notify_string: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "NotifyString", notify_string)
        return self

    def with_pack(self, number: int) -> 'UpdateOperator':
        self.with_attribute(AttributeType.INTEGER, "Pack", number)
        return self

    def with_pause_acq(self, option: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "PauseAcq", option)
        return self

    def with_private_log_name(self, log_name: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "PrivateLogName", log_name)
        return self

    def with_query_band_sess_info(self, query_band_expression: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "QueryBandSessInfo", query_band_expression)
        return self

    def with_replication_override(self, option: ReplicationOverride) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "ReplicationOverride", option.value)
        return self

    def with_role_name(self, role_name: Union[RoleName, List[RoleName]]) -> 'UpdateOperator':
        if isinstance(role_name, list):
            self.with_attribute(AttributeType.VARCHAR_ARRAY, "RoleName", [r.value for r in role_name])
        else:
            self.with_attribute(AttributeType.VARCHAR, "RoleName", role_name.value)
        return self

    def with_target_table(self, target_table_name: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "TargetTable", target_table_name)
        return self

    def with_tasmfastfail(self, value: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "TASMFASTFAIL", value)
        return self

    def with_tenacity_hours(self, hours: int) -> 'UpdateOperator':
        self.with_attribute(AttributeType.INTEGER, "TenacityHours", hours)
        return self

    def with_tenacity_sleep(self, minutes: int) -> 'UpdateOperator':
        self.with_attribute(AttributeType.INTEGER, "TenacitySleep", minutes)
        return self

    def with_tdp_id(self, dbc_name: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "TdpId", dbc_name)
        return self

    def with_time_zone_sess_info(self, time_zone_value: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "TimeZoneSessInfo", time_zone_value)
        return self

    def with_trace_level(self, level: Union[TraceLevel, List[TraceLevel]]) -> 'UpdateOperator':
        if isinstance(level, list):
            self.with_attribute(AttributeType.VARCHAR_ARRAY, "TraceLevel", [l.value for l in level])
        else:
            self.with_attribute(AttributeType.VARCHAR, "TraceLevel", level.value)
        return self

    def with_transform_group(self, transform_group_name: Union[TransformGroup, List[TransformGroup]]) -> 'UpdateOperator':
        if isinstance(transform_group_name, list):
            self.with_attribute(AttributeType.VARCHAR_ARRAY, "TransformGroup", [t.value for t in transform_group_name])
        else:
            self.with_attribute(AttributeType.VARCHAR, "TransformGroup", transform_group_name.value)
        return self

    def with_treat_dbs_restart_as_fatal(self, option: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "TreatDBSRestartAsFatal", option)
        return self

    def with_unicode_pass_through(self, value: UnicodePassThrough) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "UnicodePassThrough", value.value)
        return self

    def with_user_name(self, user_id: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "UserName", user_id)
        return self

    def with_user_password(self, password: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "UserPassword", password)
        return self

    def with_work_table(self, work_table_name: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "WorkTable", work_table_name)
        return self

    def with_working_database(self, database_name: str) -> 'UpdateOperator':
        self.with_attribute(AttributeType.VARCHAR, "WorkingDatabase", database_name)
        return self
