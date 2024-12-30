# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Frameseq(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.frames = []
        i = 0
        while not self._io.is_eof():
            self.frames.append(Frameseq.Frame(self._io, self, self._root))
            i += 1


    class Frame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.header = self._io.read_u4be()
            if not self.header == 1196575044:
                raise kaitaistruct.ValidationNotEqualError(1196575044, self.header, self._io, u"/types/frame/seq/0")
            self.telemetry_count = self._io.read_u1()
            self.cmd_count = self._io.read_u1()
            self.latest_received_cmd = self._io.read_u1()
            self.latest_received_cmd_progress = self._io.read_u1()
            self.latest_complete_cmd = self._io.read_u1()
            self.latest_complete_cmd_arg = self._io.read_u4be()
            self.latest_complete_cmd_exit = self._io.read_u1()
            self.utc_time = self._io.read_u4be()
            self.ecu_cpu_tempratrue = self._io.read_s1()
            self.daq_temperature_i2c1_0x49 = self._io.read_s1()
            self.system_power = self._io.read_u2be()
            self.system_input_voltage = self._io.read_u2be()
            self.file_upload_progress = self._io.read_u1()
            self.file_upload_check = self._io.read_u1()
            self.normal_or_backup = self._io.read_u1()
            self.storage_valid = self._io.read_u2be()
            self.pl_version = self._io.read_u1()
            self.app_version = self._io.read_u1()
            self.log_index = self._io.read_u1()
            self.sci_data_index = self._io.read_u1()
            self.sample_mode = self._io.read_u1()
            self.data_transfer_package_count = self._io.read_u1()
            self.saa_status = self._io.read_u1()
            self.entered_saa_count = self._io.read_u1()
            self.sipm_voltage_ch0 = self._io.read_u2be()
            self.sipm_current_ch0 = self._io.read_u2be()
            self.sipm_temprature_ch0 = self._io.read_u2be()
            self.sipm_voltage_ch1 = self._io.read_u2be()
            self.sipm_current_ch1 = self._io.read_u2be()
            self.sipm_temprature_ch1 = self._io.read_u2be()
            self.sipm_voltage_ch2 = self._io.read_u2be()
            self.sipm_current_ch2 = self._io.read_u2be()
            self.sipm_temprature_ch2 = self._io.read_u2be()
            self.sipm_voltage_ch3 = self._io.read_u2be()
            self.sipm_current_ch3 = self._io.read_u2be()
            self.sipm_temprature_ch3 = self._io.read_u2be()
            self.count_rate0 = self._io.read_u2be()
            self.count_rate1 = self._io.read_u2be()
            self.count_rate2 = self._io.read_u2be()
            self.count_rate3 = self._io.read_u2be()
            self.sipm_hot_flag = self._io.read_u1()
            self.heat_protect_threshold = self._io.read_u1()
            self.sum = self._io.read_u2be()

        @property
        def body_data(self):
            if hasattr(self, '_m_body_data'):
                return self._m_body_data

            _pos = self._io.pos()
            self._io.seek(0)
            self._m_body_data = []
            for i in range(71):
                self._m_body_data.append(self._io.read_u1())

            self._io.seek(_pos)
            return getattr(self, '_m_body_data', None)



