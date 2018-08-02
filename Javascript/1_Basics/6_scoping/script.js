function scoping(){
  var varScope = "Function scope"
      if (true){
        let varScope = "Condition scope"
        console.log("Condition Scope : " + varScope)

      }
      console.log("Function Scope : " + varScope)

}

scoping()
