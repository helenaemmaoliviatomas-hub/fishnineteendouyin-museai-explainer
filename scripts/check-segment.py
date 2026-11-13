#!/usr/bin/env python3
"""出片前检查：量一段视频的说话起止、段内停顿，给出建议剪辑点。
用法: python3 check-segment.py <video.mp4>
通过标准：说话在 9.5s 前结束；段内停顿 >1s 的要压到 0.75s；尾巴静音 >=0.5s。
"""
import subprocess, sys, math, wave, array, os

def extract_wav(video, wav):
    subprocess.run(["ffmpeg","-y","-v","error","-i",video,"-vn","-ac","1","-ar","16000",wav], check=True)

def analyze(wav, thresh=300, bin_s=0.25):
    w = wave.open(wav)
    a = array.array('h', w.readframes(w.getnframes()))
    sr = w.getframerate()
    n = int(bin_s * sr)
    bins = []
    for i in range(0, len(a), n):
        chunk = a[i:i+n]
        rms = math.sqrt(sum(x*x for x in chunk)/len(chunk)) if chunk else 0
        bins.append((i/sr, rms))
    speech = [(t, r) for t, r in bins if r >= thresh]
    if not speech:
        return None
    start, end = speech[0][0], speech[-1][0] + bin_s
    # pauses inside speech span longer than 1s
    pauses = []
    in_pause = False
    p_start = 0
    for t, r in bins:
        if start <= t <= end:
            if r < thresh and not in_pause:
                in_pause, p_start = True, t
            elif r >= thresh and in_pause:
                in_pause = False
                if t - p_start >= 1.0:
                    pauses.append((p_start, t, t - p_start))
    if in_pause and end - p_start >= 1.0:
        pauses.append((p_start, end, end - p_start))
    return {"start": start, "end": end, "pauses": pauses, "bins": bins}

def main():
    video = sys.argv[1]
    wav = "/tmp/check-seg.wav"
    extract_wav(video, wav)
    r = analyze(wav)
    if r is None:
        print("FAIL: 没有检测到说话"); return
    print(f"说话: {r['start']:.2f}s - {r['end']:.2f}s")
    for p0, p1, d in r["pauses"]:
        print(f"停顿: {p0:.2f}s - {p1:.2f}s, 长 {d:.2f}s -> 建议压到 0.75s")
    ok = True
    if r["end"] > 9.5:
        print(f"FAIL: 说话 {r['end']:.2f}s 才结束，超过 9.5s，脚本太长，重做这一段"); ok = False
    else:
        print(f"建议剪到: 说话结束 +0.5s = {r['end']+0.5:.2f}s")
    print("PASS" if ok and not r["pauses"] else ("PASS(需压停顿)" if ok else "FAIL"))

if __name__ == "__main__":
    main()
