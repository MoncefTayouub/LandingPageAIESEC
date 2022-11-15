



console.log('hello word')


let getData = async () => {
    let parent = document.getElementById('droplist')
    let respons = await fetch ('https://aieseclandingpage.herokuapp.com/mc_info/team_members/create/')
    let data = await respons.json()
    data.map((ob,i)=>{
        let li = document.createElement('option');
        li.value = ob.id 
        li.textContent = ob.name
        parent.appendChild(li)
    })
}
getData();






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

        const AddMc = async ()=> {
            const dataF =  new FormData();
            dataF.append( 'name' , document.getElementById('addMcMemberName').value)
            dataF.append( 'parent' , document.getElementById('droplist').value)
            dataF.append( 'picture' , document.getElementById('AddPicture').files[0])
            dataF.append( 'whatsapp' , document.getElementById('whatsapp').value)
            dataF.append( 'instagram' , document.getElementById('instagram').value)
            dataF.append( 'linkedin' , document.getElementById('linkedin').value)
            dataF.append( 'facebook' , document.getElementById('facebook').value)
            dataF.append( 'deparment' , document.getElementById('addMcMemberdeparment').value)
            // await axios ({
            //     method : 'post' ,
            //     url : 'http://127.0.0.1:8000/mc_info/create/' ,
            //     data : dataF
            // })  
            // .then((response)=>{
            //     console.log(response.data) ;            
            // }) .catch(function (error) {
            //     console.log(error)
            //   });
            }

            const addMCMember = async ()=> {
                const dataC =  new FormData();
                dataC.append( 'name' , document.getElementById('addMcName').value)
                dataC.append( 'why' , document.getElementById('addwhy').value)
                dataC.append( 'how' , document.getElementById('addhow').value)
                dataC.append( 'what' , document.getElementById('AddWhat').value)
                dataC.append( 'vision' , document.getElementById('AddVision').value)
                dataC.append( 'picture' , document.getElementById('AddPicture').files[0])
                dataC.append( 'Date' , document.getElementById('addDate').value)
                await axios ({
                    method : 'post' ,
                    url : 'http://127.0.0.1:8000/mc_info/create/' ,
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