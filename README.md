<h1 align="center">🎵 Spotify Global 🌐</h1>
<div align="center">
  
[![download](https://img.shields.io/badge/Download-Latest-green)](https://github.com/mavvos/SpotifyGlobal/releases/latest)
[![license](https://img.shields.io/badge/License-MIT-red)](https://github.com/mavvos/SpotifyGlobal/blob/main/LICENSE)
[![python](https://img.shields.io/badge/Python-3.10-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

  Control Spotify from anywhere with customizable Global Hotkeys!\
  No need for the window to be in focus, working for all Spotify accounts (free & premium)!

</div>

#
### How does this work?
SpotifyGlobal is a python script that works listening for hotkeys with the <i><b>keyboard</b></i> module then sending them to <i><b>pywinauto</b></i> who will send the equivalent hotkey command to the Spotify application.
Because commands are sent <b>only</b> to the Spotify window, this script doesn't affect any  other audio sources! And because it doesn't use Spotify API, it's functional for all Spotify accounts (free & premium).

### Why does this exist?
While Spotify has built-in hotkeys, they don't work out of focus, this is what I was looking to fix with SpotifyGlobal. Sometimes you just don't have time to alt tab or open game bar but still want to interact with the Spotify desktop application. I tried really hard to find a global hotkey solution for a while, but all of them had some sort of problem, so the natural conclusion was for me to make a script that works for my needs, and I'm sharing in hopes it can help you too!

#
<h3>🎁 Download</h3>
Click <a href="https://github.com/mavvos/SpotifyGlobal/releases/latest">here</a> to download the latest version.

On the download page there's an executable version (.exe), download it, double click and you're good to go!

If you are trying to run the Python script manully, you'll need Python version 3.10 or newer, then clone this repository:
```
git clone https://github.com/mavvos/SpotifyGlobal.git
```

Make sure you have the required modules installed. Inside the cloned directory run:
```
pip install -r requirements.txt
```

Then inside the SpotifyGlobal directory run SpotifyGlobal.py

#
<h3>🤔 How To Use </h3>
When you open SpotifyGlobal it connects to your open Spotify, because of this <b>Spotify must be open and active/maximized when you start SpotifyGlobal</b>.
<br><br>
After connection, let Spotify active/maximized and feel free to click away to other programs, now controlling Spotify with your new global hotkeys!
<br><br>
The first time you open SpotifyGlobal it creates an options.txt file that contains all your hotkeys.

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
  <li><b>If Spotify is minimized it will continue to appear when you press a hotkey</b>. To fix this don't minimize Spotify, let the window open/maximized and click away to your other programs.</li>
  <li>SpotifyGlobal doesn't seem to work when Spotify is "closed" to the system tray.</li>
  <li>SpotifyGlobal might not work if you have any other executable that has 'Spotify' in their name (for example, the github page for this project open in your browser), make sure Spotify is the only program using the Spotify name.</li>
  <li>If you spam press hotkeys, you may get stuck in a loop where the commands keep repeating, to fix this close everything and restart  applications.</li>
  <li>Some keys and hotkey combinations have more trouble than others when it comes to being registered, this is a common problem with the <i>keyboard</i> library.</li>
  <li>This software <i>should</i> work only on Windows, because of the dependencies on modules pywinauto and pywin32.</li>
</ol>
