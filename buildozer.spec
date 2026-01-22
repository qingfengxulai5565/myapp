[app]
title = 我的第一个APP
package.name = myfirstapp
package.domain = com.example
source.dir = .
source.include_exts = py,png,jpg,kv
version = 1.0
requirements = python3,kivy

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[android]
api = 31
minapi = 21
android.accept_sdk_license = true
android.permissions = INTERNET

# 指定使用较旧的build-tools版本，避免许可证问题
android.build_tools_version = 33.0.0
