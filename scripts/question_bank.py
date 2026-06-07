#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
QB = ROOT / 'question-bank' / 'self-contained'

def read_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]

def cmd_stats(args):
    manifest = json.loads((QB/'manifest.json').read_text(encoding='utf-8'))
    print(manifest['name'])
    print('Version:', manifest['version'])
    print('Coding + DSA:', manifest['coding_dsa_count'])
    print('Aptitude + Reasoning:', manifest['aptitude_reasoning_count'])
    print('Total:', manifest['total_count'])

def cmd_day(args):
    if args.path == 'coding-dsa':
        path = QB/'coding-dsa'/'by-day'/f'day-{args.day:02d}.jsonl'
    else:
        path = QB/'aptitude-reasoning'/'by-day'/f'day-{args.day:02d}.jsonl'
    rows=read_jsonl(path)
    print(f'{args.path} day {args.day:02d}: {len(rows)} questions')
    for r in rows:
        print(f"- {r['id']} [{r['tier']}/{r['difficulty']}] {r['title']}")

def cmd_topic(args):
    base = QB/args.path/'by-topic'/f'{args.slug}.jsonl'
    rows=read_jsonl(base)
    print(f'{args.path} topic {args.slug}: {len(rows)} questions')
    for r in rows:
        print(f"- Day {r['day']:02d} {r['id']} [{r['tier']}] {r['title']}")

def main():
    p=argparse.ArgumentParser(description='KPOS self-contained question bank helper')
    sub=p.add_subparsers(dest='cmd', required=True)
    sp=sub.add_parser('stats'); sp.set_defaults(func=cmd_stats)
    sp=sub.add_parser('day'); sp.add_argument('--path', choices=['coding-dsa','aptitude-reasoning'], required=True); sp.add_argument('--day', type=int, required=True); sp.set_defaults(func=cmd_day)
    sp=sub.add_parser('topic'); sp.add_argument('--path', choices=['coding-dsa','aptitude-reasoning'], required=True); sp.add_argument('--slug', required=True); sp.set_defaults(func=cmd_topic)
    args=p.parse_args(); args.func(args)
if __name__=='__main__': main()
