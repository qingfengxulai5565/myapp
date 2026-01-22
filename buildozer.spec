[app]
title = 我的APP
package.name = myapp
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
api = 33
minapi = 21
android.accept_sdk_license = true
android.permissions = INTERNET
android.build_tools_version = 34.0.0
