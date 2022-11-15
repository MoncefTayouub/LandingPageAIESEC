



console.log('hello word')

const DataForm= new FormData();
DataForm.append('username' , 'anotherUser')
DataForm.append('email' , 'user@gmail.com')
DataForm.append('password' , 'chamali123@')

const submiting = async ()=> {
    const dataF =  new FormData();
    dataF.append( 'username' , document.getElementById('signName').value)
    dataF.append( 'email' , document.getElementById('signEmail').value)
    dataF.append( 'password' , document.getElementById('signPassword').value)
 

    await axios ({
        method : 'post' ,
        url : 'https://aieseclandingpage.herokuapp.com/log/singin/' ,
        data : dataF
    })
    .then((response)=>{
        console.log(response.data) ;

    }) .catch(function (error) {
        console.log(error)
    });
}

const login = async ()=> {
    const dataL =  new FormData();
    dataL.append( 'username' , document.getElementById('loginName').value)
    dataL.append( 'password' , document.getElementById('loginPassword').value)
 
    await axios ({
        method : 'post' ,
        url : 'https://aieseclandingpage.herokuapp.com/log/in/' ,
        data : dataL
    })
    .then((response)=>{
        console.log(response.data) ;
    
    }) .catch(function (error) {
        console.log(error)
      });
    
    
    }


    const changePassword = async ()=> {
        const dataC =  new FormData();
        dataC.append( 'name' , document.getElementById('changeName').value)
        dataC.append( 'password' , document.getElementById('changePassword').value)
    
        await axios ({
            method : 'post' ,
            url : 'https://aieseclandingpage.herokuapp.com/log/changepassword/' ,
            data : dataC
        })
        .then((response)=>{
            console.log(response.data) ;
        
        }) .catch(function (error) {
            console.log(error)
          });
        
        
        }

        const testConnection = async ()=> {
            console.log('pushing')
            
            await axios ({
                method : 'post' ,
                url : 'https://aieseclandingpage.herokuapp.com/' ,
                data : DataForm
            })
            .then((response)=>{
                console.log(response.data) ;
            
            }) .catch(function (error) {
                console.log(error)
              });
            }
        // https://aieseclandingpage.herokuapp.com/mc_info/team_members/create/