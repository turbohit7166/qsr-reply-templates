# QSR Reply Templates

多语言客服回复模板库 & 简单生成器，面向小型餐饮/零售门店（QSR）。  
Multi-language customer service reply templates & simple generator for small QSR/retail stores.  
Bibliothèque de modèles de réponses au service client et générateur simple pour petites enseignes QSR/retail.

## 功能 / Features / Fonctionnalités

- 预置常见场景模板：订单延迟、餐品做错、退款、招聘咨询等  
- 支持中文 / English / Français 三语模板  
- 简单命令行工具，根据场景 + 语言输出回复草稿  
- 易于扩展：只需在 `templates/*.json` 中增加场景即可  

## 安装 / Installation / Installation

1. 克隆仓库：
   ```bash
   git clone https://github.com/turbohit7166/qsr-reply-templates.git
   cd qsr-reply-templates
   ```
2. 确保已安装 Python 3.8+。  
3. 无需额外依赖，直接运行 `generator.py`。

## 使用 / Usage / Utilisation

列出所有场景：

```bash
python generator.py --list
```

生成回复（以“订单延迟”的中文版本为例）：

```bash
python generator.py --scenario complaints:late_order --lang zh
```

支持的语言：`zh`（中文）、`en`（English）、`fr`（Français）。

## 适用对象 / Target Users / Public cible

- 小型餐饮店、快餐店、便利店、零售门店  
- 需要多语言客服回复模板的店主和员工  
- 想标准化客服话术、提高响应速度的团队  

## 贡献 / Contributing / Contribution

欢迎提交 Issue 和 Pull Request，尤其是：

- 新的场景模板  
- 更贴近实际业务的措辞  
- 更多语言支持  

## 许可证 / License / Licence

MIT License. 详见 `LICENSE` 文件。

---

## 中文说明

本项目由一位在蒙特利尔经营 Dairy Queen 的店主发起，用于统一管理日常客服回复模板（投诉、退款、招聘等），并分享给同类小商家使用。

## English Description

This project was started by a Dairy Queen franchise owner in Montreal to standardize daily customer service replies (complaints, refunds, hiring inquiries, etc.) and share them with similar small businesses.

## Description en français

Ce projet a été lancé par un franchisé Dairy Queen à Montréal afin de standardiser les réponses quotidiennes au service client (plaintes, remboursements, demandes d'embauche, etc.) et de les partager avec d'autres petites entreprises.
