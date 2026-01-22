[app]
title = 我的APP
package.name = myapp
package.domain = com.example
source.dir = .
source.include_exts = py,png,jpg,kv
version = 0.1
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
EO
# 创建最简化的buildozer.spec
cat > buildozer.spec << 'EOF'
[app]
title = 我的APP
package.name = myapp
package.domain = com.example
source.dir = .
source.include_exts = py,png,jpg,kv
version = 0.1
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
