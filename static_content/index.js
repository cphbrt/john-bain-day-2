function doStuff() {
  console.log("doing stuff");
  var pStuff = document.getElementById("stuff");
  pStuff.innerHTML = "done!";
}

function doAPICall(url) {
  var request = new XMLHttpRequest();
  //var url = 'https://google.com'
  //var url = 'https://ghibliapi.herokuapp.com/films';
  //var url = 'http://localhost:5000/introduction/';
  request.open('GET', url);
  request.onload = function() {
    console.log("received API data");
    var data = this.response;
    displayAPIResults(data);
  }
  request.send();
}

function displayAPIResults(data) {
  console.log("displaying API results");
  var pStuff = document.getElementById("stuff");
  pStuff.innerHTML = data;
}

function doAPICallAbout(url){
  var request = new XMLHttpRequest();
  //var url = 'https://google.com'
  //var url = 'https://ghibliapi.herokuapp.com/films';
  //var url = 'http://localhost:5000/introduction/';
  request.open('GET', url);
  request.onload = function() {
    console.log("received API data");
    var obj = JSON.parse(this.response);
    var data = "<h1>" + obj.solution + "</h1><p>" + obj.value + "</p>";

    displayAPIResults(data);
  }
  request.send();
}

function doAPIPush(url){
  var first_num = document.getElementById("firstNum").value;
  var second_num = document.getElementById("secondNum").value;
  var postString = "first_num=" + first_num + "&second_num=" + second_num;

  var request = new XMLHttpRequest();
  request.open('POST', url);
  request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  request.onload = function() {
    console.log("received API data");
    displayAPIResults(this.response);
  }
  request.send(postString);
}

function doAPIPrime(url){
  var happyPrime = document.getElementById("happyPrime").value;
  var postString = "happy_prime=" + happyPrime;

  var request = new XMLHttpRequest();
  request.open('POST', url);
  request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  request.onload = function() {
    console.log("received API data");
    displayAPIResults(this.response);
  }
  request.send(postString)
}
