# Mina The Hollower
## State of the Implementaion
The Archipelago Mod and AP World are currently fairly stable. As a late alpha, we are primarily looking for help finding logic bugs and reporting any issues with the mod.
- The mod breaks whenever any game update comes out. Wait for a new mod release to play.
- If you find a logic bug or are unsure what is causing the issue, create an issue on the [AP World Issue Tracker](https://github.com/FyreDay/Archipelago-MinaTheHollower/issues).
- If you know the problem is with the mod itself, create an issue on the [Mod Issue Tracker](https://github.com/Axertin/mth-apclient/issues)

## What does randomization do to this game?

In the Archipelago Randomizer, all trinkets, player upgrades, underlab improvements, and train tickets. Every chest, trinket, bonestone, and shop are locations.

Ability Shuffling is by default on and is the main way we gate checks in this open world game, with the option to shuffle certain abilities (Burrow, Swim, Climb, Carry, Bounce, Spring),
preventing them from being used until found. Burrow is by default not shuffled. Shuffle Burrow if you want a challenge.

Enemy randomization is an option in the ingame modifiers if you want to randomize them. (but not taken into account in the ap world)
Feel free to enable/disable modifiers at will. The AP world assumes you can teleport to Ossex and the Shipwreck at any time

## What are the goals of Mina the Hollower Archipelago?
- Defeat Giga Lionel and repair the final generator
- Repair a target number of generators


## Is there a tracker pack?
There is a map tracker built for Universal Tracker (UT) built into the Mina the Hollower AP world. To use it, install the [Universal Tracker](https://github.com/FarisTheAncient/Archipelago/releases?q=Tracker) tracker.apworld and use it as your text client.

There is also support for additional commands You can use ```/explain Max Jump``` To see what AP thinks your best trinket combo is at the moment and ```/explain Generators``` to see which generators are on and which ones you can repair with your items

We would also appreciate feedback on how the map tracker is organized and whether you find it useful.

## Installing

Download the mod and the AP world. The mod will be a zip file with your OS name
- [Latest Mod Release](https://github.com/Axertin/mth-apclient/releases/latest)

- [Latest AP World release](https://github.com/FyreDay/Archipelago-MinaTheHollower/releases/latest)

### Switch to the Experimental Modding Beta
 The mod requires a Steam copy of Mina the Hollower on the **experimental-modding Beta** It also requires 
 `-mod -mod-allow-code` launch options set (this enables loading a mod's code library).

If you have never done this before, 
1. navigate to Steam->Mina The Hollower->Properties->Game Versions & Betas
2. Select `experimental-modding` in the version list

### Windows

Unzip the mod.zip (containing a `apclient` folder with a `mod.dll` and `mod.yc`) inside into:

```
%APPDATA%\Yacht Club Games\Mina the Hollower\mods
```
so that the .dll and .yc files are in
```
%APPDATA%\Yacht Club Games\Mina the Hollower\mods\apclient\
```

Set Steam launch options for Mina the Hollower:

```
-mod -mod-allow-code
```

The game's mod loader writes `%APPDATA%\Yacht Club Games\Mina the Hollower\mod.log` each run;
the mod's own runtime log is `%LOCALAPPDATA%\mth-apclient\mthap_*.log`.

### Linux

The mod is installed into Mina The Hollower's save directory (the SDL prefix path), not the install dir.

Unzip the mod.zip (containing a `apclient` folder with a `mod.so` and `mod.yc`) inside into:, 

```
~/.local/share/Yacht Club Games/Mina the Hollower/mods
```
so that the .dll and .yc files are in
```
~/.local/share/Yacht Club Games/Mina the Hollower/mods/apclient/
```
Set Steam launch options for Mina the Hollower:

```
-mod -mod-allow-code
```

The game's mod loader writes `~/.local/share/Yacht Club Games/Mina the Hollower/mod.log` each
run (whether a mod loaded, version-check or load failures) - check it first if the mod doesn't
appear. The mod's own runtime log is `~/.local/share/mth-apclient/mthap_*.log` (one file per run).

## Running
An ImGui overlay window should appear allowing connection and disconnection to an AP server. If it
doesn't appear or you want to hide it once connected, it can be toggled by pressing `F2`.

1. Connect to AP immediately on game launch
2. Create a new save or load into a save already played on with this slot

# Warnings

**NEVER CREATE A SAVE AND THEN CONNECT**

**NEVER COPY A SAVE AND PLAY THAT SAVE IN AP**

**NEVER LOAD INTO A SAVE AND THEN CONNECT**

**NEVER LOAD INTO A VANILLA SAVE YOU DONT WANT MODIFIED**

There is also a console you can access by presssing **F1**. type ```help``` to see commands

## Options

### Start In Ossex
- Skips Loner's Landing. You can still teleport there from the pause menu.

### Kear Rando
- **Vanilla**: Universal Kears are placed in the multiworld. Any Kear Lock opened before receiving every Kear will be **OUT OF LOGIC**
- **AP Items**: Each Kear Lock is removed by a unique AP item.

### Bone Up Caps
- **Per Upgrade**: Attack, defense, and sidearm upgrades are progressively limited separately.
- **All upgrade**: A single progressive cap applies to attack, defense, and sidearm upgrades.

### Maximum Stat Caps
- Select what your max level for your stats will be

### Randomize Starting Items
- Takes your 15 starting items and shuffles them. This increases difficulty and can cause some funny starts.

### Ability Rando
- Allows you to select which abilities become items from the list below. Burrow is disabled by default because it significantly limits your starting options.

**Burrow** - The ability to burrow. You will still be able to enter Underlabs, go into geysers, and go into pipes.

**Swim** - The ability to swim (burrow in deep water).

**Climb** - The ability to climb ropes.

**Bounce** - The ability to bounce on bounce plants and springboards.

**Spring** - The ability to be launched by springboards.

**Carry** - The ability to carry objects.

### Deathlink
- Sends a DeathLink every time you die.

(Planned change: only sparkless deaths will trigger DeathLink in the future.)
