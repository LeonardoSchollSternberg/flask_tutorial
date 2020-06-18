function carregar() {
  document.body.style.cursor="none"
  var today = new Date()
  var month = today.getMonth()+1
  var day = today.getDate()
  var hours = today.getHours()
  var min = today.getMinutes()
  var sec = today.getSeconds()
  var dia_semana = today.getDay()

  var semana = new Array(6)
  semana[0]='Domingo'
  semana[1]='Segunda'
  semana[2]='Terça'
  semana[3]='Quarta'
  semana[4]='Quinta'
  semana[5]='Sexta'
  semana[6]='Sábado'


  if (hours<10)
    hours=`0${hours}`
  if (min<10)
    min=`0${min}`
  if (sec<10)
    sec=`0${sec}`

  if (month<10)
    month=`0${month}`
  if (day<10)
    day=`0${day}`

  var hor = document.getElementById("horario").innerText=`${hours}:${min}:${sec}`
  var d_date = document.getElementById("calendario").innerText=`${day}/${month}/${today.getFullYear()} - ${semana[dia_semana]}`
  setTimeout(function() {
    carregar();
  }, 1000);
  //setTimeout(carregar, 1000)
  setTimeout(mudar, 4000)

  //var hor = document.getElementById("horario").innerText=`${user4}`
}



function mudar() {
  document.location.href="teste2"
}