#!/bin/bash -x

# 1. Install the application
site=$1
logfile=$2
echo $lofgile
echo "Starting"
/home/jnejati/android-sdk-linux/platform-tools/adb uninstall "org.chromium.chrome.testshell" # Uninstall application if already installed
/home/jnejati/android-sdk-linux/platform-tools/adb logcat -c # Clear log buffer
/home/jnejati/android-sdk-linux/platform-tools/adb install "/home/jnejati/chrome/ChromiumTestShell.apk" # Install the application

# 2. Launch the application
/home/jnejati/android-sdk-linux/platform-tools/adb logcat -c
/home/jnejati/android-sdk-linux/platform-tools/adb shell am start -n "org.chromium.chrome.testshell"/"org.chromium.chrome.testshell.ChromiumTestShellActivity" # Launch the application
sleep 2 # wait for 50 sec
#/home/jnejati/android-sdk-linux/platform-tools/adb shell am start -n "org.chromium.chrome.testshell"/"org.chromium.chrome.testshell.ChromiumTestShellActivity"  $site
#sleep 2 # wait for 50 sec

#/home/jnejati/android-sdk-linux/platform-tools/adb shell su -c 'rm -rf /data/data/org.chromium.chrome.testshell/cache'
#sleep 2
/home/jnejati/android-sdk-linux/platform-tools/adb shell am start -n "org.chromium.chrome.testshell"/"org.chromium.chrome.testshell.ChromiumTestShellActivity"  $site
#/home/jnejati/android-sdk-linux/platform-tools/adb logcat *:E | tee $logfile
/home/jnejati/android-sdk-linux/platform-tools/adb logcat *:E> $logfile
#sleep 50 # wait for 50 sec
exit 0
