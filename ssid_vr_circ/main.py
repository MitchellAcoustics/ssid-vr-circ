import argparse
from ssid_vr_circ import process
from pathlib import Path

parser = argparse.ArgumentParser(description='Process circumplex data from SSID VR Circumplex Study')
parser.add_argument('circ_dir', type=str, help='Directory containing circumplex data')
parser.add_argument('--index_file', type=str, default='SSID IVR STUDY 1 EXPERIMENT INDEX.xlsx', help='Excel file containing session IDs')
parser.add_argument('--out_file', type=str, default=None, help='Output file name')
args = parser.parse_args()

circ_dir = Path(args.circ_dir)
out_file = Path(args.out_file) if args.out_file else None
index_file = Path(args.index_file) if args.index_file else None

process.save_circ_data(circ_dir, out_file, index_file)


