meta:
  id: frameseq
  endian: be
seq:
  - id: frames
    type: frame
    repeat: eos
types:
  frame:
    seq:
      - id: header
        type: u4
        valid:
          eq: 0x47524944
      - id: telemetry_count
        type: u1
      - id: cmd_count
        type: u1
      - id: latest_received_cmd
        type: u1
      - id: latest_received_cmd_progress
        type: u1
      - id: latest_complete_cmd
        type: u1
      - id: latest_complete_cmd_arg
        type: u4
      - id: latest_complete_cmd_exit
        type: u1
      - id: utc_time
        type: u4
      - id: ecu_cpu_tempratrue
        type: s1
      - id: daq_temperature_i2c1_0x49
        type: s1
      - id: system_power
        type: u2
      - id: system_input_voltage
        type: u2
      - id: file_upload_progress
        type: u1
      - id: file_upload_check
        type: u1
      - id: normal_or_backup
        type: u1
      - id: storage_valid
        type: u2
      - id: pl_version
        type: u1
      - id: app_version
        type: u1
      - id: log_index
        type: u1
      - id: sci_data_index
        type: u1
      - id: sample_mode
        type: u1
      - id: data_transfer_package_count
        type: u1
      - id: saa_status
        type: u1
      - id: entered_saa_count
        type: u1
      - id: sipm_voltage_ch0
        type: u2
      - id: sipm_current_ch0
        type: u2
      - id: sipm_temperature_ch0
        type: u2
      - id: sipm_voltage_ch1
        type: u2
      - id: sipm_current_ch1
        type: u2
      - id: sipm_temperature_ch1
        type: u2
      - id: sipm_voltage_ch2
        type: u2
      - id: sipm_current_ch2
        type: u2
      - id: sipm_temperature_ch2
        type: u2
      - id: sipm_voltage_ch3
        type: u2
      - id: sipm_current_ch3
        type: u2
      - id: sipm_temperature_ch3
        type: u2
      - id: count_rate0
        type: u2
      - id: count_rate1
        type: u2
      - id: count_rate2
        type: u2
      - id: count_rate3
        type: u2
      - id: sipm_hot_flag
        type: u1
      - id: heat_protect_threshold
        type: u1
      - id: sum
        type: u2
    instances:
      body_data:
        pos: 0
        type: u1
        repeat: expr
        repeat-expr: 71