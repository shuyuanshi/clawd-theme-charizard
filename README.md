# Clawd on Desk Theme - Charizard (喷火龙)

Clawd on Desk 应用的**喷火龙 (Charizard)** 桌宠主题包。

## 📦 主题内容

- `theme.json`: 主题配置文件与动作动画映射
- `assets/`: 各状态 GIF 动画资源文件
  - `idle.gif`: 站立
  - `thinking.gif`: Mega 喷火龙 Y 思考
  - `working.gif`: 爪击工作
  - `attention.gif`: 咆哮/权限请求
  - `error.gif`: 尾巴攻击/报错
  - `notification.gif`: G-Max 极巨化通知
  - `sleeping.gif`: 异色喷火龙睡眠
  - `run-left.gif` / `run-right.gif`: 点击反应/奔跑

## 🚀 跨电脑同步与安装使用

### macOS 安装说明

在目标 Mac 上，直接将本仓库克隆至 Clawd on Desk 的主题目录下：

```bash
mkdir -p "$HOME/Library/Application Support/clawd-on-desk/themes"
git clone git@github.com:shuyuanshi/clawd-theme-charizard.git "$HOME/Library/Application Support/clawd-on-desk/themes/charizard"
```

或者克隆到 `~/projects/` 目录并建立软链接：

```bash
git clone git@github.com:shuyuanshi/clawd-theme-charizard.git ~/projects/clawd-theme-charizard
mkdir -p "$HOME/Library/Application Support/clawd-on-desk/themes"
ln -s ~/projects/clawd-theme-charizard "$HOME/Library/Application Support/clawd-on-desk/themes/charizard"
```

完成之后重新打开 Clawd on Desk 应用，在设置/主题列表中切换至 **喷火龙 Charizard** 即可。
