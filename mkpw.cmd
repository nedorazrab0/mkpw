@echo off
chcp 65001
:: SPDX-License-Identifier: 0BSD
setlocal
title mkpw

py.exe -3 "%~dp0mkpw" %*
pause
