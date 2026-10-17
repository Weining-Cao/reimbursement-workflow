#!/usr/bin/env python3
"""Export the maintained workflow as one text attachment, without case data."""

import argparse
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL = Path("skills/reimbursement-workflow")
# Explicit public inputs: never recursively collect a user's case directory.
SOURCES = (
    Path("prompts/start.md"),
    SKILL / "SKILL.md",
    SKILL / "references/workflow.md",
    SKILL / "references/rules.md",
    SKILL / "references/scenarios/nju-travel-materials.md",
    SKILL / "references/scenarios/nju-doctoral-conference-funding-2026.md",
    SKILL / "references/scenarios/SCENARIO_TEMPLATE.md",
    SKILL / "references/collection.md",
    SKILL / "references/finance-review.md",
    SKILL / "assets/case.md",
    SKILL / "assets/oa-draft.md",
    SKILL / "assets/expenses.csv",
    SKILL / "assets/review.md",
    SKILL / "references/replay.md",
    SKILL / "references/integrity.md",
    SKILL / "scripts/check_packet.py",
)


def export(root, destination):
    sections = [
        "差旅报销工作流 — 聊天版\n\n"
        "面向南京大学计算机国际会议申请和报销。上传本文件或粘贴全文，再说明院系、身份、"
        "行程、经费、当前阶段和已有材料；未知项可注明不清楚，无需安装软件。\n\n"
        "按适用规则、整理材料、逐条检查、最终交付推进，未通过项修正后复查。"
        "学生 OA 由本人点击提交，财务报销交经办老师办理；材料就绪不等于财务批准。\n\n"
        "本文件由下列公共源文件生成，包含说明、空白模板和可选文件校验脚本，"
        "不含真实申请人材料，也不是学校制度发布文件。\n\n"
        "给 agent：从启动提示和执行流程开始，用中文沟通。相对链接按引用源文件所在目录"
        "解析至本附件的 SOURCE 区段，不重复索取已包含的文件。模板复制到私人目录后，"
        "工作记录引用实际规则位置和版本。脚本区段是源码，不代表已安装或已经执行。"
        "仅使用本次实际可用能力，不虚称完成文件写入、浏览器、邮箱或渲染操作。\n\n"
        "来源目录\n" + "\n".join(str(path) for path in SOURCES)
    ]
    for relative in SOURCES:
        source = root / relative
        sections.append(
            f"\n=== SOURCE: {relative.as_posix()} ===\n\n"
            + source.read_text(encoding="utf-8").rstrip()
            + f"\n\n=== END SOURCE: {relative.as_posix()} ==="
        )
    # Read every input before creating output; never overwrite an earlier export.
    with destination.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write("\n".join(sections) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="New text file; parent must exist")
    args = parser.parse_args()
    try:
        export(ROOT, args.output)
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    print(f"Created {args.output} from {len(SOURCES)} public source files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
