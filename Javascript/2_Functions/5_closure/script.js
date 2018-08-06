function doSomeMath() {
	var a = 5;
	var b = 4;

	//This is an example of closure. JS is smart enough to figure out
	//that a, b need to be passed along with returning the multiply function
	function multiply(){
		return a*b;
	}

	return multiply;
}


console.log("The result: ", doSomeMath());
