<h1 align="center">🎵 Spotify Global 🌐</h1>
<div align="center">
  
  <a href="https://github.com/mavvos/SpotifyGlobal/blob/main/LICENSE">![License](https://img.shields.io/badge/License-MIT-red)</a>
  <a href="https://github.com/mavvos/SpotifyGlobal/releases/latest">![Demo](https://img.shields.io/badge/Download-Latest-green)</a>

  Control Spotify from anywhere with customizable Global Hotkeys!\
  No need for the window to be in focus, working for all Spotify accounts (free & premium)!

</div>

#
<h3>❓ F.A.Q.</h3>

### How does this work?
This Python script listens for hotkeys with the <i><b>keyboard</b></i> module then sent to the <i><b>pywinauto</b></i> module who will send the equivalent hotkey command to the Spotify application.
Because commands are sent <b>only</b> to the Spotify window, this script doesn't affect any  other audio sources! And because it doesn't use Spotify API, it's functional for all Spotify accounts.

### Why does this exist? Spotify already has hotkeys?
It's true that Spotify has hotkeys, but they don't work out of focus (at least not for me), this is what I was looking to fix with SpotifyGlobal. Sometimes you just don't have time to alt tab or open game bar to interact with Spotify.

### Toastify, hayer's SpotifyHotkeys, lofi, etc. already do that. Why didn't you just use them?
Trust me when I say that I tried really hard to find a global hotkey solution for a long time, but in all of them there was always a problem, so the natural conclusion was for me to make a script that works for my needs, and I'm sharing it in hopes that I can help someone that had the same problem.

### How do I make the script run on startup?
If you want the script to start on Windows boot,  follow [this tutorial.](https://support.microsoft.com/en-us/windows/add-an-app-to-run-automatically-at-startup-in-windows-10-150da165-dcd9-7230-517b-cf3c295d89dd). Make you sure you add a shortcut to the script, not the script itself, if you add the script to the folder the created options file will also open on boot.

#
<h3>🎁 Download</h3>
Click <a href="https://github.com/mavvos/SpotifyGlobal/releases/latest">here</a> to download the latest version.


On the download page you can get the executable version (.exe), it should work as any other normal application, just run it.

If you are trying to run the Python version, clone this repository and get the modules in requirements.txt
```
pip install -r requirements.txt
```

Then inside the SpotifyGlobal directory run SpotifyGlobal.py

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
  <li>The script doesn't seem to work with the Microsoft Store version of Spotify (untested).</li>
  <li>If you spam press hotkeys, you may get stuck in a loop where the commands keep repeating, to fix this close everything and restart the application.</li>
  <li>Some hotkey combinations have more trouble than others when it comes to being registered, this is a common problem with the <i>keyboard</i> library.</li>
  <li>If you are not on Windows, there's a chance the script won't work for you, this is a problem with the <i>pywinauto</i> library.</li>
</ol>
