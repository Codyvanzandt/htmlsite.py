import argparse
import shutil
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# ---------------------------------------------------------------------------
# Command line interface
# ---------------------------------------------------------------------------

parser = argparse.ArgumentParser(description="Build a static site.")
parser.add_argument(
    "--source_dir",
    default="src",
    help="Source directory for index.html files (default: src)",
)
parser.add_argument(
    "--output_dir",
    default="site",
    help="Directory where the built site is written (default: site)",
)
args = parser.parse_args()

SOURCE_DIR = Path(args.source_dir)
OUTPUT_DIR = Path(args.output_dir)

# ---------------------------------------------------------------------------
# Validate input and output directories
# ---------------------------------------------------------------------------

if not SOURCE_DIR.exists():
    raise SystemExit(f"Error: source directory '{SOURCE_DIR.resolve()}' does not exist.")

if SOURCE_DIR.resolve() == OUTPUT_DIR.resolve():
    raise SystemExit("Error: source directory and output directory must be different directories.")

# ---------------------------------------------------------------------------
# Copy static assets from source directory to output directory
# ---------------------------------------------------------------------------

if OUTPUT_DIR.exists():
    shutil.rmtree(OUTPUT_DIR)

shutil.copytree(SOURCE_DIR, OUTPUT_DIR, ignore=shutil.ignore_patterns("_*"))

# ---------------------------------------------------------------------------
# Set up Jinja2 environment
# ---------------------------------------------------------------------------

env = Environment(
    loader=FileSystemLoader(str(SOURCE_DIR)),
    autoescape=False
)

# ---------------------------------------------------------------------------
# Render templates
# ---------------------------------------------------------------------------

for page in SOURCE_DIR.rglob("index.html"):

    relative = page.relative_to(SOURCE_DIR)
    if any(part.startswith("_") for part in relative.parts):
        continue

    dest = OUTPUT_DIR / relative
    dest.write_text(env.get_template(str(relative)).render(), encoding="utf-8")