import argparse
import process

parser = argparse.ArgumentParser(description='Process circumplex data from SSID VR Circumplex Study')
parser.add_argument('circ_dir', type=str, help='Directory containing circumplex data')
parser.add_argument('--index_file', type=str, default='SSID IVR STUDY 1 EXPERIMENT INDEX.xlsx', help='Excel file containing session IDs')
parser.add_argument('--out_file', type=str, default=None, help='Output file name')
args = parser.parse_args()

process.save_circ_data(args.circ_dir, args.out_file, args.index_file)


