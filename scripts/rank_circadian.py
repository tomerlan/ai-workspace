import re, json, pathlib, collections

MD = pathlib.Path("input/kruse_blog_glix/markdown")

# weighted circadian-core vocabulary
W = {
    # core clock machinery (high weight - specific)
    r"suprachiasmatic|\bscn\b": 6,
    r"melanopsin": 6,
    r"\bclock gene|bmal1|\bper[12]\b|cry ?[12]|clock/bmal|circadian gene": 6,
    r"zeitgeber|entrain\w*": 5,
    r"chronobiolog\w*|chronotype|chronodisruption|circadian mismatch": 5,
    r"eye clock|central clock|peripheral clock|master clock": 5,
    r"pineal|melatonin": 3,
    r"\bipRGC|retinohypothalamic|rhythm(?:ic)? gene expression": 5,
    r"circadian": 3,
    r"cortisol awakening|diurnal|nocturnal|photoperiod|seasonal": 2,
    r"light at night|\bALAN\b|blue light at night|night shift|shift work": 3,
    r"sleep[- ]wake|dim light melatonin|DLMO": 3,
    r"leptin.{0,40}circadian|circadian.{0,40}leptin": 4,
    r"AM sunlight|sunrise|solar noon|UVA rise|first light": 3,
    r"time\b(?!\s*(?:to|for|of day-?to))": 0,   # too generic, skip
}
COMP = [(re.compile(p, re.I), w) for p, w in W.items() if w]

rows = []
for f in sorted(MD.glob("*.md")):
    t = f.read_text(encoding="utf-8", errors="ignore")
    m = re.search(r"^date:\s*(\S+)", t, re.M)
    date = m.group(1) if m else "?"
    title_m = re.search(r"^title:\s*(.+)$", t, re.M)
    title = title_m.group(1).strip() if title_m else f.stem
    n = len(t)
    score = 0
    hits = {}
    for rx, w in COMP:
        c = len(rx.findall(t))
        if c:
            hits[rx.pattern[:28]] = c
            score += c * w
    # density-normalized companion score (per 10k chars) to surface short, dense posts
    dens = score / max(n, 1) * 10000
    rows.append(dict(file=f.name, title=title, date=date, chars=n,
                     score=score, density=round(dens, 1), hits=hits))

rows.sort(key=lambda r: -r["score"])
json.dump(rows, open("outputs/circadian/raw/circadian_rank.json", "w"), indent=1)

print(f"{'score':>6} {'dens':>6} {'kB':>5}  {'date':10}  title")
for r in rows[:45]:
    print(f"{r['score']:>6} {r['density']:>6} {r['chars']//1000:>5}  {r['date']:10}  {r['title'][:62]}")
tot = sum(1 for r in rows if r['score'] > 0)
print(f"\nposts with any hit: {tot}/737   |  score>=100: {sum(1 for r in rows if r['score']>=100)}   >=200: {sum(1 for r in rows if r['score']>=200)}")
