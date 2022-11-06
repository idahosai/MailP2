//login
const loginForm = document.querySelector(".login-form");
console.log(loginForm);

loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    console.log("HELLO");
    //get user info
    const email = loginForm['email-login'].value;
    const password = loginForm['password-login'].value;
    auth.signInWithEmailAndPassword(email, password).then(cred => {
        console.log(cred.user);
        loginForm.reset();
        document.location.href = './dashboard.html';
    })
})