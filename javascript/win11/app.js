let taskbar = document.getElementsByClassName("taskbar")[0]
let startmenu = document.getElementsByClassName("startmenu")[0]
let icons = document.getElementsByClassName("icons")
console.log("working")

taskbar.addEventListener('click' , () => {
    console.log("working")

    if (startmenu.style.bottom == "50px"){
        startmenu.style.bottom = "-650px"
    }else{
        startmenu.style.bottom = "50px"
    }
})