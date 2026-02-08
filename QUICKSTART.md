# Quick Start Guide 🚀

## Run the GUI (Easiest - Click & Play!)

```powershell
python expense_tracker_gui.py
```

## Run the CLI (Command-Line)

```powershell
python expense_tracker.py
```

## Run Tests

```powershell
python test_tracker.py
```

---

## First Time Setup for GitHub

1. **Create GitHub Account**: https://github.com/signup

2. **Create New Repository** on GitHub website
   - Name it: `expense-tracker`
   - Click "Create repository"

3. **Copy & Run** (replace YOUR_USERNAME and YOUR_REPO_NAME):

```powershell
cd C:\Users\Administrator\Desktop\expense_tracker
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

4. **Enter Token When Prompted**:
   - Go to: https://github.com/settings/tokens
   - Click "Generate new token"
   - Copy the token
   - Paste when Git asks (it won't show as you type)

---

## After Changes, Update GitHub

```powershell
git add .
git commit -m "Your description of changes"
git push
```

---

## File Overview

| File | Purpose |
|------|---------|
| `expense_tracker_gui.py` | 🎨 GUI version (recommended!) |
| `expense_tracker.py` | 💻 CLI version |
| `test_tracker.py` | 🧪 Automated tests |
| `expenses.csv` | 📊 Your data (auto-created) |
| `README.md` | 📖 Full documentation |
| `GITHUB_SETUP.md` | 📤 GitHub instructions |
| `.gitignore` | 🚫 Files to skip in Git |

---

**Questions?** See [README.md](README.md) or [GITHUB_SETUP.md](GITHUB_SETUP.md)
