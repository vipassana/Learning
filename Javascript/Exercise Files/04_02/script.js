function findBiggestFraction(a, b){
  var result;
  (a > b)? result = ["First Fraction", a] : result = ["Second Fraction", b];
  return result;
}
console.log(findBiggestFraction(34/67,4/19));
