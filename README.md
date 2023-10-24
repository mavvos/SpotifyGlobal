<h1 align="center">🎵 Spotify Global 🌐</h1>
<div align="center">
  
  <a href="https://github.com/mavvos/SpotifyGlobal/blob/main/LICENSE">![License](https://img.shields.io/badge/License-MIT-red)</a>
  <a href="https://github.com/mavvos/SpotifyGlobal/releases/latest">![Demo](https://img.shields.io/badge/Download-Latest-green)</a>

  Control Spotify from anywhere with Global Hotkeys!\
  No need for the window to be in focus, working for all users (free & premium)

</div>
<hr>
<h3>🔨 How It Works</h3>
This script works recording key presses with <i>keyboard</i> and using <i>pywinauto</i> to send the equivalent hotkey command to the Spotify application.
Because it doesn't use Spotify API, it's completely functional for all Spotify accounts.
And since the command is sent <b>only</b> to the Spotify window, it doesn't affect any of your other audio sources!

#
<h3>🎁 Download</h3>
Click <a href="https://github.com/mavvos/SpotifyGlobal/releases/latest">here</a> for the latest version.

If you don't have python installed, download the .exe (executable version) and run it, it should work as any other normal application.

If you are trying to run the python script version, you'll need to install the modules in requirements.txt
```
pip install -r requirements.txt
```


#
<h3>📂 Your First Time Opening</h3>
The first time you run the script it will try to find Spotify's executable in the default installation folder, if it's not found there, you'll be prompted to type your Spotify's application path.

Which by default is located at:
```
C:\Users\~\AppData\Roaming\Spotify\Spotify.exe
```
After that, <b>a file (options.txt) is created containing your default path and your hotkeys</b>, so you don't have to keep typing again.

#
<h3>🎹 Default Controls</h3>
<h6>Hotkey in Script = Expected Command</h6>

```
SHIFT + 8 = Volume Up
SHIFT + 2 = Volume Down
SHIFT + 4 = Previous Track
SHIFT + 6 = Next Track
SHIFT + 5 = Play/Pause
SHIFT + 1 = Go back 5 seconds
SHIFT + 3 = Go forward 5 seconds
SHIFT + 7 = Like/Dislike Track
SHIFT + 9 = Quit Script
```

#
<h3>⌨ Custom Controls</h3>
If you wish to <b>customize your hotkeys</b>, simply locate your options.txt and alter the value that follows the "="

A normal hotkey looks something like this:
```
VolDown=shift+2
```

Keys are written as you'd expect, in plain english, so to change the hotkey above, you can put something like:
```
VolDown=alt+shift+p
```

This way, to send the Volume Down command to Spotify, you would have to simultaneously press <i>ALT SHIFT P</i>

#
<h3>🐜 Known Issues and Bugs 🦟</h3>
<ul>
  <li><b>Spotify needs to be closed</b> when you run this script. If your Spotify is already running when you try opening the script, it will not work.</li>
  <li><b>If Spotify is minimized it will continue to appear when you press a hotkey</b>. To fix this, just don't minimize Spotify, let the window open and click away to your other programs.</li>
  <li>The script doesn't seem to work with the Microsoft Store version of Spotify (because you can't access Spotify's path folder, lol).</li>
  <li>You should never have an options.txt file if it's your first run and/or if you can't open Spotify, if this somehow happens, just delete the options.txt file.</li>
  <li>If you delete any line from options.txt, the script will crash. To fix this simply delete the options.txt file completely and a new one will be created for you on next launch.</li>
  <li>If you spam press hotkeys, you may get stuck in a loop where the commands keep repeating, to fix this close the script and Spotify and restart the application.</li>
  <li>Sometimes the message about application running takes longer than usual to appear.</li>
  <li>Some hotkey combinations have more trouble than others when it comes to being registered, this is a problem with the <i>keyboard</i> library.</li>
  <li>If you are not on Windows, there's a chance the script won't work for you, this is a problem with the <i>pywinauto</i> library.</li>
</ul>
