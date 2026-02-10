@echo off
cd /d E:\GPBiz
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/alanburchill/GroupPolicyBiz.git
git push -u --force origin main
