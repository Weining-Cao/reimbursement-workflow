# 文件校验工具

`scripts/check_packet.py` 仅依赖 Python 3.10+ 标准库，对明确列出的文件计算哈希。它不生成、解析或目视检查 Word／PDF，不证明输出与来源对应、报销资格或交付就绪，也无法发现未列入的依赖。快照是本地变化检测记录，不是签名审计日志。

在私人材料目录创建清单：

```json
{
  "version": 1,
  "inputs": [
    "case.md",
    "expenses.csv",
    "rules.md",
    "original-template.docx",
    "working-summary.docx",
    "evidence/hotel-invoice.pdf"
  ],
  "outputs": [
    "summary.pdf",
    "packet.pdf",
    "review.md"
  ]
}
```

路径相对于清单所在目录。列入全部可能使交付失效的依赖，包括当前 Word、实际使用的规则副本和页码清单（可放在 `review.md` 中）。纸质材料写入 `case.md`，不伪造文件路径。两组列表均须非空；重复解析路径、父目录跳转、绝对路径、缺失文件、目录及逃出案例目录的符号链接都会被拒绝，清单和锁文件不能列入自身。

1. 完成编辑、重建和实际页面复核，填好复核报告。
2. 暂停编辑，执行 `record MANIFEST --lock NEW_LOCK`；锁文件必须不存在。只有内容核验后才记录，不能为消除过期提示重录。
3. 交付前执行 `check MANIFEST --lock LOCK`；哈希期间保持文件不变，本工具没有文件系统事务或并发写保护。
4. 发现变化后定位原因、重建受影响文件、复查，再用新锁文件记录新版本。

从任意目录可用脚本的绝对路径运行；以下两个路径均替换为实际位置：

```sh
python3 /path/to/skill/scripts/check_packet.py record /path/to/private-case/manifest.json --lock /path/to/private-case/review-v1.lock.json
python3 /path/to/skill/scripts/check_packet.py check /path/to/private-case/manifest.json --lock /path/to/private-case/review-v1.lock.json
```

退出码：`0` 表示已记录或文件未变；`1` 表示清单／文件变化；`2` 表示无效数据、文件缺失／不可读或其他 I/O 错误。`1`、`2` 都不能算检查通过；即使为 `0`，PDF 内容仍可能错误。工具不会更新案例状态。
