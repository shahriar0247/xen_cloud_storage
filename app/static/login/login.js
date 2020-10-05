
               inputname = document.getElementsByClassName("inputname")
            textbox = document.getElementsByClassName("textbox")
            function add_hover_class(i){
                    inputname[i].classList.add("inputnamehover")
                }

            function remove_hover_class(i){
                    inputname[i].classList.remove("inputnamehover")
                }
            function TestOnTextChange(input){
                for (let i = 0; i < textbox.length ; i++){
                    if (textbox[i] == input){
                        add_hover_class(i)
                      
                    }
                }
            }
    
            for (let i = 0; i < textbox.length; i++) {
            
             
                    if (textbox[i].value == ""){
                   
                    }
                    else{
                        add_hover_class(i)
                    }
                
                textbox[i].addEventListener("mouseover",function(){
                   add_hover_class(i)
                })
                inputname[i].addEventListener("mouseover",function(){
                   add_hover_class(i)
                })

                textbox[i].addEventListener("mouseout",function(){
                    if (textbox[i].value == ""){
                    remove_hover_class(i)
                }
                })
                inputname[i].addEventListener("mouseout",function(){
                    if (textbox[i].value == ""){
                    remove_hover_class(i)}
                })
          
            }


        
