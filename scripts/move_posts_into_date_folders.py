#!/usr/bin/env python3
"""Move flat Markdown posts into content/posts/YYYY/MM folders.

This script matches the year/month destination using the Markdown filename prefix:
YYYY-MM-DD-post-slug.md -> content/posts/YYYY/MM/YYYY-MM-DD-post-slug.md

By default the script performs a dry run.
Use --apply to move files on disk.
"""
from __future__ import annotations

import argparse
import shutil
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

DATE_PREFIX_PATTERN = re.compile(r"^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})-")


@dataclass(frozen=True)
class MovePlan:
    source: Path
    target: Path
    year: str
    month: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--content-dir",
        type=Path,
        default=Path("content/posts"),
        help="Directory containing Markdown files (default: content/posts)",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Move files on disk. Default is dry run.",
    )
    return parser.parse_args()


def build_move_plan(path: Path, content_dir: Path) -> MovePlan | None:
    match = DATE_PREFIX_PATTERN.match(path.name)
    if match is None:
        return None

    year = match.group("year")
    month = match.group("month")
    target = content_dir / year / month / path.name
    return MovePlan(source=path, target=target, year=year, month=month)


def collect_move_plans(content_dir: Path) -> tuple[list[MovePlan], list[Path]]:
    plans: list[MovePlan] = []
    skipped: list[Path] = []

    for path in sorted(content_dir.glob("*.md")):
        plan = build_move_plan(path, content_dir)
        if plan is None:
            skipped.append(path)
            continue
        plans.append(plan)

    return plans, skipped


def relative_to_cwd(path: Path) -> Path:
    if path.is_absolute() and path.is_relative_to(Path.cwd()):
        return path.relative_to(Path.cwd())
    return path


def print_plan_summary(plans: list[MovePlan], skipped: list[Path], apply_changes: bool) -> None:
    mode = "APPLY" if apply_changes else "DRY RUN"
    print(f"Mode: {mode}")
    print(f"Root-level Markdown files matched: {len(plans)}")
    print(f"Root-level Markdown files skipped: {len(skipped)}")

    if not plans:
        print("No matching flat Markdown files found to move.")
        return

    destination_counts = Counter((plan.year, plan.month) for plan in plans)
    print("Destination summary:")
    for (year, month), count in sorted(destination_counts.items()):
        print(f"- {year}/{month}: {count}")

    sample_count = min(len(plans), 10)
    print(f"Sample moves ({sample_count} shown):")
    for plan in plans[:sample_count]:
        print(f"- {relative_to_cwd(plan.source)} -> {relative_to_cwd(plan.target)}")
    if len(plans) > sample_count:
        print(f"- ... and {len(plans) - sample_count} more")

    if skipped:
        print("Skipped files without YYYY-MM-DD prefix:")
        for path in skipped[:10]:
            print(f"- {relative_to_cwd(path)}")
        if len(skipped) > 10:
            print(f"- ... and {len(skipped) - 10} more")


def validate_targets(plans: list[MovePlan]) -> list[MovePlan]:
    collisions: list[MovePlan] = []
    for plan in plans:
        if plan.target.exists():
            collisions.append(plan)
    return collisions


def apply_moves(plans: list[MovePlan]) -> int:
    moved = 0
    for plan in plans:
        plan.target.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(plan.source), str(plan.target))
        moved += 1
    return moved


def main() -> int:
    args = parse_args()
    content_dir = args.content_dir.resolve()

    if not content_dir.exists():
        print(f"Error: Content directory not found: {content_dir}")
        return 1

    plans, skipped = collect_move_plans(content_dir)
    print_plan_summary(plans, skipped, args.apply)

    if not plans:
        return 0

    collisions = validate_targets(plans)
    if collisions:
        print("\nRefusing to continue because target files already exist:")
        for plan in collisions[:10]:
            print(f"- {relative_to_cwd(plan.target)}")
        if len(collisions) > 10:
            print(f"- ... and {len(collisions) - 10} more")
        return 1

    if not args.apply:
        print("\nDry run only. Re-run with --apply to move files.")
        return 0

    moved = apply_moves(plans)
    remaining_flat = sorted(content_dir.glob("*.md"))

    print("")
    print(f"Moved files: {moved}")
    print(f"Remaining root-level Markdown files: {len(remaining_flat)}")
    if remaining_flat:
        for path in remaining_flat[:10]:
            print(f"- {relative_to_cwd(path)}")
        if len(remaining_flat) > 10:
            print(f"- ... and {len(remaining_flat) - 10} more")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
