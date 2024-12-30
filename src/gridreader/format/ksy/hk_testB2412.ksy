meta:
  id: frameseq
  endian: be

seq:
  - id: frames
    type: frame_and_unknown
    repeat: eos
types:
  frame_and_unknown:
    seq:
      - id: frame
        type: frame
      - id: unknown
        type: unknown
  unknown:
    seq:
      - id: unknown
        type: u1
        repeat: expr
        repeat-expr: 78
  frame:
    seq:
      - id: header
        type: u4
        valid:
          eq: 0x1a2b3c4d
      - id: utc_time
        type: u4
      - id: cpu_temperature
        type: u2
      - id: daq_temperature_i2c1_0x49
        type: u2
      - id: storage_valid
        type: u2
      - id: voltage_i2c1_0x40
        type: s2
      - id: current_i2c1_0x40
        type: s2
      - id: voltage_i2c1_0x41
        type: s2
      - id: current_i2c1_0x41
        type: s2
      - id: voltage_i2c1_0x42
        type: s2
      - id: current_i2c1_0x42
        type: s2
      - id: voltage_i2c1_0x4d
        type: s2
      - id: current_i2c1_0x4d
        type: s2
      - id: voltage_i2c2_0x40
        type: s2
      - id: current_i2c2_0x40
        type: s2
      - id: voltage_i2c2_0x41
        type: s2
      - id: current_i2c2_0x41
        type: s2
      - id: voltage_i2c2_0x42
        type: s2
      - id: current_i2c2_0x42
        type: s2
      - id: voltage_i2c2_0x43
        type: s2
      - id: current_i2c2_0x43
        type: s2
      - id: voltage_i2c2_0x44
        type: s2
      - id: current_i2c2_0x44
        type: s2
      - id: voltage_i2c2_0x45
        type: s2
      - id: current_i2c2_0x45
        type: s2
      - id: voltage_i2c2_0x46
        type: s2
      - id: current_i2c2_0x46
        type: s2
      - id: voltage_i2c2_0x47
        type: s2
      - id: current_i2c2_0x47
        type: s2
      - id: voltage_i2c1_0x43
        type: s2
      - id: current_i2c1_0x43
        type: s2
      - id: voltage_i2c1_0x44
        type: s2
      - id: current_i2c1_0x44
        type: s2
      - id: voltage_i2c1_0x45
        type: s2
      - id: current_i2c1_0x45
        type: s2
      - id: voltage_i2c1_0x47
        type: s2
      - id: current_i2c1_0x47
        type: s2
      - id: voltage_i2c1_0x48
        type: s2
      - id: current_i2c1_0x48
        type: s2
      - id: voltage_sipm_ch0
        type: u2
      - id: current_sipm_ch0
        type: u2
      - id: temperature_sipm_ch0
        type: u2
      - id: voltage_sipm_ch1
        type: u2
      - id: current_sipm_ch1
        type: u2
      - id: temperature_sipm_ch1
        type: u2
      - id: voltage_sipm_ch2
        type: u2
      - id: current_sipm_ch2
        type: u2
      - id: temperature_sipm_ch2
        type: u2
      - id: voltage_sipm_ch3
        type: u2
      - id: current_sipm_ch3
        type: u2
      - id: temperature_sipm_ch3
        type: u2
      - id: saa_judge_method
        type: u1
      - id: crc16
        type: u2
    instances:
      body_data:
        pos: 0
        type: u1
        repeat: expr
        repeat-expr: 107