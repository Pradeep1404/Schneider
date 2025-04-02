Feature: Arithmetic operation on calculator applications

  Scenario: Addition of 3 numbers
    Given I have Launch calculator application
    When I enter the "<Number1>","<Number2>","<Number3>"
    And I perform the arithmetic operations "<Operator1>","<Operator2>"
    Then I able to verify the addition of two numbers.
    
