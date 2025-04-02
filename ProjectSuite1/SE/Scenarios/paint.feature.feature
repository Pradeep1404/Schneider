Feature: Running the paint application

  Scenario: using brushes to find slope in paint.
    Given I have open the paint
    When I have select the brushes in items toolbar
    And I have draw the slope to find the co-ordinates
    Then I verify that Slope is drawn.