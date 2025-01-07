from gridreader import parse_file, parse_frame
from gridreader.format import TestB2412, DataSet, get_frames_with_seq, get_header_length
import pytest

def file_read(file_name):
    with open(file_name, "rb") as f:
        data = f.read()
    return data

@pytest.fixture
def feat_frames():
    return "tests/data/testB2412/feat_frames.dat"


@pytest.fixture
def feat_frameseq():
    return file_read("tests/data/testB2412/feat_frameseq.dat")


def test_feat_frame(feat_frames):
    df = parse_file(feat_frames, TestB2412.FEAT, DataSet.ALL)
    assert df.shape == (3, 11)


def test_feat_frameseq(feat_frameseq):
    frames = get_frames_with_seq(feat_frameseq, TestB2412.FEAT)
    assert len(frames) == 2


@pytest.fixture
def wave_frames():
    return "tests/data/testB2412/wave_frames.dat"


@pytest.fixture
def wave_frameseq():
    return file_read("tests/data/testB2412/wave_frameseq.dat")


def test_testB2412_wave(wave_frames):
    df = parse_file(wave_frames, TestB2412.WAVE, DataSet.ALL)
    assert df.shape == (3, 14)


def test_wave_frameseq(wave_frameseq):
    frames = get_frames_with_seq(wave_frameseq, TestB2412.WAVE)
    assert len(frames) == 2


@pytest.fixture
def tel_frames():
    return "tests/data/testB2412/tel_frames.dat"


@pytest.fixture
def tel_frameseq():
    return file_read("tests/data/testB2412/tel_frameseq.dat")


def test_tel_frame(tel_frames):
    df = parse_file(tel_frames, TestB2412.TEL, DataSet.ALL)
    assert df.shape == (2, 48)


def test_tel_frameseq(tel_frameseq):
    frames = get_frames_with_seq(tel_frameseq, TestB2412.TEL)
    assert len(frames) == 2


@pytest.fixture
def hk_frames():
    return "tests/data/testB2412/hk_frames.dat"


@pytest.fixture
def hk_frameseq():
    return file_read("tests/data/testB2412/hk_frameseq.dat")


def test_hk(hk_frames):
    df = parse_file(hk_frames, TestB2412.HK, DataSet.ALL)
    assert df.shape == (11, 55)

def test_hk_frameseq(hk_frameseq):
    frames = get_frames_with_seq(hk_frameseq, TestB2412.HK)
    assert len(frames) == 2

def test_bytes(feat_frameseq):
    _, length = get_header_length(TestB2412.FEAT)
    d = parse_frame(feat_frameseq[:length], TestB2412.FEAT, DataSet.ALL)
    assert d['pkg_event_num'] == len(d['events'])

def test_bytes_error(feat_frameseq):
    _, length = get_header_length(TestB2412.FEAT)
    with pytest.raises(EOFError):
        parse_frame(feat_frameseq[:length-1], TestB2412.FEAT, DataSet.ALL)