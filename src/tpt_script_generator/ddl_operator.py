from tpt_script_generator.enums import AttributeType
from tpt_script_generator.base_operator import Operator

class DDLOperator(Operator):
    def __init__(self):
        super().__init__("DDLOperator", "DDL")

    def with_account_id(self, account_id):
        self.with_attribute(AttributeType.VARCHAR, "AccountId", account_id)
        return self

    def with_array(self):
        self.with_attribute(AttributeType.VARCHAR, "ARRAY", "")
        return self

    def with_connect_string(self, connect_string):
        self.with_attribute(AttributeType.VARCHAR, "ConnectString", connect_string)
        return self

    def with_data_encryption(self, option):
        self.with_attribute(AttributeType.VARCHAR, "DataEncryption", option)
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

    def with_log_sql(self, log_sql):
        self.with_attribute(AttributeType.VARCHAR, "LogSQL", log_sql)
        return self
