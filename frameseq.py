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
            if not self.header == 774779903:
                raise kaitaistruct.ValidationNotEqualError(774779903, self.header, self._io, u"/types/frame/seq/0")
            self.utc = self._io.read_u4be()
            self.pps_for_utc = self._io.read_u4be()
            self.timestamp_for_pps_for_utc = self._io.read_u8be()
            self.channel_n = self._io.read_u2be()
            self.event_number = self._io.read_u4be()
            self.sample_length = self._io.read_u2be()
            self.waveform_data = []
            for i in range(512):
                self.waveform_data.append(self._io.read_u1())

            self.timestamp = self._io.read_u8be()
            self.data_max = self._io.read_u2be()
            self.data_base = self._io.read_u2be()
            self.buff_full_count = self._io.read_u2be()
            self.crc = self._io.read_u2be()
            self.tail = self._io.read_u4be()
            if not self.tail == 586088243:
                raise kaitaistruct.ValidationNotEqualError(586088243, self.tail, self._io, u"/types/frame/seq/13")

        @property
        def body_data(self):
            if hasattr(self, '_m_body_data'):
                return self._m_body_data

            _pos = self._io.pos()
            self._io.seek(0)
            self._m_body_data = []
            for i in range(554):
                self._m_body_data.append(self._io.read_u1())

            self._io.seek(_pos)
            return getattr(self, '_m_body_data', None)



