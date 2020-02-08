function doStuff() {
  console.log("doing stuff");
  var pStuff = document.getElementById("stuff");
  pStuff.innerHTML = "done!";
}

function doAPICall(url) {
  var request = new XMLHttpRequest();
  //var url = 'https://google.com'
  //var url = 'https://ghibliapi.herokuapp.com/films';
  //var url = 'http://127.0.0.1:5000/introduction/';
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
