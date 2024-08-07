import unittest
from tpt_script_generator.script import TPTScript
from tpt_script_generator.update_operator import UpdateOperator
from tpt_script_generator.step import Step
from tpt_script_generator.enums import (
    LogonMech, LogSQL, NotifyMethod, NotifyLevel,
    TraceLevel, TransformGroup, UnicodePassThrough,
    ReplicationOverride, RoleName
)

class TestUpdateTPTScript(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        
    def test_script_generation_for_update_operator(self):
        builder = (
            TPTScript("LoadToTeradata")
            .with_description("Load data into Teradata using Update operator")
            .with_var("UpdateTdpId", "@var_tdpid")
            .with_var("UpdateUserName", "@var_username")
            .with_var("UpdateUserPassword", "@var_password")
            .with_var("TargetTable", "@var_target_table")
            .with_schema(
                "TargetSchema",
                {
                    "COLUMN1": "VARCHAR(100)",
                    "COLUMN2": "INTEGER",
                    "COLUMN3": "DATE",
                },
            )
            .with_operator(
                UpdateOperator()
                .with_schema("TargetSchema")
                .with_account_id("acctId")
                .with_amp_check("YES")
                .with_buffer_size(1024)
                .with_checkpoint_row_count("1000")
                .with_connect_string("connectionString")
                .with_data_encryption("ON")
                .with_date_form("ANSIDate")
                .with_delete_lob_data_files("YES")
                .with_delete_task("YES")
                .with_drop_error_table("YES")
                .with_drop_log_table("YES")
                .with_drop_work_table("YES")
                .with_error_limit(1)
                .with_error_table1("ErrorTable1")
                .with_error_table2("ErrorTable2")
                .with_logon_mech(LogonMech.EXTERNAL)
                .with_logon_mech_data("logonMechData")
                .with_log_sql(LogSQL.DETAIL)
                .with_log_table("LogTable")
                .with_max_sessions(5)
                .with_min_sessions(1)
                .with_notify_exit("NotifyExit")
                .with_notify_exit_is_dll("YES")
                .with_notify_level(NotifyLevel.ALL)
                .with_notify_method(NotifyMethod.MSG)
                .with_notify_string("NotifyString")
                .with_pack(10)
                .with_pause_acq("YES")
                .with_private_log_name("PrivateLogName")
                .with_query_band_sess_info("QueryBandSessInfo")
                .with_replication_override(ReplicationOverride.ON)
                .with_role_name(RoleName.ADMIN)
                .with_target_table("TargetTable")
                .with_tasmfastfail("YES")
                .with_tenacity_hours(1)
                .with_tenacity_sleep(10)
                .with_tdp_id("TdpId")
                .with_time_zone_sess_info("TimeZoneSessInfo")
                .with_trace_level([TraceLevel.CLI, TraceLevel.PX])
                .with_transform_group([TransformGroup.JSON, TransformGroup.ST_GEOMETRY])
                .with_treat_dbs_restart_as_fatal("YES")
                .with_unicode_pass_through(UnicodePassThrough.ON)
                .with_user_name("UserName")
                .with_user_password("UserPassword")
                .with_work_table("WorkTable")
                .with_working_database("WorkingDatabase")
            )
            .with_step(
                Step("Load_Data")
                .add_operation("APPLY ('INSERT INTO ' || @TargetTable || ' VALUES (?, ?, ?);')")
                .add_operation("TO OPERATOR (UpdateOperator)")
            )
            .build()
        )

        expected_script = """DEFINE JOB LoadToTeradata
DESCRIPTION 'Load data into Teradata using Update operator'
(
    SET UpdateTdpId = @var_tdpid
    SET UpdateUserName = @var_username
    SET UpdateUserPassword = @var_password
    SET TargetTable = @var_target_table
    DEFINE SCHEMA TargetSchema
    (
        "COLUMN1" VARCHAR(100),
        "COLUMN2" INTEGER,
        "COLUMN3" DATE
    );

    DEFINE OPERATOR UpdateOperator
    TYPE Update
    SCHEMA TargetSchema
    ATTRIBUTES
    (
        VARCHAR AccountId = 'acctId',
        VARCHAR AmpCheck = 'YES',
        INTEGER BufferSize = 1024,
        VARCHAR CheckpointRowCount = '1000',
        VARCHAR ConnectString = 'connectionString',
        VARCHAR DataEncryption = 'ON',
        VARCHAR DateForm = 'ANSIDate',
        VARCHAR DeleteLobDataFiles = 'YES',
        VARCHAR DeleteTask = 'YES',
        VARCHAR DropErrorTable = 'YES',
        VARCHAR DropLogTable = 'YES',
        VARCHAR DropWorkTable = 'YES',
        INTEGER ErrorLimit = 1,
        VARCHAR ErrorTable1 = 'ErrorTable1',
        VARCHAR ErrorTable2 = 'ErrorTable2',
        VARCHAR LogonMech = 'EXTERNAL',
        VARCHAR LogonMechData = 'logonMechData',
        VARCHAR LogSQL = 'DETAIL',
        VARCHAR LogTable = 'LogTable',
        INTEGER MaxSessions = 5,
        INTEGER MinSessions = 1,
        VARCHAR NotifyExit = 'NotifyExit',
        VARCHAR NotifyExitIsDLL = 'YES',
        VARCHAR NotifyLevel = 'All',
        VARCHAR NotifyMethod = 'Msg',
        VARCHAR NotifyString = 'NotifyString',
        INTEGER Pack = 10,
        VARCHAR PauseAcq = 'YES',
        VARCHAR PrivateLogName = 'PrivateLogName',
        VARCHAR QueryBandSessInfo = 'QueryBandSessInfo',
        VARCHAR ReplicationOverride = 'On',
        VARCHAR RoleName = 'Admin',
        VARCHAR TargetTable = 'TargetTable',
        VARCHAR TASMFASTFAIL = 'YES',
        INTEGER TenacityHours = 1,
        INTEGER TenacitySleep = 10,
        VARCHAR TdpId = 'TdpId',
        VARCHAR TimeZoneSessInfo = 'TimeZoneSessInfo',
        VARCHAR_ARRAY TraceLevel = ['CLI', 'PX'],
        VARCHAR_ARRAY TransformGroup = ['JSON CHARACTER SET LATIN TD_JSON_VARCHAR', 'ST_GEOMETRY TD_GEO_VARCHAR'],
        VARCHAR TreatDBSRestartAsFatal = 'YES',
        VARCHAR UnicodePassThrough = 'On',
        VARCHAR UserName = 'UserName',
        VARCHAR UserPassword = 'UserPassword',
        VARCHAR WorkTable = 'WorkTable',
        VARCHAR WorkingDatabase = 'WorkingDatabase'
    );

    STEP Load_Data
    (
        APPLY ('INSERT INTO ' || @TargetTable || ' VALUES (?, ?, ?);')
        TO OPERATOR (UpdateOperator)
    );

);
"""
        self.assertEqual(builder, expected_script)

if __name__ == '__main__':
    unittest.main()
