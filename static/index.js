function pegar()
{
        const ul = document.getElementById("ul");
        if(ul.classList.contains("ocultar"))
        {
                var aparecer = document.querySelector(".fases");
                aparecer.classList.remove("ocultar"); 
        }
        else
        {
                var aparecer = document.querySelector(".fases");
                aparecer.classList.add("ocultar");
        }
              
}