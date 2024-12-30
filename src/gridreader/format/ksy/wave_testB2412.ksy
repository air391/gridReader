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
          eq: 0x2e2e33ff
      - id: utc
        type: u4
      - id: pps_for_utc
        type: u4
      - id: timestamp_for_pps_for_utc
        type: u8
      - id: channel_n
        type: u2
      - id: event_number
        type: u4
      - id: sample_length
        type: u2
      - id: waveform_data
        type: u1
        repeat: expr
        repeat-expr: 512
      - id: timestamp
        type: u8
      - id: data_max
        type: u2
      - id: data_base
        type: u2
      - id: buff_full_count
        type: u2
      - id: crc
        type: u2
      - id: tail
        type: u4
        valid:
          eq: 0x22eeff33
    instances:
      body_data:
        pos: 0
        type: u1
        repeat: expr
        repeat-expr: 554