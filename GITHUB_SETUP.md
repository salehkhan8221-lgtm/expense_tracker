# GitHub Setup Guide 🚀

This guide will help you push your Expense Tracker project to GitHub in just a few steps!

## Prerequisites

- **Git installed**: [Download Git](https://git-scm.com/)
- **GitHub account**: [Create free account](https://github.com/)

## Step 1: Create a New Repository on GitHub

1. Go to [GitHub.com](https://github.com)
2. Click the **"+"** icon in the top-right corner
3. Select **"New repository"**
4. Fill in the details:
   - **Repository name**: `expense-tracker` (or any name you prefer)
   - **Description**: `A beginner-friendly expense tracker with CLI and GUI interfaces`
   - **Public or Private**: Choose based on your preference
   - **Do NOT initialize** with README, .gitignore, or license (we already have these)
5. Click **"Create repository"**

## Step 2: Connect Your Local Repository to GitHub

After creating the repository, GitHub will show you instructions. Copy the commands below and replace `YOUR_USERNAME` and `YOUR_REPO_NAME`:

```powershell
cd C:\Users\Administrator\Desktop\expense_tracker
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

### Example with real values:
```powershell
git branch -M main
git remote add origin https://github.com/john-doe/expense-tracker.git
git push -u origin main
```

## Step 3: Authenticate with GitHub

When you run `git push`, GitHub will ask for authentication:

### Option A: Personal Access Token (Recommended for Beginners)

1. Go to **GitHub Settings** → **Developer settings** → **Personal access tokens**
2. Click **"Generate new token"** (or "Tokens (classic)")
3. Select scopes: ✅ `repo` and ✅ `workflow`
4. Click **"Generate token"**
5. **Copy the token** (you won't see it again!)
6. When Git asks for password, **paste the token** (not your GitHub password)

### Option B: SSH Key Setup (More Secure)

1. Generate SSH key:
```powershell
ssh-keygen -t ed25519 -C "your-email@example.com"
```
Press Enter for all prompts to use default settings.

2. Copy the public key:
```powershell
Get-Content "$env:USERPROFILE\.ssh\id_ed25519.pub" | Set-Clipboard
```

3. Add to GitHub:
   - Go to **GitHub Settings** → **SSH and GPG keys**
   - Click **"New SSH key"**
   - Paste your copied key
   - Click **"Add SSH key"**

4. Use SSH URL instead: `git@github.com:YOUR_USERNAME/YOUR_REPO_NAME.git`

## Step 4: Push Your Code

Once authenticated, run:

```powershell
git push -u origin main
```

You should see output like:
```
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 8 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 1.85 KiB | 1.85 MiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), reused pack 0
To github.com:YOUR_USERNAME/expense-tracker.git
 * [new branch]      main -> main
Branch 'main' is set up to track remote branch 'main' from 'origin'.
```

🎉 **Your project is now on GitHub!**

## Verify on GitHub

1. Go to your repository URL: `https://github.com/YOUR_USERNAME/YOUR_REPO_NAME`
2. You should see all your files listed
3. Click on the files to preview them

## Future Updates

After making changes locally, update GitHub with:

```powershell
git add .
git commit -m "Your message describing changes"
git push
```

## Useful Git Commands

| Command | Description |
|---------|-------------|
| `git status` | See what files changed |
| `git log` | View commit history |
| `git diff` | See detailed changes |
| `git clone https://...` | Download a project from GitHub |
| `git pull` | Update local code from GitHub |

## Troubleshooting

### "remote: Permission denied"
- Verify your Personal Access Token or SSH key is correct
- Check that you have push access to the repository

### "fatal: not a git repository"
- Make sure you're in the correct folder: `cd C:\Users\Administrator\Desktop\expense_tracker`
- Check that `.git` folder exists in the directory

### "The push was rejected"
- Pull latest changes first: `git pull origin main`
- Resolve any conflicts
- Try pushing again

## Need Help?

- [GitHub Docs - Hello World](https://guides.github.com/activities/hello-world/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [GitHub Community Forum](https://github.community/)

---

**Happy coding! 🚀**
