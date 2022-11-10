



console.log('hello word')

const DataForm= new FormData();
DataForm.append('username' , 'anotherUser')
DataForm.append('email' , 'user@gmail.com')
DataForm.append('password' , 'chamali123@')

const submiting = async ()=> {
await axios ({
    method : 'post' ,
    url : 'http://127.0.0.1:8000/log/singin/' ,
    data : DataForm
})
.then((response)=>{
    console.log(response.data) ;

}) .catch(function (error) {
    console.log(error)
  });


}

const login = async ()=> {
    await axios ({
        method : 'post' ,
        url : 'http://127.0.0.1:8000/log/in/' ,
        data : DataForm
    })
    .then((response)=>{
        console.log(response.data) ;
    
    }) .catch(function (error) {
        console.log(error)
      });
    
    
    }


    const changePassword = async ()=> {
        
        await axios ({
            method : 'post' ,
            url : 'http://127.0.0.1:8000/log/changepassword/' ,
            data : DataForm
        })
        .then((response)=>{
            console.log(response.data) ;
        
        }) .catch(function (error) {
            console.log(error)
          });
        
        
        }

        const craetmc = async ()=> {
            let gettingData= new FormData();
            gettingData.append('name',document.getElementById('name').value)
            gettingData.append('why',document.getElementById('name2').value)
            gettingData.append('how',document.getElementById('name3').value)
            gettingData.append('what',document.getElementById('name4').value)
            gettingData.append('vision',document.getElementById('5').value)
            gettingData.append('picture',document.getElementById('picture').files[0])
            console.log(document.getElementById('picture').files[0])
            await axios ({
                method : 'post' ,
                url : 'http://127.0.0.1:8000/mc_info/create/' ,
                data : gettingData
            })
            .then((response)=>{
                console.log(response.data) ;
            
            }) .catch(function (error) {
                console.log(error)
              });
            
        }