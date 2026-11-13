#!/usr/bin/env python3
"""Inventory a local BIDS MRI dataset without loading participant imaging data.

This is a preliminary repository utility. It checks basic BIDS files and
summarizes participant and imaging-file counts; it does not perform imaging
quality control, preprocessing, event alignment, or statistical analysis.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


def read_json(path: Path) -> dict[str, Any] | None:
    """Read a JSON file, returning None when it is unavailable or invalid."""
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"_read_error": str(exc)}


def list_subjects(bids_dir: Path) -> list[str]:
    """Return BIDS subject labels for directories named sub-*."""
    return sorted(path.name for path in bids_dir.glob("sub-*") if path.is_dir())


def count_files(paths: list[Path]) -> Counter[str]:
    """Count files by extension for the provided file paths."""
    counts: Counter[str] = Counter()
    for path in paths:
        name = path.name.lower()
        if name.endswith(".nii.gz"):
            counts[".nii.gz"] += 1
        else:
            counts[path.suffix.lower() or "[no extension]"] += 1
    return counts


def build_report(bids_dir: Path) -> dict[str, Any]:
    """Build a metadata/file inventory for a BIDS dataset directory."""
    if not bids_dir.exists() or not bids_dir.is_dir():
        raise NotADirectoryError(f"BIDS directory does not exist: {bids_dir}")

    dataset_description = read_json(bids_dir / "dataset_description.json")
    participants_file = bids_dir / "participants.tsv"
    subjects = list_subjects(bids_dir)
    all_files = [path for path in bids_dir.rglob("*") if path.is_file()]

    func_files = [
        path for path in all_files
        if "/func/" in path.as_posix()
        and path.name.lower().endswith((".nii", ".nii.gz"))
    ]
    anat_files = [
        path for path in all_files
        if "/anat/" in path.as_posix()
        and path.name.lower().endswith((".nii", ".nii.gz"))
    ]
    sidecars = [path for path in all_files if path.suffix.lower() == ".json"]

    return {
        "bids_directory": str(bids_dir.resolve()),
        "dataset_description": dataset_description,
        "has_dataset_description": (bids_dir / "dataset_description.json").is_file(),
        "has_participants_tsv": participants_file.is_file(),
        "subject_directory_count": len(subjects),
        "subject_labels": subjects,
        "total_file_count": len(all_files),
        "file_counts_by_extension": dict(count_files(all_files)),
        "functional_nifti_count": len(func_files),
        "anatomical_nifti_count": len(anat_files),
        "json_sidecar_count": len(sidecars),
        "derivatives_directory_present": (bids_dir / "derivatives").is_dir(),
        "note": (
            "Inventory only. Counts do not establish data usability, quality, "
            "or inclusion in any statistical analysis."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Inventory the structure of a local BIDS MRI dataset."
    )
    parser.add_argument(
        "--bids-dir",
        required=True,
        type=Path,
        help="Path to the root of the downloaded BIDS dataset.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional path for a JSON report. If omitted, print to stdout.",
    )
    args = parser.parse_args()

    report = build_report(args.bids_dir.expanduser())
    rendered = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
        print(f"Wrote inventory report to: {args.output}")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())