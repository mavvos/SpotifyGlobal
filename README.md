<h1 align="center">🎵 Spotify Global 🌍</h1>
<div align="center">

  [![python](https://img.shields.io/badge/Python-3.6-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
  [![issue](https://img.shields.io/badge/Report-Issue-red)](https://github.com/mavvos/SpotifyGlobal/issues)
  [![download](https://img.shields.io/badge/Download-Latest-brightgreen)](https://github.com/mavvos/SpotifyGlobal/releases/latest)

  Control Spotify from anywhere with customizable global hotkeys!\
  No need for the Spotify window to be in focus. Works for all accounts (Free & Premium)!
  
</div>

#
<h3 align=center>About the project</h3>
<b>Spotify Global</b> was created to solve a simple problem: Spotify's built-in media hotkeys only work when the application is in focus. This script allows you to control your music no matter what you're doing, whether you're in a full-screen game or working in another application. It works by listening for your custom hotkey combinations and sending the corresponding command directly to the Spotify desktop app, so it won't interfere with other audio sources on your system.

<h3>⭐ Key Features</h3>
<ul>
  <li>✅ Control: Control playback from anywhere on your desktop.
  <li>✅ Customizable: Easily change hotkeys by editing a simple text file.
  <li>✅ Universal: Works with both Free and Premium Spotify accounts because it doesn't rely on the official API.
  <li>✅ Lightweight: Runs as a simple script in the background.
</ul>

#
<h3>🏁 Getting Started</h3>

You can either download the pre-packaged executable for a simple setup, or run the Python script from source.

<h3>💾 Simple Install</h2>
On the <a href="https://github.com/mavvos/SpotifyGlobal/releases/latest">releases page</a>, download the SpotifyGlobal.exe file from the latest release, run the executable and you're good to go!

<h3>🐍 Manual Setup</h3>
If you prefer to run the script directly, you'll need Python 3.6 or newer.

Clone the repository:
```
git clone https://github.com/mavvos/SpotifyGlobal.git
```

Navigate into the project directory and install the required modules:

```
pip install -r requirements.txt
```

Run the script:
```
python SpotifyGlobal.py
```

#
<h3>🤔 How To Use </h3>

Using Spotify Global is straightforward, but might require a specific startup sequence for it to connect properly.

<b>Spotify must be open and active when you launch the script:</b>

1. Open the Spotify desktop application. Make sure it's visible and not minimized.

2. Run Spotify Global. A connection will be established.

3. Once connected, you can click away to other programs. Spotify will remain open in the background (but not minimized) and your global hotkeys will work!

On the first launch, a file named <b>options.txt</b> will be created in the same directory. This is where you customize your hotkeys.

#
<h3>⌨ Customizing Hotkeys</h3>

Command | Default Hotkey
:-----: | :----------:
Play / Pause | shift+5
Volume Up | shift+8
Volume Down | shift+2
Previous Track | shift+4
Next Track | shift+6
Back 5 seconds | shift+1
Forward 5 seconds | shift+3
Like / Dislike | shift+7
Quit | shift+9

To change a hotkey, open <b>options.txt</b> and edit the key combination after the = sign.

For example, to change the "Volume Down" command from the default <b><i>SHIFT+2</i></b> to <b><i>ALT+SHIFT+P</i></b>, you would edit the file like this:

<h3>Before:</h3>

```
VolDown=shift+2
```

<h3>After:</h3>

```
VolDown=alt+shift+p
```

> Note: We use the <i>keyboard</i> library for our hotkeys. Most keys are written in plain English. For a full list of valid key names, please refer to the library's list of <a href="https://github.com/boppreh/keyboard/blob/master/keyboard/_canonical_names.py?h=1">canonical names</a>, for an easy way to get your desired key, see <a href="https://github.com/boppreh/keyboard/issues/589#issuecomment-1399599739">here</a>.

#
<h3>🐜 Known Issues 🦟</h3>
<ol>
  <li><b>If Spotify is minimized, it will pop up every time a hotkey is used.</b> Workaround: Keep the Spotify window open and active (not minimized) in the background before switching to other applications.
  <li>The script may fail if another running application has "Spotify" in its window title (e.g., a web browser with this repository open). Ensure that the Spotify desktop client is the only application with that name.
  <li>Spamming hotkeys quickly can sometimes cause commands to get stuck in a loop. Workaround: Close and restart both Spotify and Spotify Global.
  <li>Some keys and hotkey combinations have more trouble than others when it comes to being registered, this is a common problem with <i>keyboard</i>.
  <li>NumPad keys may be interpreted as arrow keys (e.g., 4 is 'left', 6 is 'right'). This is a known issue with the <i>keyboard</i> library, see <a href="https://github.com/boppreh/keyboard/issues/618">Issue #618</a>.
</ol>
