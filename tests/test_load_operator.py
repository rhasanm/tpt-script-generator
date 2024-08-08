import unittest

from tpt_script_generator import LoadOperator
from tpt_script_generator.enums.ddl_operator import LogSQLOption
from tpt_script_generator.enums.load_operator import (
    DataEncryptionOption,
    TraceLevelOption,
    WildcardInsert,
    TASMFASTFAIL,
    CheckpointRowCount,
    DateForm,
    DropErrorTable,
    DropLogTable,
    NotifyExitIsDLL,
    NotifyLevel,
    NotifyMethod,
    PauseAcq,
    UnicodePassThrough,
)
from tpt_script_generator.script import TPTScript
from tpt_script_generator.step import Step


class TestLoadOperatorTPTScript(unittest.TestCase):
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
                LoadOperator()
                .with_user_password("password")
                .with_wildcard_insert(WildcardInsert.YES)
                .with_working_database("my_database")
                .with_account_id("acctId")
                .with_buffer_size(1024)
                .with_checkpoint_row_count(CheckpointRowCount.YES)
                .with_connect_string("connectionString")
                .with_data_encryption(DataEncryptionOption.ON)
                .with_date_form(DateForm.ANSI_DATE)
                .with_drop_error_table(DropErrorTable.NO)
                .with_drop_log_table(DropLogTable.NO)
                .with_error_limit(100)
                .with_error_table1("errorTable1")
                .with_error_table2("errorTable2")
                .with_logon_mech("logonMec")
                .with_logon_mech_data("logonMechData")
                .with_log_sql(LogSQLOption.YES)
                .with_log_table("logTable")
                .with_max_sessions(10)
                .with_min_sessions(1)
                .with_notify_exit("notifyExit")
                .with_notify_exit_is_dll(NotifyExitIsDLL.YES)
                .with_notify_level(NotifyLevel.HIGH)
                .with_notify_method(NotifyMethod.EXIT)
                .with_notify_string("notifyString")
                .with_pause_acq(PauseAcq.NO)
                .with_private_log_name("privateLogName")
                .with_query_band_sess_info("queryBandInfo")
                .with_role_name("roleName")
                .with_target_table("targetTableName")
                .with_tasm_fast_fail(TASMFASTFAIL.YES)
                .with_tenacity_hours(5)
                .with_tenacity_sleep(10)
                .with_tdp_id("tdpId")
                .with_time_zone_sess_info("timeZoneInfo")
                .with_trace_level(TraceLevelOption.CLI)
                .with_transform_group("transformGroupName")
                .with_user_name("userName")
                .with_unicode_pass_through(UnicodePassThrough.ON)
            )
            .with_step(
                Step("CLEANUP")
                .add_operation("APPLY ('DROP TABLE   ' || @TargetTable || '_WT  ; ')")
                .add_operation("('DROP TABLE   ' || @TargetTable || '_ET  ; ')")
                .add_operation("('DROP TABLE   ' || @TargetTable || '_UV  ; ')")
                .add_operation("('DROP TABLE   ' || @TargetTable || '_LOG ; ')")
                .add_operation("('DELETE FROM  ' || @TargetTable || '     ; ')")
                .add_operation("TO OPERATOR ($LoadOperator)")
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

    DEFINE OPERATOR LoadOperator
    TYPE LOAD
    ATTRIBUTES
    (
        VARCHAR UserPassword = 'password',
        VARCHAR WildcardInsert = 'Yes',
        VARCHAR WorkingDatabase = 'my_database',
        VARCHAR AccountId = 'acctId',
        INTEGER BufferSize = 1024,
        VARCHAR CheckpointRowCount = 'Yes',
        VARCHAR ConnectString = 'connectionString',
        VARCHAR DataEncryption = 'On',
        VARCHAR DateForm = 'ansiDate',
        VARCHAR DropErrorTable = 'No',
        VARCHAR DropLogTable = 'No',
        INTEGER ErrorLimit = 100,
        VARCHAR ErrorTable1 = 'errorTable1',
        VARCHAR ErrorTable2 = 'errorTable2',
        VARCHAR LogonMech = 'logonMec',
        VARCHAR LogonMechData = 'logonMechData',
        VARCHAR LogSQL = 'Yes',
        VARCHAR LogTable = 'logTable',
        INTEGER MaxSessions = 10,
        INTEGER MinSessions = 1,
        VARCHAR NotifyExit = 'notifyExit',
        VARCHAR NotifyExitIsDLL = 'Yes',
        VARCHAR NotifyLevel = 'High',
        VARCHAR NotifyMethod = 'Exit',
        VARCHAR NotifyString = 'notifyString',
        VARCHAR PauseAcq = 'No',
        VARCHAR PrivateLogName = 'privateLogName',
        VARCHAR QueryBandSessInfo = 'queryBandInfo',
        VARCHAR RoleName = 'roleName',
        VARCHAR TargetTable = 'targetTableName',
        VARCHAR TASMFASTFAIL = 'Yes',
        INTEGER TenacityHours = 5,
        INTEGER TenacitySleep = 10,
        VARCHAR TdpId = 'tdpId',
        VARCHAR TimeZoneSessInfo = 'timeZoneInfo',
        VARCHAR TraceLevel = 'CLI',
        VARCHAR TransformGroup = 'transformGroupName',
        VARCHAR UserName = 'userName',
        VARCHAR UnicodePassThrough = 'On'
    );

    STEP CLEANUP
    (
        APPLY ('DROP TABLE   ' || @TargetTable || '_WT  ; ')
        ('DROP TABLE   ' || @TargetTable || '_ET  ; ')
        ('DROP TABLE   ' || @TargetTable || '_UV  ; ')
        ('DROP TABLE   ' || @TargetTable || '_LOG ; ')
        ('DELETE FROM  ' || @TargetTable || '     ; ')
        TO OPERATOR ($LoadOperator)
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
