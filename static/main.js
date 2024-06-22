function show_info() {
    console.log("Mostrando")
}
function download(url) {
    window.open(url, "_blank")
}
function hook_item(id) {
    let hooked_item = document.getElementById(id);
    hooked_item.style.animation = 'remark 0.8s linear'
    setTimeout(() => {
    hooked_item.style.animation = ''
    }, 900)
    window.location.href = `#${id}`
}
show_info()
const tabContainers = document.querySelectorAll('.tab-container');

tabContainers.forEach(container => {
    const tabs = container.querySelectorAll('.tab');
    const contents = container.querySelectorAll('.tab-content');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            contents.forEach(c => c.classList.remove('active'));
            container.querySelector(`#${tab.getAttribute('data-tab')}`).classList.add('active');
        });
    });
});
