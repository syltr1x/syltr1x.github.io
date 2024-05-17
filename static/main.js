function show_info() {
    console.log("Mostrando")
}
function download(url) {
    window.open(url, "_blank")
}
function hook_item(id) {
    let hooked_item= document.getElementById(id);
    hooked_item.style.animation = 'remark 0.8s linear'
    setTimeout(() => {
    hooked_item.style.animation = ''
    }, 900)
    window.location.href = `#${id}`
}
show_info()