@echo off
chcp 65001 >nul
echo ========================================================
echo   GITHUB YUKLEME ARACI (Resul Ekrem OZCAN - 25902009)
echo ========================================================
echo.
echo Lutfen GitHub'da olusturdugunuz repository linkini yapistirin.
echo Ornek: https://github.com/KULLANICI_ADINIZ/25902009_ResulEkremOzcan_InventoryManagement.git
echo.
set /p REPO_URL="Repository URL: "

if "%REPO_URL%"=="" (
    echo Hata: URL girmediniz!
    pause
    exit /b
)

echo.
echo 1. Remote baglantisi ayarlaniyor...
git remote remove origin >nul 2>&1
git remote add origin %REPO_URL%
git branch -M main

echo 2. Kodlar GitHub'a yukleniyor (git push)...
git push -u origin main

echo.
echo ========================================================
echo ISLEM TAMAMLANDI!
echo Eger yukarida 'main -> main' yazisini gorduyseniz kodlariniz basariyla yuklenmistir.
echo Simdi hocaniz 'tohid.yousefi'yi Collaborator olarak eklemeyi unutmayin!
echo ========================================================
pause
