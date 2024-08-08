from tpt_script_generator.base_operator import Operator
from tpt_script_generator.enums import AttributeType
from tpt_script_generator.enums.ddl_operator import (
    DataEncryptionOption,
    LogSQLOption,
    RestartAtFirstDMLGroupOption,
    TraceLevelOption,
    TreatDBSRestartAsFatalOption,
    UnicodePassThroughOption,
)


class DDLOperator(Operator):
    def __init__(self):
        super().__init__("DDLOperator", "DDL")

    def with_account_id(self, account_id):
        self.with_attribute(AttributeType.VARCHAR, "AccountId", account_id)
        return self

    def with_connect_string(self, connect_string):
        self.with_attribute(AttributeType.VARCHAR, "ConnectString", connect_string)
        return self

    def with_data_encryption(self, option: DataEncryptionOption):
        self.with_attribute(AttributeType.VARCHAR, "DataEncryption", option.value)
        return self

    def with_error_list(self, error_list):
        self.with_attribute(AttributeType.VARCHAR, "ErrorList", error_list)
        return self

    def with_logon_mech(self, logon_mech):
        self.with_attribute(AttributeType.VARCHAR, "LogonMech", logon_mech)
        return self

    def with_logon_mech_data(self, logon_mech_data):
        self.with_attribute(AttributeType.VARCHAR, "LogonMechData", logon_mech_data)
        return self

    def with_log_sql(self, log_sql: LogSQLOption):
        self.with_attribute(AttributeType.VARCHAR, "LogSQL", log_sql.value)
        return self

    def with_private_log_name(self, private_log_name):
        self.with_attribute(AttributeType.VARCHAR, "PrivateLogName", private_log_name)
        return self

    def with_query_band_sess_info(self, query_band_sess_info):
        self.with_attribute(
            AttributeType.VARCHAR, "QueryBandSessInfo", query_band_sess_info
        )
        return self

    def with_replication_override(self, option: TreatDBSRestartAsFatalOption):
        self.with_attribute(AttributeType.VARCHAR, "ReplicationOverride", option.value)
        return self

    def with_restart_at_first_dml_group(self, option: RestartAtFirstDMLGroupOption):
        self.with_attribute(
            AttributeType.VARCHAR, "RestartAtFirstDMLGroup", option.value
        )
        return self

    def with_role_name(self, role_name):
        self.with_attribute(AttributeType.VARCHAR, "RoleName", role_name)
        return self

    def with_splopt(self, option: UnicodePassThroughOption):
        self.with_attribute(AttributeType.VARCHAR, "SPLOPT", option.value)
        return self

    def with_sql_cmd_file_name(self, sql_cmd_file_name):
        self.with_attribute(AttributeType.VARCHAR, "SQLCmdFileName", sql_cmd_file_name)
        return self

    def with_tdp_id(self, tdp_id):
        self.with_attribute(AttributeType.VARCHAR, "TdpId", tdp_id)
        return self

    def with_time_zone_sess_info(self, time_zone_sess_info):
        self.with_attribute(
            AttributeType.VARCHAR, "TimeZoneSessInfo", time_zone_sess_info
        )
        return self

    def with_trace_level(self, trace_level: TraceLevelOption):
        self.with_attribute(AttributeType.VARCHAR, "TraceLevel", trace_level.value)
        return self

    def with_transform_group(self, transform_group):
        self.with_attribute(AttributeType.VARCHAR, "TransformGroup", transform_group)
        return self

    def with_treat_dbs_restart_as_fatal(self, option: TreatDBSRestartAsFatalOption):
        self.with_attribute(
            AttributeType.VARCHAR, "TreatDBSRestartAsFatal", option.value
        )
        return self

    def with_unicode_pass_through(self, option: UnicodePassThroughOption):
        self.with_attribute(AttributeType.VARCHAR, "UnicodePassThrough", option.value)
        return self

    def with_username(self, username):
        self.with_attribute(AttributeType.VARCHAR, "Username", username)
        return self

    def with_user_password(self, user_password):
        self.with_attribute(AttributeType.VARCHAR, "UserPassword", user_password)
        return self

    def with_working_database(self, working_database):
        self.with_attribute(AttributeType.VARCHAR, "WorkingDatabase", working_database)
        return self
