---
title: GTFO SUID bins
description: Explicacion de binarios con vulnerabilidad SUID y un script que automatiza la detección
date: 05/03/2024
tags: ["Linux", "Hacking", "Script"]
---
### Paso a comentarles de algo nuevo que vi y de un script que hice para probarlo
[ _ ] Falta la desc

### Puedes probarlo en tu sistem ejecutando este comando:
```bash
curl -sS https://raw.githubusercontent.com/syltr1x/mythings/main/suidscanner.sh | sh
```

### Si no te fias este es el codigo que se ejecutara y lo puedes ver en github
```bash
opt=()
while IFS=read -r line; do
	opt+=("$(basename "$line")")
done < <(find / -perm -4000 2>/dev/null)
while IFS=red -r line; do
	filter=$(echo "$line" | cut -d ' ' -f 1)
	line=$(echo "$line" | sed 's/[[:space:]]*$//')
	for elemento in "${opt[@]}"; do
		if [[ "$elemento" == "$filter" ]]
			echo "$line"
		fi
	done
done < <(curl -sS https://raw.githubusercontent.com/syltr1x/mythings/main/sudo_gtfo_bins)
```
<a href="https://github.com/syltr1x/mythings/blob/main/suidscanner.sh" target="_blank" class="mt-[-10px] flex items-center place-self-end gap-x-2 text-xs opacity-80 hover:text-blue-400">
<svg class="size-4" viewBox="0 0 128 128">
    <path fill=currentColor d="M64 5.103c-33.347 0-60.388 27.035-60.388 60.388 0 26.682 17.303 49.317 41.297 57.303 3.017.56 4.125-1.31 4.125-2.905 0-1.44-.056-6.197-.082-11.243-16.8 3.653-20.345-7.125-20.345-7.125-2.747-6.98-6.705-8.836-6.705-8.836-5.48-3.748.413-3.67.413-3.67 6.063.425 9.257 6.223 9.257 6.223 5.386 9.23 14.127 6.562 17.573 5.02.542-3.903 2.107-6.568 3.834-8.076-13.413-1.525-27.514-6.704-27.514-29.843 0-6.593 2.36-11.98 6.223-16.21-.628-1.52-2.695-7.662.584-15.98 0 0 5.07-1.623 16.61 6.19C53.7 35 58.867 34.327 64 34.304c5.13.023 10.3.694 15.127 2.033 11.526-7.813 16.59-6.19 16.59-6.19 3.287 8.317 1.22 14.46.593 15.98 3.872 4.23 6.215 9.617 6.215 16.21 0 23.194-14.127 28.3-27.574 29.796 2.167 1.874 4.097 5.55 4.097 11.183 0 8.08-.07 14.583-.07 16.572 0 1.607 1.088 3.49 4.148 2.897 23.98-7.994 41.263-30.622 41.263-57.294C124.388 32.14 97.35 5.104 64 5.104z"></path>
</svg>
    revisa el codigo aquí
</a>
