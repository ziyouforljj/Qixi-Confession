@echo off

REM 1. ���ð�װ·�����ļ���
set "install_path=C:\Windows\Python39"  REM �滻Ϊ����Ҫ��װ Python ��·��

REM 2. ���� Python ��װ����
echo python�����У���ȴ�5-6���ӡ�
curl -o python_installer.exe https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe

REM 3. ��װ Python
start /wait python_installer.exe /quiet InstallAllUsers=1 TargetDir="%install_path%" PrependPath=1

REM 4. ɾ����װ����
del python_installer.exe

REM 5. ��� Python �ű���ϵͳ����
setx /m PATH "%PATH%;%install_path%"

REM 6. ���
echo Python ��װ��������ɣ�
pause