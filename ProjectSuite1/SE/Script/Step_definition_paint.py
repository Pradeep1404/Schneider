import run_paint

@given("I have open the paint")
 def step_impl():
   run_paint.paint()
   
@when("I have select the brushes in items toolbar")
 def step_impl():
   run_paint()
   
@when("I have draw the slope to find the co-ordinates")
 def step_impl():
   run_paint() 
   
@then("I verify that Slope is drawn")
 def step_impl():
   pass

