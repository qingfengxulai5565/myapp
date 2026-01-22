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
api = 31
minapi = 21
android.accept_sdk_license = true
android.permissions = INTERNET
