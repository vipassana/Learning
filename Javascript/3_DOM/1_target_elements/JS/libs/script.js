function change(){
  let p = d3.select(".promo-lede")
  p.text("changed it!!!!")
}

function addButton(){
  let p = d3.select(".promo-lede")
  p.append('button').text("Another buttons")
}

function changeBgColor(){
  let p = d3.select(".promo-lede")
  p.style('background-color', 'coral')
}
