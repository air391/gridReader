from frameseq import Frame, Frameseq
import pandas as pd

def check_frame(frame: Frame) -> bool:
    return frame.sum == sum(frame.body_data)


def parse_frame(bytes) -> Frame | None:
    frame = Frame.from_bytes(bytes)
    return frame if check_frame(frame) else None


def parse_frameSeq(bytes) -> list[Frame]:
    frames = Frameseq.from_bytes(bytes)
    return [f for f in frames.frames if check_frame(f)]


def frame_to_dict(data):
    d = {}
    for k, v in data.__dict__.items():
        if not k.startswith("_"):
            d[k] = v
    for ch in range(4):
        # convert temp to ℃
        d[f"sipm_temprature_ch{ch}"] = d[f"sipm_temprature_ch{ch}"] / 100 - 273.15
    return d


def parse(bytes):
    return frame_to_dict(parse_frame(bytes))

def parse_to_dict(content:bytes):
    frames = parse_frameSeq(content)
    return (frame_to_dict(frame) for frame in frames)

def parse_file(content:bytes):
    frames = parse_frameSeq(content)
    df = pd.DataFrame()
    for frame in frames:
        parsed_data = frame_to_dict(frame)
        df = pd.concat([df, pd.DataFrame([parsed_data])], ignore_index=True)
    return df

if __name__ == "__main__":
    data = b'GRID\x00\x0bE\x00E\x00\x00\x00\x00\x00"4\x96\x9d*\x1e\x00O\x04\xaa\x00\x00\x02j\xc9\x06\x01\x1f\x00\x02\x9a\x00\x00o_\x00\x01t\xedo_\x00\x01t\xe7o_\x00\x01t\x96o_\x00\x01t\xbb\x00\x00\x00\x00\x00\x00\x00\x00\x00D\x0e\xf5'
    frame = parse_frame(data)
    d = frame_to_dict(frame)
    for i, (k, v) in enumerate(d.items()):
        print(i, k, v)
    frameSeq = parse_frameSeq(data + data)
    d2 = frame_to_dict(frameSeq[-1])
    assert d == d2
