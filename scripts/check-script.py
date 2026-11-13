#!/usr/bin/env python3
"""脚本平均检查：三段中文台词，每段 25-28 字（中文一字算1，英文一词算1），三段之间差 <=2 字。
用法: python3 check-script.py "第1段台词" "第2段台词" "第3段台词"
"""
import sys

def count(s):
    # 中文一个字算 1，英文一个词算 1，标点不计
    import re
    return len(re.findall(r'[\u4e00-\u9fff]|[A-Za-z]+|\d+', s))

def main():
    lines = sys.argv[1:4]
    if len(lines) != 3:
        print("用法: check-script.py \"段1\" \"段2\" \"段3\"")
        return
    counts = [count(l) for l in lines]
    for i, c in enumerate(counts, 1):
        print(f"第{i}段: {c} 字")
    ok = True
    for c in counts:
        if not 25 <= c <= 28:
            print(f"FAIL: {c} 字不在 25-28 字标准内")
            ok = False
    if max(counts) - min(counts) > 2:
        print(f"FAIL: 三段差 {max(counts)-min(counts)} 字，超过 2 字，不平均")
        ok = False
    print("PASS" if ok else "FAIL: 改脚本，不生成")

if __name__ == "__main__":
    main()
