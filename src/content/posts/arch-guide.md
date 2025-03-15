---
title: Instalación de Arch Linux
description: Un "paso a paso" para instalar Arch Linux de forma manual y basica, sin Desktop Enviroment ni Windows Manager
date: 10/12/2024
tags: ["Arch", "Tutorial", "Linux"]
---
<p class="mb-8">Si bien las cosas se simplificaron con 'arch-install' es importante saber hacer la instalación manual en caso de ser necesario</p>
<h1 id="instalacion" class="mt-12 text-2xl font-bold">1- Crearemos un USB "booteable" para instalar Arch Linux</h1>
<p class="mb-5">Puedes encontrar la iso de la ultima version de Arch <a class="hover:text-blue-400 underline decoration-wavy" href="https://geo.mirror.pkgbuild.com/iso/" target="_blank">aquí</a>
<p class="mb-5">Una vez descargada usaremos <a class="hover:text-blue-400 underline decoration-wavy" href="https://etcher.balena.io/#download-etcher" target="_blank">Balena Etcher</a> para crear un USB "booteable"</p>
<p>O si eres un usuario (medio/avanzado) de Linux puedes hacerlo con el siguiente comando</p>
<p>el id_del_usb lo puedes ver con el comando lsblk y el tamaño_de_buffer puedes calcularlo siendo 4M por cada 1GB de RAM que tengas. Ej: 128M en 32GB</p>

```bash
sudo dd if={nombre_del_archivo} of={id_del_usb} bs={tamaño_de_buffer} status=progress
```
Ejemplo:
```bash
sudo dd if=archlinux-x86_64.iso of=/dev/sdd bs=128M status=progress
```
<h2 id="wifi" class="mt-12 text-2xl font-bold">2- Ahora configuraremos el Wifi, si tienes conexión cableada ve al <a class="opacity-80 hover:text-blue-400" href="#discos">paso 3</a></h2>

```bash
loadkeys es #A menos que quieras usar el teclado inglés
```
```bash
iwctl # Para poder conectarte a internet
```
```bash
device list # Mostrara las interfaces disponibles
station {tu_interfaz} get-networks # Mostrara las redes disponibles 
station {tu_interfaz} connect {tu_red} #para conectarte a tu red (luego te pedira la contraseña)
```
<h3 id="discos" class="mt-12 text-2xl font-bold">3- Esta es una parte vital, intenta hacerla bien</h3>
En mi caso reconozco que el disco en el que quiero instalar es el sdc ya que es de 240GB (238.5G según lo que vemos)

```bash
lsblk
# output 👇
#NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
#sda      8:0    0 465.8G  0 disk 
#├─sda1   8:1    0   100M  0 part 
#├─sda2   8:2    0    16M  0 part 
#└─sda3   8:3    0 465.6G  0 part 
#sdb      8:16   0 465.8G  0 disk 
#└─sdb1   8:17   0 465.8G  0 part 
#sdc      8:32   0 238.5G  0 disk 
#├─sdc1   8:33   0   500M  0 part 
#└─sdc2   8:34   0   238G  0 part 
cfdisk /dev/sdc # En mi caso, que mi disco es el sdc
```
Es necesario que crees dos particiones. Una de 500MB y otra del espacio que quieras para tu sistema (min 20GB)
<h4 id="formato" class="mt-12 text-2xl font-bold">4- Si haz hecho todo bien, vamos a formatear los discos para poder continuar</h4>

Para poder utilizar las particiones que creamos le daremos un formato y las "montaremos".
```bash
mkfs.ext4 /dev/sdc2 # En mi caso es la particion de sistema
mkfs.fat -F 32 /dev/sdc1 # En mi caso es la particion de 500MB
# Ahora las montamos
mount /dev/sdc2 /mnt
mkdir /mnt/boot
mount /dev/sdc1 /mnt/boot
```
Ahora vamos a instalar algunos paquetes necesarios e indicarle al sistema que monte automaticamente estas particiones
```bash
pacstrap /mnt base base-devel linux linux-firmware vim
genfstab -U /mnt >> /mnt/etc/fstab
# Iniciamos arch   🥁
arch-chroot /mnt
```
<h5 id="grub" class="mt-12 text-2xl font-bold">5- Si ya llegaste hasta acá no lo arruinemos ahora</h5>

```bash
pacman -S grub efibootmgr networkmanager # Con esto instalamos lo necesario para arrancar el sistema y gestionar el wifi
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```
<h6 id="final" class="mt-12 text-2xl font-bold">6- Ahora solo configuraremos unas cosas y listo</h6>

```bash
passwd # Esto para configurar la contraseña de administrador (root)
useradd -m -G wheel -s /bin/bash tuusuario
passwd tuusuario # Con esto creareas la contraseña para tu usuario
```
Recomiendo que hagas lo siguiente para poder instalar paquetes y ejecutar comandos como administrador desde tu usuario.
```bash
sed -i 's/# %wheel ALL=(ALL) ALL/%wheel ALL=(ALL) ALL/' /etc/sudoers
systemctl enable NetworkManager # Iniciara el servicio para conectarnos a la red cada vez que inicie sesion
```
Bueno, eso es todo
```bash
exit
umount -R /mnt
reboot # Despues de esto desconecta el USB
```

<div class="absolute right-4 top-20 fixed flex-col hidden lg:flex">
<p class="text-lg underline">Tabla de contenidos</p>
<a class="opacity-70 hover:text-blue-400 duration-100" href="#instalacion">1. Creacion del medio de instalación</a>
<a class="opacity-70 hover:text-blue-400 duration-100" href="#wifi">2. Conexión a internet</a>
<a class="opacity-70 hover:text-blue-400 duration-100" href="#discos">3. Particionado de disco</a>
<a class="opacity-70 hover:text-blue-400 duration-100" href="#formato">4. Formateo de particiones</a>
<a class="opacity-70 hover:text-blue-400 duration-100" href="#grub">5. Configuración de arranque</a>
<a class="opacity-70 hover:text-blue-400 duration-100" href="#final">6. Retoques finales</a>
</div>
