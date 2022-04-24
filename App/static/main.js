
async function getUserData(){
    const response = await fetch('/api/users');
    return response.json();
}

function loadTable(users){
    const table = document.querySelector('#result');
    for(let user of users){
        table.innerHTML += `<tr>
            <td>${user.id}</td>
            <td>${user.username}</td>
        </tr>`;
    }
}

async function main(){
    const users = await getUserData();
    loadTable(users);
}
async function signup(event){
    event.preventDefault();

    let form = event.target;
    let fields = event.target.elements;

    let data = {
     first_name: fields['first_name'].value,
     last_name: fields['last_name'].value,
     graduation_year: fields['graduation_year'].value,
     programme: fields['programme'].value,
     department: fields['department'].value,
     faculty: fields['faculty'].value,
     job: fields['job'].value,
     email: fields['email'].value,
     Uname: fields['Uname'].value,
     password: fields['password'].value
    }
     form.reset();
  
      let result = await sendRequest(`${server}/signup`, 'POST', data);

    if('error' in result){
      toast("Login Failed: "+result['error']);
    }else{
      toast("Logged Successful");
      window.location.href= 'index.html';
   }
  }
  //attach signup to submit event of form
    document.forms['signUpForm'].addEventListener('submit', signup);

    function logout(){
        window.localStorage.removeItem('access_token');
        window.location.href ="login.html";
      }

main();