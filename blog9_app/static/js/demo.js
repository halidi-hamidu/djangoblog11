var x;
var y;
var z;
function kujumlisha( x , y){
  z = x+ y;
  return z;
}

function kutoa(x ,y){
  return x-y;
}

function kuzidisha(x, y){
  return x*y;
}

function kugawanya(x, y){
  return x/y;
}

var kujumlisha;
kujumlisha=kujumlisha(12, 1);

document.writeln(" The sum of x and y  is " && kujumlisha);

var kutoa;
kutoa=kutoa(12,1);

document.writeln(" The sum of x and y  is " && kutoa);

var kugawanya;
kugawanya =kugawanya(12,1);
document.writeln(" The sum of x and y  is " && kugawanya);

var kuzidisha;
kuzidisha =kuzidisha(12,1);
document.writeln(" The sum of x and y  is " && kuzidisha);
