<h1 align="center">🎵 Spotify Global 🌐</h1>
<div align="center">
  
  <a href="https://github.com/mavvos/SpotifyGlobal/blob/main/LICENSE">![License](https://img.shields.io/badge/License-MIT-red)</a>
  <a href="https://github.com/mavvos/SpotifyGlobal/releases/latest">![Demo](https://img.shields.io/badge/Download-Latest-green)</a>

  Control Spotify from anywhere with Global Hotkeys!\
  No need for the window to be in focus, working for all users (free & premium)

</div>
<hr>
<h3>🔨 How It Works</h3>
This script works registering key presses with <i>keyboard</i> and using <i>pywinauto</i> to send the equivalent hotkey command to the Spotify application.
Because it doesn't use Spotify's API, it's completely functional for all Spotify accounts.
And because the command is sent <b>only</b> to the Spotify window, it doesn't affect any of your other audio sources!

#
<h3>🎁 Download</h3>
Click <a href="https://github.com/mavvos/SpotifyGlobal/releases/latest">here</a> for the latest version.

If you don't have python installed, download the .exe (executable version) and run it, should work as any other normal app.

If you are trying to run the python script version, you'll need to install the modules in requirements.txt
```
pip install keyboard pywinauto
```


#
<h3>📂 Your First Time Opening</h3>
The first time you run the script, it will try to find Spotify's executable in the default installation folder, if it's not found there, you'll be prompted to type your Spotify's application path.

Which by default is located at:
```
C:\Users\~\AppData\Roaming\Spotify\Spotify.exe
```
After that, <b>a file (options.txt) is created containing your default path and your hotkeys</b>, so you don't need to keep retyping.

#
<h3>🎹 Default Controls</h3>
<h6>Hotkey in Script = Expected Command</h6>

```
SHIFT + 8   = Volume Up
SHIFT + 2   = Volume Down
SHIFT + 4   = Previous Track
SHIFT + 6   = Next Track
SHIFT + 5   = Play/Pause
SHIFT + 1   = Go back 5 seconds
SHIFT + 3   = Go forward 5 seconds
SHIFT + 7   = Like/Dislike Track
SHIFT + 9   = Quit Script
```

#
<h3>⌨ Custom Controls</h3>
If you wish to <b>customise your hotkeys</b>, simply locate your options.txt and alter the value that follows the "="

A normal hotkey looks something like this:
```
VolDown=shift+2
```

Keys are written as you expect them to be, in plain english, so to change the hotkey above, you could put something like:
```
VolDown=alt+shift+p
```

That way, to send the command Volume Down to Spotify, you would have to press simultaneously <i>ALT SHIFT P</i>

#
<h3>🐜 Known Problems and Bugs 🦟</h3>
<ul>
<li><b>Spotify needs to be closed</b> when you run this script. The script takes care of oppening Spotify for you, in fact it <b>has</b> to open Spotify for it to work, if your Spotify is already running when you try oppening this, the script will just crash and not work.</li>
<li>Script doesn't seem to work with the Microsoft Store version of Spotify (because you can't access Spotify's path folder, lol).</li>
<li>If you spam press hotkeys you can get stuck in a loop where the commands keep repeating, to fix this restart application.</li>
<li>If you delete any line from options.txt after your first launch, the script will crash, to fix this just delete the options.txt file alltogether and a new one will be created for you on next launch.</li>
<li>Spotify needs to be open as a window for the script to work, if Spotify is minimized it will keep popping up when you press a hotkey, to fix this just let Spotify's window open and click away to your other programs.</li>
<li>Sometimes the message about app running takes longer than normal to appear.</li>
<li>If you are not on Windows, there's a high chance the script won't work for you, because it uses the library <i>pywinauto</i>.</li>
</ul>
