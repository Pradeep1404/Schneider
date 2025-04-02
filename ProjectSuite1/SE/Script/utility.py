def run_Calculator():
  TestedApps.WindowsCalculator.Run()
  
def close_claculator():
  calc = Sys.Process("Microsoft.WindowsCalculator").UIAObject("Calculator")
  calc.Close()
  
 
def numbers():
  one = Sys.Process("Microsoft.WindowsCalculator").UIAObject("Calculator").UIAObject("NavView").UIAObject("LandmarkTarget").UIAObject("Number_pad").UIAObject("One")
  two = Sys.Process("Microsoft.WindowsCalculator").UIAObject("Calculator").UIAObject("NavView").UIAObject("LandmarkTarget").UIAObject("Number_pad").UIAObject("Two")
  three = Sys.Process("Microsoft.WindowsCalculator").UIAObject("Calculator").UIAObject("NavView").UIAObject("LandmarkTarget").UIAObject("Number_pad").UIAObject("Three")
  
  add = Sys.Process("Microsoft.WindowsCalculator").UIAObject("Calculator").UIAObject("NavView").UIAObject("LandmarkTarget").UIAObject("Standard_operators").UIAObject("Plus")
  equals = Sys.Process("Microsoft.WindowsCalculator").UIAObject("Calculator").UIAObject("NavView").UIAObject("LandmarkTarget").UIAObject("Standard_operators").UIAObject("Equals")
  
  one.Click()
  add.Click()
  two.Click()
  add.Click()
  three.Click()
  equals.Click()  
  
############################################################################################################################################################ 
#name: Author name 
#Description: what does this method do 
#parameters: what is the parameter format and eg as well
def numbers_add(param):
  
  num_pad = Sys.Process("Microsoft.WindowsCalculator").UIAObject("Calculator").UIAObject("NavView").UIAObject("LandmarkTarget").UIAObject("Number_pad")
  buttons = num_pad.FindAllChildren("ClassName","Button",10)
  for button in buttons:
    if button.ObjectIdentifier == param:
      button.Click()
      Log.Message(f'{button.ObjectIdentifier} has been clicked')
      break
  else:
    Log.Warning(f'{param} has not been clicked')
############################################################################################################################################################ 
def add():
  numbers_add("Three")
  numbers_add("Four")
  numbers_add("Tree")