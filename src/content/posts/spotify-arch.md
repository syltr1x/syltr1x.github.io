---
title: Spotify para Arch
description: Tutorial para instalar spotify y configurarlo con spicetify en Arch-Linux
date: 04/03/2024
tags: ["Tutorial", "Spotify", "Arch"]
---
<p class="mb-[-1rem] mt-5">Instala yay y luego lo usa para instalar spotify</p>

```bash
sudo git clone https://aur.archlinux.org/yay-git.git/ /opt/				
sudo chown $USER:$USER /opt/yay-git
cd /opt/yay-git
makepkg -si
yay -S spotify
```
❗ Ahora deberias iniciar sesión en Spotify, luego cierralo y continuemos

<p class="mb-[-1rem] mt-5">Para evitar problemas al instalar spicetify cambiaremos los permisos de la instalación de spotify</p>

```bash
sudo chmod a+rw /opt/spotify/Apps
sudo chmod a+rw /opt/spotify/Apps/*
sudo chown -R $USER:$USER /opt/spotify
curl -fsSL https://raw.githubusercontent.com/spicetify/cli/main/install.sh | sh
```


Ahora podras de dejar de ser un pesado con tu "_fastfetch_" y comenzar a ser un pesado con tu spotify-TUI based, **ahora puedes ser un "hacker" sin saber ocupar una terminal**, bien por ti
