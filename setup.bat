@echo off

echo Criando arquivo .env...
echo f | xcopy /f /y .env.example .env > nul
timeout /t 1 /nobreak
cls

echo Criando ambiente virtual...
call python -m venv venv
timeout /t 1 /nobreak
cls

echo Instalando dependencias...
venv\Scripts\python.exe -m pip install -r requirements.txt
timeout /t 1 /nobreak
cls

echo O ambiente foi configurado com sucesso!
echo Por favor configure a sua matricula e senha no arquivo .env