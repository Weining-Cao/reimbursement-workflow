# 虚构案例试用

本目录只有虚构文本，用于检验费用去重、币种分开、日期冲突、纸质交接和文件变化检测，不是真实票据、官方模板或已渲染文档。示例中的 `Example University` 及其要求不代表南京大学制度。

## 开始试用

按项目首页提供工作流后，发送：

```text
请用差旅报销工作流，只检查这个虚构文本案例。
读取 examples/synthetic 中的 case.md、evidence.txt 和 expenses.csv，
将其视为虚构用户给定事实，在独立临时目录或聊天中写结论。
计算原币小计，指出未解决问题并给出下一步。
不访问真实邮箱，不搜索虚构学校，不编造规则，不改示例文件。
本次不要求生成 Word 或 PDF。
```

本地 agent 使用完整示例目录路径；纯聊天使用者将三个输入文件与 `START_CHAT.txt` 一起上传或粘贴。先形成准确台账及具体下一步即可，不应为得到“可提交”结论跳过阻碍。

## 预期结果

- [案例](case.md)中，2030 年 Example Workshop 的表格日期确认为 6 月 3—7 日／五天，但返程证据为 6 月 8 日。保留双方事实及待解释问题，不擅改草稿或推定资格。
- [证据](evidence.txt) E1 和 E2 支持同一笔 USD 120.00 费用；[台账](expenses.csv)原币小计为 **USD 145.50、EUR 64.20**，不重复计费或虚构汇率。`reviewed` 只表示示例金额已核对，不是资格或财务批准。
- [预期汇总文本](summary.txt)保留仅城市路线和有意留空的经费栏；[复核结果](review.md)明确纸件仅由用户确认、视觉检查与合并未完成，整体仍为 `needs-review`。

[材料收集演练](collection-walkthrough.md)是另一个假想交互，展示从查规则到补件、部门办理和合集复核的过程；不是已执行的浏览器／邮箱测试，也不改变本目录文本案例的状态。

## 可选文件校验演示

先将整个示例目录复制到私人临时目录。按[工具说明](../../skills/reimbursement-workflow/references/integrity.md)，用副本的 [manifest.json](manifest.json)和新锁文件运行 `record`，再改副本 `summary.txt` 并运行 `check`，预期返回 `STALE` 和退出码 1。修改副本 `case.md` 或 `expenses.csv` 也须使快照失效；不要改公共示例来做演示。

完整文档试用需另备虚构 Word 模板和 PDF，在私人目录按[情景检查](../../evals/scenarios.md)评估实际导出和合并结果。本目录本身不验证 Word 编辑或 PDF 制作。
