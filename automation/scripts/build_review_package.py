from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
package = OUT / f"LEGALDECODE-REVIEW-{today}.md"

content = f"""# LegalDecode — Content Review Package

- Package date (UTC): {today}
- Status: **DRAFT — NOT READY FOR PUBLICATION**
- Publishing approval: **NOT GRANTED**
- Package ID: LEGALDECODE-{today}

## 1. Case / Legal Update
- Court:
- Case title:
- Case number:
- Date of order/judgment:
- Official source URL:

## 2. Verification Checklist
- [ ] Official judgment/order obtained
- [ ] Case title and citation checked against primary source
- [ ] Relevant paragraphs/page numbers recorded
- [ ] Statutory provisions checked in current official text
- [ ] Subsequent history / appeal or stay checked
- [ ] No unsupported proposition or invented citation

## 3. Editorial Package
- Hindi title:
- English title:
- Key legal issue:
- Verified facts:
- Court's reasoning:
- Final holding:
- Practical significance:

## 4. Production
- [ ] Hindi script
- [ ] English captions
- [ ] Reel/Short slides
- [ ] Long-form outline (if applicable)
- [ ] Voiceover and subtitles
- [ ] Video render checked

## 5. Approval Gate
- Review status: **READY FOR REVIEW only after all checks are complete**
- User approval for this exact package: **PENDING**
- Exact approval phrase required: **DONE**
- Publishing action: **BLOCKED until explicit DONE**
"""

package.write_text(content, encoding="utf-8")

# Fail closed if the approval gate is missing or accidentally permissive.
text = package.read_text(encoding="utf-8")
required = [
    "Official source URL:",
    "Official judgment/order obtained",
    "User approval for this exact package: **PENDING**",
    "Publishing action: **BLOCKED until explicit DONE**",
]
missing = [item for item in required if item not in text]
if missing:
    raise SystemExit(f"Review package safety check failed: {missing}")

print(f"Created non-publishing review template: {package.relative_to(ROOT)}")
