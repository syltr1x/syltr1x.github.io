---
title: Instalación de GstarCAD
description: Como instalar y hacer un bypass para GstarCAD
date: 23/05/2025
tags: ["Linux", "CAD", "Crack"]
---
<h1 class="text-xl mb-5">GstarCAD es planteado como una alternativa a AutoCAD</h1> 

<div class="flex place-content-around">
    <a 
        class="bg-[#6e0001] rounded-lg px-3 py-2 flex gap-x-2 items-center hover:bg-[#9e0001] hover:shadow-[0_0_20px_#f008]"
        href="https://drive.usercontent.google.com/download?id=1Fr6Iv6CST_aLB9GvP7zy08LyTyA2fzpO&export=download&authuser=0"
        target="_blank">
        <svg class="size-6" fill=currentColor xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M5,20H19V18H5M19,9H15V3H9V9H5L12,16L19,9Z" /></svg>
        Descargar .deb</a>
    <a 
        class="bg-[#6e0001] rounded-lg px-3 py-2 flex gap-x-2 items-center hover:bg-[#9e0001] hover:shadow-[0_0_20px_#f008]"
        href="https://drive.usercontent.google.com/download?id=1vUUKY6_gTHFqG78Hnis_PlHtT173dd4g&export=download&authuser=0"
        target="_blank">
        <svg class="size-6" fill=currentColor xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M5,20H19V18H5M19,9H15V3H9V9H5L12,16L19,9Z" /></svg>
        Descargar .pkg.tar.zst</a>
</div>

El único problema es que no es gratis, pero ofrece una version de prueba por 30 días.
El conteo de días lo almacena en local, por lo tanto podemos eliminar este registro y "reiniciar el contador" cuantas veces queramos con los siguientes comandos

Linux y MacOS
```bash
find / \( -type f -o -type d \) -name "*gstar*" -exec rm -rf {} + 2/dev/null
```

Windows
```bash
Get-ChildItem -Path C:\ -Recurse -Filter "*gcad*" -File | Remove-Item -Force
Get-ChildItem -Path C:\ -Recurse -Filter "*gcad*" | Remove-Item -Force -Recurse
```
