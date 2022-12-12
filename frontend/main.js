



console.log('hello word')


let getData = async () => {
    let parent = document.getElementById('droplist')
    let respons = await fetch ('http://127.0.0.1:8000/mc_info/team_members/create/')
    let data = await respons.json()
    console.log(data)
    data.map((ob,i)=>{
        let li = document.createElement('option');
        li.value = ob.id 
        li.textContent = ob.name
        parent.appendChild(li)
    })
}
getData();





// push to sign in 


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
                url : 'https://aieseclandingpage.herokuapp.com/mc_info/create/' ,
                data : dataC
            })  
            .then((response)=>{
                console.log(response.data) ;            
            }) .catch(function (error) {
                console.log(error)
              });
            }

            const addMCMember = async ()=> {
                const dataC =  new FormData();
                dataC.append( 'name' , document.getElementById('addMcMemberName').value)
                dataC.append( 'parent' , document.getElementById('droplist').value)
                dataC.append( 'whatsapp' , document.getElementById('whatsapp').value)
                dataC.append( 'insta' , document.getElementById('instagram').value)
                dataC.append( 'linkedin' , document.getElementById('linkedin').value)
                dataC.append( 'picture' , document.getElementById('MCPicture').files[0])
                dataC.append( 'facebook' , document.getElementById('facebook').value)
                dataC.append( 'deparment' , document.getElementById('addMcMemberdeparment').value)
                await axios ({
                    method : 'post' ,
                    url : 'https://aieseclandingpage.herokuapp.com/team_members/create/' ,
                    data : dataC
                })  
                .then((response)=>{
                    console.log(response.data) ;            
                }) .catch(function (error) {
                    console.log(error)
                  });
                }
            

                const AddEvent = async ()=> {
                    let tm = document.getElementById('eventdate').value
                    let arr = tm.split('/')
                    let TheDay = arr[1]+'/'+arr[0]+'/'+arr[2]
                    const dataC =  new FormData();
                    dataC.append( 'name' , document.getElementById('EventName').value)
                    dataC.append( 'address' , document.getElementById('EventVenue').value)
                    dataC.append( 'maps' , document.getElementById('eventVenLink').value)
                   
                    dataC.append( 'date' , tm )
                    dataC.append( 'form' , document.getElementById('eventform').value)
                    dataC.append( 'time' , document.getElementById('eventTime').value)
                   
                    dataC.append( 'AIESECER' , document.getElementById('eventIfAiesecer').value)

                    dataC.append( 'link_page' , document.getElementById('eventLinkPage').value)
                    dataC.append( 'eventlimited_places_OR_nonlimited' , false)
                   
                    dataC.append( 'event_city_name' , document.getElementById('event_city_name').value)
                    dataC.append( 'event_description' , document.getElementById('event_description').value)
                    dataC.append( 'eventPic' , document.getElementById('eventPic').value)
                    console.log(TheDay)
                    await axios ({
                        method : 'post' ,
                        url : 'https://aieseclandingpage.herokuapp.com/event/insert/' ,
                        data : dataC
                    })
                    .then((response)=>{
                        console.log(response.data) ;
                    
                    }) .catch(function (error) {
                        console.log(error)
                      });
                    }       

        const AddQestion_Answer = async ()=> {
            const dataC =  new FormData();
            dataC.append( 'question' , document.getElementById('question').value)
            dataC.append( 'Answer' , document.getElementById('Answer').value)

            
            await axios ({
                method : 'post' ,
                url : 'https://aieseclandingpage.herokuapp.com/question_answer/insert/' ,
                data : dataC
            })
            .then((response)=>{
                console.log(response.data) ;
            
            }) .catch(function (error) {
                console.log(error)
                });
            }

            const AddForm = async ()=> {
                const dataC =  new FormData();
                dataC.append( 'joinAIESC' , document.getElementById('joinAIESC').value)
                dataC.append( 'beApartner' , document.getElementById('beApartner').value)
                dataC.append( 'EP' , document.getElementById('EP').value)
    
                
                await axios ({
                    method : 'post' ,
                    url : 'https://aieseclandingpage.herokuapp.com/form/insert/' ,
                    data : dataC
                })
                .then((response)=>{
                    console.log(response.data) ;
                
                }) .catch(function (error) {
                    console.log(error)
                    });
                }

    
        // https://aieseclandingpage.herokuapp.com/mc_info/team_members/create/