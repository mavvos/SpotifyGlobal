<h1 align="center">🎵 Spotify Global 🌐</h1>
<div align="center">
  
[![download](https://img.shields.io/badge/Download-Latest-green)](https://github.com/mavvos/SpotifyGlobal/releases/latest)
[![license](https://img.shields.io/badge/License-MIT-red)](https://github.com/mavvos/SpotifyGlobal/blob/main/LICENSE)
[![python](https://img.shields.io/badge/Python-3.6-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

  Control Spotify from anywhere with customizable Global Hotkeys!\
  No need for the window to be in focus, working for all Spotify accounts (free & premium)!

</div>

#
### How does this work?
SpotifyGlobal listens for hotkeys with the <i><b>keyboard</b></i> module then sends them to <i><b>pywinauto</b></i> who will send the equivalent hotkey command to the Spotify application.
Because commands are sent <b>only</b> to the Spotify window, this script doesn't affect any  other audio sources! And because it doesn't use Spotify API, it's functional for all Spotify accounts (free & premium).

### Why does this exist?
While Spotify has built-in hotkeys, they don't work out of focus (at least not for me), this is what I was looking to fix with SpotifyGlobal. Sometimes you just don't have time to alt tab or open game bar but still want to interact with the Spotify desktop application. I tried really hard to find a global hotkey solution for a while, but all of them had some sort of problem, so the natural conclusion was for me to make a script that works for my needs, and I'm sharing it in hopes it can help you too!

### How do I make SpotifyGlobal run on startup?
If you want the script to start on Windows boot, follow [this tutorial](https://support.microsoft.com/en-us/windows/add-an-app-to-run-automatically-at-startup-in-windows-10-150da165-dcd9-7230-517b-cf3c295d89dd). Make you sure you add a shortcut to the script, not the script itself.

#
<h3>🎁 Download</h3>
Click <a href="https://github.com/mavvos/SpotifyGlobal/releases/latest">here</a> to download the latest version.


On the download page there's an executable version (.exe), download it, double click and you're good to go!



If you are trying to run the Python script, you'll need Python version 3.6 or newer, then clone this repository:
```
git clone https://github.com/mavvos/SpotifyGlobal.git
```

Make sure you have the required modules installed. Inside the cloned directory run:
```
pip install -r requirements.txt
```

Inside the SpotifyGlobal directory run SpotifyGlobal.py

#
<h3>📂 Your First Time Opening</h3>
The first time you run the script it will try to find Spotify's executable in the default installation folder, if it's not found there, you'll be prompted to type your Spotify's application path.

After that, a file is created containing your path and hotkeys (options.txt).

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

Keys are written as you would expect them, in plain english, so to change the above, you could put:
```
VolDown=alt+shift+p
```

This way, to send the Volume Down command to Spotify, you would have to simultaneously press <i>ALT SHIFT P</i>

#
<h3>🐜 Known Issues and Bugs 🦟</h3>
<ol>
  <li><b>Spotify needs to be closed</b> when you run this script. If your Spotify is already running when you try opening the script, it will not work.</li>
  <li><b>If Spotify is minimized it will continue to appear when you press a hotkey</b>. To fix this don't minimize Spotify, let the window open and click away to your other programs.</li>
  <li>If you spam press hotkeys, you may get stuck in a loop where the commands keep repeating, to fix this close everything and restart the application.</li>
  <li>Some hotkey combinations have more trouble than others when it comes to being registered, this is a common problem with the <i>keyboard</i> library.</li>
  <li>This software works only on Windows, because of the dependencies on modules pywinauto and pywin32.</li>
</ol>
