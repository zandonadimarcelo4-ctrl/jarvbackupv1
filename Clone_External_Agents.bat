@echo off
setlocal enabledelayedexpansion

rem ---------------------------------------------------------------------------
rem  Clone_External_Agents.bat
rem  Clones or updates a set of public repositories that may be useful for
rem  PitronIA/OpenHands integrations. Repositories are placed under the
rem  "external_agents" folder in the same directory as this script.
rem ---------------------------------------------------------------------------

where git >nul 2>nul
if errorlevel 1 (
    echo [ERRO] Git nao foi encontrado no PATH. Instale o Git ou abra o prompt do Git.
    pause
    exit /b 1
)

set "SCRIPT_DIR=%~dp0"
set "TARGET_ROOT=%SCRIPT_DIR%external_agents"
if not exist "%TARGET_ROOT%" (
    mkdir "%TARGET_ROOT%"
    if errorlevel 1 (
        echo [ERRO] Nao foi possivel criar a pasta de destino: "%TARGET_ROOT%"
        pause
        exit /b 1
    )
)

for %%R in (
    "SmartManoj/Kevin"
    "block/goose"
    "kortix-ai/suna"
    "MikeyBeez/Ollama_Agents"
    "coleam00/local-ai-packaged"
    "tcsenpai/ollama-code"
    "TransformerOptimus/SuperAGI"
    "microsoft/autogen"
    "OpenInterpreter/open-interpreter"
) do (
    set "OWNER_REPO=%%~R"
    set "URL=https://github.com/!OWNER_REPO!.git"

    for %%F in ("!OWNER_REPO!") do set "FOLDER=%%~nxF"
    set "DEST=%TARGET_ROOT%\!FOLDER!"

    echo ------------------------------------------------------------
    echo [INFO] Processando !OWNER_REPO!

    if exist "!DEST!\.git" (
        echo [INFO] Repositorio ja existe. Atualizando com git pull...
        pushd "!DEST!" >nul
        git pull --ff-only
        if errorlevel 1 (
            echo [WARN] Falha ao atualizar !OWNER_REPO!. Verifique manualmente.
        ) else (
            echo [OK] Atualizado: !OWNER_REPO!
        )
        popd >nul
    ) else (
        if exist "!DEST!" (
            echo [WARN] Ja existe uma pasta chamada !DEST! sem .git. Pulando.
        ) else (
            echo [INFO] Clonando !URL! ...
            git clone "!URL!" "!DEST!"
            if errorlevel 1 (
                echo [ERRO] Falha ao clonar !OWNER_REPO!.
            ) else (
                echo [OK] Clonado em !DEST!
            )
        )
    )
)

echo ------------------------------------------------------------
echo [DONE] Processo concluido. Repositorios disponiveis em:
echo         %TARGET_ROOT%
pause
endlocal
