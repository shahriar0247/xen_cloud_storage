
inputname = document.getElementsByClassName("inputname")
textbox = document.getElementsByClassName("textbox")
function add_hover_class(i) {
   
    inputname[i].classList.add("inputnamehover")
}

function remove_hover_class(i) {
    inputname[i].classList.remove("inputnamehover")
}
function TestOnTextChange(input) {
    for (let i = 0; i < textbox.length; i++) {
        if (textbox[i] == input) {
            add_hover_class(i)

        }
    }
}
var hoveron = [false, false]
var focuson = [false, false]

for (let i = 0; i < textbox.length; i++) {


    if (textbox[i].value == "") {
        remove_hover_class(i)
    }
    else {
        add_hover_class(i)
    }
    
    textbox[i].addEventListener("mouseover", function () {
        
        hoveron[i] = true 
      
    })
    inputname[i].addEventListener("mouseover", function () {
        (hoveron[i] = true) 
    })

    textbox[i].addEventListener("mouseout", function () {
     
            (hoveron[i] = false) 
        
    })
    inputname[i].addEventListener("mouseout", function () {
     
            (hoveron[i] = false) 
        
    })
    textbox[i].addEventListener("focus", function () {
        
        focuson[i] = true 
      
    })
    inputname[i].addEventListener("focus", function () {
        (focuson[i] = true) 
    })

    textbox[i].addEventListener("blur", function () {
     
            (focuson[i] = false) 
        
    })
    inputname[i].addEventListener("blur", function () {
     
            (focuson[i] = false) 
        
    })

}

function if_text_in_input() {
    for (let i = 0; i < textbox.length; i++) {
        
    if (hoveron[i] == true){
        add_hover_class(i)
    }

    if (focuson[i] == true){
        add_hover_class(i)
    }
    if (textbox[i].value != "")
    {
        add_hover_class(i)
    }
    if (hoveron[i] == false && textbox[i].value == false && focuson[i] == false)
{
    remove_hover_class(i)
}
    }
}

function async_loop() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve('resolved');
        }, 100);
    });
}

async function asyncCall() {

    while (true) {
        const result = await async_loop();
        if_text_in_input()
        console.log("lol")
    }

}

asyncCall();



