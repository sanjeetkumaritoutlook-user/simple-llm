import argparse
from iss_pass_tracker import set_api_key, get_passes

parser = argparse.ArgumentParser()
parser.add_argument("--api-key", required=True)
args = parser.parse_args()

# Set the API key for iss_pass_tracker
set_api_key(args.api_key)

lat, lon = 17.385044, 78.486671
passes = get_passes(lat, lon, n=10)

if not passes:
    print("No upcoming ISS passes found.")
else:
    for p in passes:
        # local_time() returns datetime in your system timezone
        print(p.local_time().strftime("%Y-%m-%d %H:%M:%S %Z"), f"for {p.duration} seconds")
