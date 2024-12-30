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
            self.frames.append(Frameseq.FrameAndUnknown(self._io, self, self._root))
            i += 1


    class FrameAndUnknown(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.frame = Frameseq.Frame(self._io, self, self._root)
            self.unknown = Frameseq.Unknown(self._io, self, self._root)


    class Unknown(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unknown = []
            for i in range(78):
                self.unknown.append(self._io.read_u1())



    class Frame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.header = self._io.read_u4be()
            if not self.header == 439041101:
                raise kaitaistruct.ValidationNotEqualError(439041101, self.header, self._io, u"/types/frame/seq/0")
            self.utc_time = self._io.read_u4be()
            self.cpu_temperature = self._io.read_u2be()
            self.daq_temperature_i2c1_0x49 = self._io.read_u2be()
            self.storage_valid = self._io.read_u2be()
            self.voltage_i2c1_0x40 = self._io.read_s2be()
            self.current_i2c1_0x40 = self._io.read_s2be()
            self.voltage_i2c1_0x41 = self._io.read_s2be()
            self.current_i2c1_0x41 = self._io.read_s2be()
            self.voltage_i2c1_0x42 = self._io.read_s2be()
            self.current_i2c1_0x42 = self._io.read_s2be()
            self.voltage_i2c1_0x4d = self._io.read_s2be()
            self.current_i2c1_0x4d = self._io.read_s2be()
            self.voltage_i2c2_0x40 = self._io.read_s2be()
            self.current_i2c2_0x40 = self._io.read_s2be()
            self.voltage_i2c2_0x41 = self._io.read_s2be()
            self.current_i2c2_0x41 = self._io.read_s2be()
            self.voltage_i2c2_0x42 = self._io.read_s2be()
            self.current_i2c2_0x42 = self._io.read_s2be()
            self.voltage_i2c2_0x43 = self._io.read_s2be()
            self.current_i2c2_0x43 = self._io.read_s2be()
            self.voltage_i2c2_0x44 = self._io.read_s2be()
            self.current_i2c2_0x44 = self._io.read_s2be()
            self.voltage_i2c2_0x45 = self._io.read_s2be()
            self.current_i2c2_0x45 = self._io.read_s2be()
            self.voltage_i2c2_0x46 = self._io.read_s2be()
            self.current_i2c2_0x46 = self._io.read_s2be()
            self.voltage_i2c2_0x47 = self._io.read_s2be()
            self.current_i2c2_0x47 = self._io.read_s2be()
            self.voltage_i2c1_0x43 = self._io.read_s2be()
            self.current_i2c1_0x43 = self._io.read_s2be()
            self.voltage_i2c1_0x44 = self._io.read_s2be()
            self.current_i2c1_0x44 = self._io.read_s2be()
            self.voltage_i2c1_0x45 = self._io.read_s2be()
            self.current_i2c1_0x45 = self._io.read_s2be()
            self.voltage_i2c1_0x47 = self._io.read_s2be()
            self.current_i2c1_0x47 = self._io.read_s2be()
            self.voltage_i2c1_0x48 = self._io.read_s2be()
            self.current_i2c1_0x48 = self._io.read_s2be()
            self.voltage_sipm_ch0 = self._io.read_u2be()
            self.current_sipm_ch0 = self._io.read_u2be()
            self.temperature_sipm_ch0 = self._io.read_u2be()
            self.voltage_sipm_ch1 = self._io.read_u2be()
            self.current_sipm_ch1 = self._io.read_u2be()
            self.temperature_sipm_ch1 = self._io.read_u2be()
            self.voltage_sipm_ch2 = self._io.read_u2be()
            self.current_sipm_ch2 = self._io.read_u2be()
            self.temperature_sipm_ch2 = self._io.read_u2be()
            self.voltage_sipm_ch3 = self._io.read_u2be()
            self.current_sipm_ch3 = self._io.read_u2be()
            self.temperature_sipm_ch3 = self._io.read_u2be()
            self.saa_judge_method = self._io.read_u1()
            self.crc16 = self._io.read_u2be()

        @property
        def body_data(self):
            if hasattr(self, '_m_body_data'):
                return self._m_body_data

            _pos = self._io.pos()
            self._io.seek(0)
            self._m_body_data = []
            for i in range(107):
                self._m_body_data.append(self._io.read_u1())

            self._io.seek(_pos)
            return getattr(self, '_m_body_data', None)



