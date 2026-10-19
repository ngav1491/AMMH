#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check a Vietnamese markdown translation against its Chinese source.

Pair mode:
    python3 scripts/qa_vi_translation.py <source.md> <vi.md> \\
        --kind handbook|founder-qa|founder-free|readme

Tree mode:
    python3 scripts/qa_vi_translation.py --tree

Prints PASS, or FAIL with reasons. Exits 0 on pass and 1 on fail.
"""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HANDBOOK_DIR = "程序员的副业赚钱宝典"
FOUNDER_DIR = "创业者早期的烦恼树洞"

KINDS = ("handbook", "founder-qa", "founder-free", "readme")
QA_LABELS = ("Tiêu đề:", "Bạn đọc gửi:", "Trả lời:")
# Case-insensitive substring counts must match the source (invented or dropped names fail).
FORBIDDEN = ("Zalo", "Shopee", "MoMo", "VNĐ", "VND")

NUM_RE = re.compile(r"\d+(?:[.,]\d+)*")
URL_RE = re.compile(r"""https?://[^\s<>\[\]()"'`]+""")
HEADING_RE = re.compile(r"^[ ]{0,3}(#{1,6})(?!#)(?:[ \t]+|$)")
URL_TRAILING = ".,;:!?，。、；：！？）】》」』"

YEN = "\u00a5"
DIFF_LIMIT = 20


def read_text(path):
    return path.read_text(encoding="utf-8-sig")


def han_count(text):
    return sum(1 for char in text if "\u4e00" <= char <= "\u9fff")


def extract_urls(text):
    return [match.rstrip(URL_TRAILING) for match in URL_RE.findall(text)]


def heading_counts(text):
    counts = {level: 0 for level in range(1, 7)}
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if match:
            counts[len(match.group(1))] += 1
    return counts


def table_line_count(text):
    # ch0067.md nests GFM rows under a list, so the pipe is not column 0.
    return sum(1 for line in text.splitlines() if line.lstrip().startswith("|"))


def clip(items):
    shown = items[:DIFF_LIMIT]
    extra = len(items) - len(shown)
    message = "; ".join(shown)
    if extra:
        message += "; and %d more" % extra
    return message


def number_mismatch(src_text, dst_text):
    src_nums = Counter(NUM_RE.findall(src_text))
    dst_nums = Counter(NUM_RE.findall(dst_text))
    diffs = []
    for key in sorted(set(src_nums) | set(dst_nums)):
        if src_nums[key] != dst_nums[key]:
            diffs.append(
                "%s (source %d, dest %d)" % (key, src_nums[key], dst_nums[key])
            )
    if not diffs:
        return None
    return "number multiset mismatch: %s" % clip(diffs)


def url_mismatch(src_text, dst_text):
    """Each source URL must occur the same number of times in the destination."""
    src_urls = Counter(extract_urls(src_text))
    dst_urls = Counter(extract_urls(dst_text))
    diffs = []
    for url in sorted(src_urls):
        if dst_urls[url] != src_urls[url]:
            diffs.append(
                "%s (source %d, dest %d)" % (url, src_urls[url], dst_urls[url])
            )
    if not diffs:
        return None
    return "URL count mismatch: %s" % clip(diffs)


def forbidden_mismatches(src_text, dst_text):
    """Each forbidden token must appear the same number of times in source and dest."""
    reasons = []
    src_folded = src_text.casefold()
    dst_folded = dst_text.casefold()
    for word in FORBIDDEN:
        needle = word.casefold()
        src_n = src_folded.count(needle)
        dst_n = dst_folded.count(needle)
        if src_n != dst_n:
            reasons.append(
                "forbidden string count mismatch: %s (source %d, dest %d)"
                % (word, src_n, dst_n)
            )
    return reasons


