function Person(name, age){
  this.name = name;
  this.age = age ;
  this.happyBirthday = function(){
    ++this.age;
  }
}

vipa = new Person("Vipassana Vijayarangan", 27);
tom = new Person("Tom Smith", 43);

console.log(vipa);
console.log(tom);
