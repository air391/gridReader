import argparse
from gridreader.format import TestB2412, DataSet
from gridreader import parse_file
from pathlib import Path
from .log import log_init, logger
log_init()
TYPES = [
    TestB2412.FEAT,
    TestB2412.WAVE,
    TestB2412.TEL,
    TestB2412.HK
]
SET = [e.name for e in DataSet]
parser = argparse.ArgumentParser(description='Read Grid Data')
parser.add_argument('file', type=str, help='Path to the file to read')
parser.add_argument('type', type=str, choices=list(map(str,TYPES)), help='Type of the file to read')
parser.add_argument('--set', type=str, choices=SET, default="ALL", help='Set of the file to read')
parser.add_argument("--output", type=str, default="./data.csv", help="Path to the output file, available formats: csv, json, parquet")
def main():
    args = parser.parse_args()
    args.type = TestB2412[args.type.split(".")[1]]
    args.set = DataSet[args.set]
    df = parse_file(args.file, args.type, args.set)
    df.info()
    ext = Path(args.output).suffix
    match ext:
        case ".csv":
            df.to_csv(args.output, index=False)
        case ".json":
            df.to_json(args.output, index=False)
        case ".parquet":
            df.to_parquet(args.output, index=False)
        case _:
            raise ValueError(f"Unsupported output format: {ext}")
    logger.info(f"Saved data to {args.output}")