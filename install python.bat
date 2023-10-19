@echo off

REM 1. 设置安装路径和文件名
set "install_path=C:\Windows\Python39"  REM 替换为你想要安装 Python 的路径

REM 2. 下载 Python 安装程序
echo python下载中，请等待5-6分钟。
curl -o python_installer.exe https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe

REM 3. 安装 Python
start /wait python_installer.exe /quiet InstallAllUsers=1 TargetDir="%install_path%" PrependPath=1

REM 4. 删除安装程序
del python_installer.exe

REM 5. 添加 Python 脚本到系统变量
setx /m PATH "%PATH%;%install_path%"

REM 6. 完成
echo Python 安装和配置完成！
pause