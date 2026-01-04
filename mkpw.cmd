@echo off
chcp 65001
setlocal
:: SPDX-License-Identifier: 0BSD
title mkpw

py.exe -3 "%~dp0mkpw" %*
pause
