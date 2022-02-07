# Iniciaremos então o ajax com Javascript no sentido de realizar o filtro sem o refresh de página:

(function(win,doc){
    'use strict';

    doc.querySelector('#country').addEventListener('change',async(event)=>{
        event.preventDefault();
        let req=await fetch('http://localhost:8000/countryFilter/',{
            method:'POST',
            headers:{
                'Accept':'application/json',
                'Content-Type':'application/json',
                'X-CSRFToken':doc.querySelectorAll('input')[0].value
            },
            body:JSON.stringify({
                'country':doc.querySelector('#country').value
            })
        });
        let res=await req.json();
        doc.querySelector('.result').innerHTML=res.data;
    },false);

})(window,document);

