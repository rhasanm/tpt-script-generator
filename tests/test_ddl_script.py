import unittest
from tpt_script_generator.script import TPTScript
from tpt_script_generator.ddl_operator import (
    DDLOperator,
    DataEncryptionOption,
    LogSQLOption,
    TraceLevelOption,
)
from tpt_script_generator.step import Step


class TestDDLTPTScript(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_script_generation(self):
        builder = (
            TPTScript("LoadFromOracle")
            .with_description("Load data from Oracle using UnixODBC into Teradata")
            .with_var("DDLTdpId", "@var_tdpid")
            .with_var("DDLUserName", "@var_username")
            .with_var("DDLUserPassword", "@var_password")
            .with_var("DDLErrorList", "'3807'")
            .with_var("DDLPrivateLogName", "'DDL_OPERATOR_LOG'")
            .with_var("TargetTable", "@var_target_table")
            .with_schema(
                "SourceSchema",
                {
                    "WORKFLOW_NAME": "VARCHAR(240)",
                    "SERVER_NAME": "VARCHAR(240)",
                    "SUBJECT_AREA": "VARCHAR(240)",
                },
            )
            .with_operator(
                DDLOperator()
                .with_account_id("acctId")
                .with_connect_string("connectionString")
                .with_data_encryption(DataEncryptionOption.ON)
                .with_error_list("3807")
                .with_logon_mech("logonMech")
                .with_logon_mech_data("logonMechData")
                .with_log_sql(LogSQLOption.YES)
                .with_trace_level(TraceLevelOption.CLI)
            )
            .with_step(
                Step("CLEANUP")
                .add_operation("APPLY ('DROP TABLE   ' || @TargetTable || '_WT  ; ')")
                .add_operation("('DROP TABLE   ' || @TargetTable || '_ET  ; ')")
                .add_operation("('DROP TABLE   ' || @TargetTable || '_UV  ; ')")
                .add_operation("('DROP TABLE   ' || @TargetTable || '_LOG ; ')")
                .add_operation("('DELETE FROM  ' || @TargetTable || '     ; ')")
                .add_operation("TO OPERATOR ($DDL)")
            )
            .with_step(
                Step("Load_Table")
                .add_operation("APPLY @var_insert_stmt")
                .add_operation("TO OPERATOR (TD_Insert)")
                .add_operation("SELECT * FROM OPERATOR (ODBC_Reader);")
            )
            .build()
        )

        expected_script = """DEFINE JOB LoadFromOracle
DESCRIPTION 'Load data from Oracle using UnixODBC into Teradata'
(
    SET DDLTdpId = @var_tdpid
    SET DDLUserName = @var_username
    SET DDLUserPassword = @var_password
    SET DDLErrorList = '3807'
    SET DDLPrivateLogName = 'DDL_OPERATOR_LOG'
    SET TargetTable = @var_target_table
    DEFINE SCHEMA SourceSchema
    (
        "WORKFLOW_NAME" VARCHAR(240),
        "SERVER_NAME" VARCHAR(240),
        "SUBJECT_AREA" VARCHAR(240)
    );

    DEFINE OPERATOR DDLOperator
    TYPE DDL
    ATTRIBUTES
    (
        VARCHAR AccountId = 'acctId',
        VARCHAR ConnectString = 'connectionString',
        VARCHAR DataEncryption = 'ON',
        VARCHAR ErrorList = '3807',
        VARCHAR LogonMech = 'logonMech',
        VARCHAR LogonMechData = 'logonMechData',
        VARCHAR LogSQL = 'Yes',
        VARCHAR TraceLevel = 'CLI'
    );

    STEP CLEANUP
    (
        APPLY ('DROP TABLE   ' || @TargetTable || '_WT  ; ')
        ('DROP TABLE   ' || @TargetTable || '_ET  ; ')
        ('DROP TABLE   ' || @TargetTable || '_UV  ; ')
        ('DROP TABLE   ' || @TargetTable || '_LOG ; ')
        ('DELETE FROM  ' || @TargetTable || '     ; ')
        TO OPERATOR ($DDL)
    );

    STEP Load_Table
    (
        APPLY @var_insert_stmt
        TO OPERATOR (TD_Insert)
        SELECT * FROM OPERATOR (ODBC_Reader);
    );

);
"""
        self.assertEqual(builder, expected_script)


if __name__ == "__main__":
    unittest.main()
