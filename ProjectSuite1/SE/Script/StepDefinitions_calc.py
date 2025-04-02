import calc

@given("I have Launch calculator application")
def step_impl():
  calc.calc()
  
@when("I enter the Number1, Number2, Number3")
def step_impl():
  calc.num_pad()
  
@when("I perform the arithmetic operations Operator1,Operator2")
def step_impl():
  calc.oprators_pad() 
  
@then("I able to verify the addition of two numbers")
def step_impl():
  pass   

  