def check_pair(source, dest, kind):
    reasons = []
    if not source.is_file():
        return ["source does not exist: %s" % source]
    if not dest.is_file():
        return ["destination does not exist: %s" % dest]
    try:
        src_text = read_text(source)
        dst_text = read_text(dest)
    except UnicodeError as exc:
        return ["cannot read files as UTF-8: %s" % exc]
    if dst_text.strip() == "":
        return ["destination is empty: %s" % dest]

    hans = han_count(dst_text)
    if hans != 0:
        reasons.append("Han characters in destination: %d (expected 0)" % hans)

    url_reason = url_mismatch(src_text, dst_text)
    if url_reason:
        reasons.append(url_reason)

    num_reason = number_mismatch(src_text, dst_text)
    if num_reason:
        reasons.append(num_reason)

    src_yen = src_text.count(YEN)
    dst_yen = dst_text.count(YEN)
    if src_yen != dst_yen:
        reasons.append(
            "yen sign count mismatch: source %d, dest %d" % (src_yen, dst_yen)
        )

    src_heads = heading_counts(src_text)
    dst_heads = heading_counts(dst_text)
    for level in range(1, 7):
        if src_heads[level] != dst_heads[level]:
            reasons.append(
                "heading level %d mismatch: source %d, dest %d"
                % (level, src_heads[level], dst_heads[level])
            )

    src_tables = table_line_count(src_text)
    dst_tables = table_line_count(dst_text)
    if src_tables != dst_tables:
        reasons.append(
            "table line count mismatch: source %d, dest %d" % (src_tables, dst_tables)
        )

    if kind == "founder-qa":
        for label in QA_LABELS:
            if label not in dst_text:
                reasons.append("missing label: %s" % label)

    reasons.extend(forbidden_mismatches(src_text, dst_text))

    return reasons


def rel(path):
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def mapped_pairs():
    pairs = [(ROOT / "README.md", ROOT / "vi" / "README.md")]
    handbook = ROOT / HANDBOOK_DIR
    founder = ROOT / FOUNDER_DIR
    if handbook.is_dir():
        for src in sorted(path for path in handbook.glob("*.md") if path.is_file()):
            pairs.append((src, ROOT / "vi" / "handbook" / src.name))
    if founder.is_dir():
        for src in sorted(path for path in founder.glob("*.md") if path.is_file()):
            pairs.append((src, ROOT / "vi" / "founder" / src.name))
    return pairs


def extra_chapter_files():
    """ch*.md under vi/handbook or vi/founder whose filename has no source md."""
    extras = []
    sources = {
        ROOT / "vi" / "handbook": ROOT / HANDBOOK_DIR,
        ROOT / "vi" / "founder": ROOT / FOUNDER_DIR,
    }
    for dest_dir, src_dir in sources.items():
        names = set()
        if src_dir.is_dir():
            names = {path.name for path in src_dir.glob("*.md") if path.is_file()}
        if not dest_dir.is_dir():
            continue
        for path in sorted(dest_dir.glob("ch*.md")):
            if path.is_file() and path.name not in names:
                extras.append(path)
    return extras


def check_tree():
    reasons = []
    for _src, dest in mapped_pairs():
        if not dest.is_file():
            reasons.append("missing: %s" % rel(dest))
    for path in extra_chapter_files():
        reasons.append("extra: %s" % rel(path))
    return reasons


def emit(reasons):
    if reasons:
        print("FAIL")
        for reason in reasons:
            print("- %s" % reason)
        return 1
    print("PASS")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Check Vietnamese markdown translations against Chinese sources."
    )
    parser.add_argument("source", nargs="?")
    parser.add_argument("dest", nargs="?")
    parser.add_argument("--kind", choices=KINDS)
    parser.add_argument("--tree", action="store_true")
    args = parser.parse_args(argv)

    if args.tree:
        if args.source or args.dest or args.kind:
            return emit(["--tree does not take source, dest, or --kind"])
        return emit(check_tree())

    if not args.source or not args.dest or not args.kind:
        return emit(
            [
                "usage: qa_vi_translation.py <source.md> <vi.md> "
                "--kind handbook|founder-qa|founder-free|readme",
                "or: qa_vi_translation.py --tree",
            ]
        )
    return emit(check_pair(Path(args.source), Path(args.dest), args.kind))


if __name__ == "__main__":
    sys.exit(main())
