function login() {

    let user = document.getElementById("username").value.trim();
    let pass = document.getElementById("password").value.trim();

    if (user === "") {
        alert("Please enter your username");
        return;
    }

    if (pass === "") {
        alert("Please enter your password");
        return;
    }

    if (user === "admin" && pass === "1234") {

        alert("✅ Login Successful!");

        window.location.href = "/services/";

    } else {

        alert("❌ Invalid Username or Password");

    }
}


function bookNow() {

    let answer = confirm("Please Login First");

    if(answer){
        window.location.href = "/";
    }

}