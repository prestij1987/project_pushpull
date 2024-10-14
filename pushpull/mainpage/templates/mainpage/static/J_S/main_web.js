// JavaScript код для показа/скрытия подменю


/* Переписали Котлин на JavaScript */
const Rp = 6356.8        // km. Not used
const Re = 6378.0        // km. Not used
const earthRadius = 6371

function Pifagor(p1, p2) {   // p.x, p.y, p.z
  return sqrt(
    (p1.z - p2.z) * (p1.z - p2.z) +
    (p1.x - p2.x) * (p1.x - p2.x) +
    (p1.y - p2.y) * (p1.y - p2.y))
}

// Стрелочные функции конверсии в радианы и градусы
const degreesToRadians = degrees => degrees * (Math.PI / 180);
const radiansToDegrees = radians => radians * (180 / Math.PI);

function loc_to_sphere(location) {   // location: longitude, latitude, altitude
  const alt = location.altitude / 1000.0         // km

  const lon = degreesToRadians(location.longitude)  
  const lat = degreesToRadians(location.latitude)

  // To Spherical coordinates
  const cl = Math.cos(lat)
  const R  = earthRadius + alt  // km
  return {
    z: R * Math.sin(lat),
    x: R * cl * Math.cos(lon),
    y: R * cl * Math.sin(lon)
  }
}

function distance(location1, location2) {
  return Pifagor(
    loc_to_sphere(location1),
    loc_to_sphere(location2)
  )
}

// Координаты городов
const cities = {
  'Москва': {
    latitude: 55.755826,
    longitude: 37.6173,}}