// JavaScript код для показа/скрытия подменю




function work_but (){
    var pogruz = way1
    var razgruz = way2

     var all_dist = way1 / way2

};

function zapros_out( ){

  var num = document.getElementById('zapros');

  num.onclick = function(){
    var number = 'Введите телефон ';
    var email = 'Введите почту '
  };

  var number = document.createElement('')
}

console.log(zapros_out())

function count_1() {
var R = 6372795
   // Координаты городов
const cities = [
    ['Москва', 55.755826, 37.6173],
    ['Санкт-Петербург', 59.934280, 30.335086],
    ['Казань', 55.797104, 49.114209],
    ['Краснодар', 45.040233, 38.976286]
  ];
}

// Чужой код
const degreesToRadians = degrees => degrees * (Math.PI / 180);
const radiansToDegrees = radians => radians * (180 / Math.PI);

const centralSubtendedAngle = (locationX, locationY) => {
  const locationXLatRadians = degreesToRadians(locationX.latitude);
  const locationYLatRadians = degreesToRadians(locationY.latitude);
return radiansToDegrees(
    Math.acos(
      Math.sin(locationXLatRadians) * Math.sin(locationYLatRadians) +
        Math.cos(locationXLatRadians) *
          Math.cos(locationYLatRadians) *
          Math.cos(
            degreesToRadians(
              Math.abs(locationX.longitude - locationY.longitude)
            )
       )
    )
  );
}

2 * PI * {radius_of_the_earth} * ({central_subtended, angle} / 360);


const earthRadius = 6371
const greatCircleDistance = angle => 2 * Math.PI * earthRadius * (angle / 360);
const distanceBetweenLocations = (locationX, locationY) =>
  greatCircleDistance(centralSubtendedAngle(locationX, locationY));

const Moscow = {latitude: 55.755826, longitude: 37.6173};
const Saint_Petersbutg = {latitude: 59.934280, longitude: 30.335086};
console.log(distanceBetweenLocations(Moscow, Saint_Petersbutg));