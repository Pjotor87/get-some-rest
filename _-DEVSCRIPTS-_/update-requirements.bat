@echo off
cd ..
cd Scripts
call activate.bat
cd ..
pip freeze > Requirements.txt
git add Requirements.txt
git commit -m "Requirements updated"