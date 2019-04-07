const fs = require('fs');
var util = require('util');

var exec = require('child_process').exec;

var command = "curl --request POST --url https://carnet.ai/recognize-file --header 'Connection: keep-alive' --header 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundarybL0pJQRNggqxuxMT' --header 'Postman-Token: 0cb3138e-d99c-4f25-ac42-30339903eff7' --header 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36' --header 'X-Requested-With: XMLHttpRequest' --header 'cache-control: no-cache' --header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' --form imageFile=@/home/alinp25/HackTM/img.jpg"

function testJSON(text){
  try{
      if (typeof text!=="string"){
          return false;
      }else{
          JSON.parse(text);
          return true;                            
      }
  }
  catch (error){
      return false;
  }
}

function doit() {
  var out = {};
  const curl = exec(command);
  return new Promise(function(resolve){
    var data = "";
    curl.stdout.on('data', function(d) {
      data += d.toString("UTF-8");
    });
    curl.on('close', function(code, signal) {
      if (testJSON(data)) {
        resolve(JSON.parse(data));
      } else {
        resolve(JSON.parse("{}"));
      }
    });
  });
  
}

async function loop(){
  while(1){
    var l = await doit();
    var data_output = "";
    if (l.error) {
      continue;
    }
    if (!l.car) {
      console.log("Car not detected.");
      data_output += "Marca: ---\nModel: ---\nGeneratie: ---\nProbabilitate: ---\n0\n0\n0\n0";
      fs.writeFile("cardata.txt", data_output, function(err) {
        if(err) {
          console.log(err);
        }
    
        console.log("The file was saved!");
      }); 
      continue;
    }
    data_output += "Marca: ";
    if (l.car.make && l.car.make != 'Other') {
      data_output += l.car.make; 
    } else {
      data_output += "---"; 
    }
    data_output += "\nModel: ";
    if (l.car.make && l.car.make != 'Other') {
      data_output += l.car.model;
    } else {
      data_output += "---"; 
    }
    data_output += "\nGeneratie: ";
    if (l.car.make && l.car.make != 'Other') {
      data_output += l.car.generation;
    } else {
      data_output += "---"; 
    }
    data_output += "\nProbabilitate: ";
    if (l.car.make && l.car.make != 'Other') {
      data_output += l.car.prob;
    } else {
      data_output += "---"; 
    }

    if (l.bbox) {
      data_output += "\n" + (l.bbox.tl_x).toString();
      data_output += "\n" + (l.bbox.tl_y).toString();
      data_output += "\n" + (l.bbox.br_x).toString();
      data_output += "\n" + (l.bbox.br_y).toString();
    } else {
      data_output += "\n0\n0\n0\0n";
    }

    fs.writeFile("cardata.txt", data_output, function(err) {
      if(err) {
          console.log(err);
      }
  
      console.log("The file was saved!");
    }); 
    console.log(data_output);
  }
}

loop();