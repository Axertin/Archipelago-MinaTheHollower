import csv
from pathlib import Path


def convert_locations(csv_path: str, output_path: str = "locations_output.txt") -> None:
    lines = []
    current_region = ""

    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)

        for row in reader:
            # Skip empty rows
            if not row:
                continue

            # Pad short rows
            while len(row) < 4:
                row.append("")

            region, name, requirements, id_str = [x.strip() for x in row[:4]]

            # Blank A column means "same region as above"
            if region:
                current_region = region
            region = current_region

            # Skip rows without a location name
            if not name:
                continue

            # Convert ID
            id_value = None
            if id_str:
                # Handle things like "174(Started with mace)"
                digits = "".join(c for c in id_str if c.isdigit())
                if digits:
                    id_value = int(digits)

            # Build output line
            if id_value is not None:
                line = f'"{name}" : LocationData({id_value}, "{region}")'
            else:
                line = f'"{name}" : LocationData(None, "{region}")'

            # Add requirements as comment
            if requirements:
                line += f", #needs {requirements.lower()}"

            line += ","
            lines.append(line)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Wrote {len(lines)} locations to {output_path}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python convert_locations.py locations.csv")
    else:
        convert_locations(sys.argv[1])