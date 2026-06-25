# Mina The Hollower

If you are reading this, you have either been invited to or are interested in helping alpha test Mina the Hollower Archipelago. This randomizer is still in ALPHA, so please play with the intention of reporting bugs and providing feedback.

- If you are unsure what is causing the issue, create an issue on the [AP World Issue Tracker](https://github.com/FyreDay/Archipelago-MinaTheHollower/issues).
- If you know the problem is with the mod itself, create an issue on the [Mod Issue Tracker](https://github.com/Axertin/mth-apclient/issues)

## Current State

The randomizer is currently believed to be completable. Below is an ever-changing list of implemented features and their current state. Please let us know how your experience goes!

Use [Universal Tracker](https://github.com/FarisTheAncient/Archipelago/releases?q=Tracker) to keep track of what you can access. There is also an in-progress map tracker built into UT that is actively being worked on.
- Ability randomization is implemented. Please test all abilities and report any bugs.
- Randomizing Burrow can make starts significantly more difficult. Be careful when enabling it, and please share any ideas for improving the experience.
- Randomizing starting items is not for the faint of heart. Good luck if you turn it on!
- Kear randomization is implemented. Please report any locks that are not removed correctly or any progression issues you encounter.
- Goaling is implemented but still needs validation.
- Location logic still has many bugs. Please report anything that UT says is inaccessible that you can reach, or anything UT says is accessible that you cannot reach.
- Combat logic has been implemented. When reporting a boss that feels too difficult, please include your attack Bone Ups, defense Bone Ups, health, vials, and currently equipped combat trinkets. [Report Combat Issues Here](https://github.com/FyreDay/Archipelago-MinaTheHollower/issues/12)

### Tracker

The [Universal Tracker](https://github.com/FarisTheAncient/Archipelago/releases?q=Tracker) Mmap tracker is currently complete for Loner's Landing, Southern Outskirts, and Eastern Hearth. Please limit map tracker feedback to these areas for now.

We would also appreciate feedback on how the map tracker is organized and whether you find it useful as development continues.

## Install Guide

Find the mod setup instructions in the [Mod Readme](https://github.com/Axertin/mth-apclient#installing--running)

- [Latest Mod Release](https://github.com/Axertin/mth-apclient/releases/latest)

- [Latest AP Morld release](https://github.com/FyreDay/Archipelago-MinaTheHollower/releases/latest)

## What does randomization do to this game?

All chests, shops, trinkets, and large Bonestones are randomized.

The goal is to defeat Giga Lionel and repair the final generator

## Options

### Start In Ossex
- Skips Loner's Landing. You can still teleport there from the pause menu.

### Kear Rando
- **Vanilla**: Universal Kears are placed in the multiworld. Any Kear Lock opened before receiving every Kear will be **OUT OF LOGIC**
- **AP Items**: Each Kear Lock is removed by a unique AP item.

### Bone Up Caps
- **Per Upgrade**: Attack, defense, and sidearm upgrades are progressively limited separately.
- **All upgrade**: A single progressive cap applies to attack, defense, and sidearm upgrades.

### Randomize Starting Items
- Takes your 15 starting items and shuffles them. This increases difficulty and can create some very cursed starts.

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