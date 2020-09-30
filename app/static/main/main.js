filepicker = document.getElementById('file-picker')
uploadform = document.getElementById('upload-form')
document.getElementById('uploadbtn').addEventListener('click', function () {
    filepicker.click()
})
document.getElementById('uploadbtn2').addEventListener('click', function () {
    filepicker.click()
})


filepicker.onchange = function () {
    uploadform.submit()
};

document.getElementById('download-btn').addEventListener('click', function () {
    document.getElementById('download_submit').click()
})

body = document.getElementsByTagName('body')[0]
menu = document.getElementsByClassName('context-menu')[0]

body.addEventListener('contextmenu', function (ev) {
    ev.preventDefault();

    menu.style.display = 'block'
    menu.style.left = ev.pageX + 'px'
    menu.style.top = ev.pageY + 'px'

    if (filename3 == '[object HTMLParagraphElement]') {
        delete1.style.display = 'none'
    }
    else {
        delete1.style.display = 'block'
    }


    return false;
}, false);

document.addEventListener('click', function () {
    clicking()
    nocont()
})

menu1 = document.getElementById('menu1')
new_folder = document.getElementById('new-folder')

htmltopython = document.getElementById('htmltopython')
new_folder.addEventListener('click', function () {
    htmltopython.value = 'new-folder'
    menu1.style.display = 'block'
    document.getElementById('menu1btn1').innerText = 'Create Folder'
    document.getElementById('menu1h2').innerText = 'Create a new folder'
    document.getElementById('menu1p').innerText = 'Type the name of the folder you want to create and press on \'Create folder\''
    document.getElementById('menu1text1').innerText = 'Folder name'
    document.getElementById('menu1btn1').style.display = 'block'
    document.getElementById('menu1cancel').style.display = 'block'
    document.getElementById('menu1text2').style.display = 'block'



    nocont()
})


menu1cancel = document.getElementById('menu1cancel')
menu1cancel.addEventListener('click', function () {
    menu1.style.display = 'none'
})


delete1 = document.getElementById('delete');



delete1.addEventListener('click', function () {
    htmltopython.value = 'delete%20,,@#' + filename3;
    console.log(htmltopython.value)


    menu1.style.display = 'block';
    document.getElementById('menu1h2').innerText = 'Delete folder \'' + filename3 + '\'';
    document.getElementById('menu1btn1').innerText = 'Delete Folder';
    document.getElementById('menu1p').innerText = 'Are you sure you want to delete the folder?';
    document.getElementById('menu1btn1').style.display = 'block';
    document.getElementById('menu1cancel').style.display = 'block';
    nocont()
})

document.getElementById('menu1btn1').addEventListener('click', function () {
    document.getElementById('actionsubmit').click()
})

new_file = document.getElementById('new-file')


new_file.addEventListener('click', function () {

})

function nocont() {
    menu = document.getElementsByClassName('context-menu')[0]
    menu.style.display = 'none'
}


function setgrid(num) {

    folders = document.getElementsByClassName("folders")[0]
    folders.classList.remove("foldersall")
    folders.classList.remove("folders1")
    folders.classList.remove("folders2")
    folders.classList.remove("folders3")
    folders.classList.remove("folders4")
    folders.classList.remove("folders5")
    if (num == "auto") {
        folders.classList.add("foldersall")
    }

    else {
        folders.classList.add("folders" + num)
    }
}