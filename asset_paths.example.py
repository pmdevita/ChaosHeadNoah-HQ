from pathlib import Path

# Paths to game assets to be used in scripts

# Base paths
# Extracted Xbox ISO
xbox_base = Path(r"C:\Chaos;Head Noah")
# Steam CHAOS;HEAD NOAH/Data folder
steam_base = Path(r"C:\Program Files (x86)\Steam\steamapps\common\CHAOS;HEAD NOAH\Data")
# Path to Yuzu dump romfs folder
switch_base = Path(r"C:\Users\username\AppData\Roaming\yuzu\dump\0100C17017CBC000\romfs")
# Shared Output Assets (this was synced between collaborators with Resilio Sync)
assets_base = Path(r"C:\CHNoahAssets")

# Extracted Steam archives
steam_bgm = steam_base / "bgm"

# Extracted Xbox archives
xbox_bgm = xbox_base / "bgm"
xbox_bg = xbox_base / "cg" / "bg"
xbox_mv1 = xbox_base / "dx1"
xbox_mv2 = xbox_base / "dx2"

# Switch romfs folders
switch_bgm = switch_base / "bgm"
switch_mv = switch_base / "movie"
