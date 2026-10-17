---
name: reimbursement-workflow
description: Assist Nanjing University international computer science conference travel from student OA drafting to evidence collection, reimbursement forms, and rule-based PDF review. Use for preparing or reviewing a travel case; not an approval service.
---

# 差旅报销工作流

处理案例前阅读[执行流程](references/workflow.md)。围绕“适用规则 → 整理材料 → 逐条检查 → 最终交付”，从用户当前阶段继续，遵守本次范围，不重复已完成的申请或材料收集。

- 根据[规则索引](references/rules.md)建立适用条目和证据关系；未知或冲突事项保持待确认。
- 行前使用 [OA 草稿](assets/oa-draft.md)，其他记录使用[案例模板](assets/case.md)、[费用台账](assets/expenses.csv)和[复核模板](assets/review.md)。副本保存在仓库外的私人目录，案例处理不修改 Skill 源文件。
- 缺材料时读[收集说明](references/collection.md)，发现并使用已授权的浏览器、邮箱和文档工具；不让用户重复获取可自行取得的材料，也不声称具备当前没有的能力。编辑文件前检查可用工作区依赖。
- 组装后按[财务复核](references/finance-review.md)核对实际 PDF 和另交材料，修正、重建并复查；全部适用条目通过后才标为最终，脚本成功不等于内容正确。

学生 OA 可填写和上传，只能由申请人本人点击提交；财务报销交经办老师处理。签字、盖章及所需原件按适用规则办理。已获授权范围可继续使用，但工具示例不授予安装软件或调用外部服务的权限，不主动打开抢占焦点的窗口。

需要检测文件是否在复核后变化时，按[校验工具说明](references/integrity.md)使用 `scripts/check_packet.py`；结果只证明文件未变。用户要求复查已有申报流程时使用[副本回放](references/replay.md)，不改已提交材料。

用中文返回实际完成的文件链接、复核结论和必要待办，不将可交付或已递交写成财务已批准。
