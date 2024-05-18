
# Pseudocode 
Ask the user to input two whole numbers (num1 and num2) and perform multiplication (num1*num2) and division (num1/num2) operation using the two numbers.

######################################################
```
PROCEDURE obtainUserInput(input_prompt)
    SET input_not_accepted = true
    SET user_input = 0
    WHILE input_not_accepted is true
        BEGIN
            PRINT input_prompt
            READ input as Integer in user_input
            SET input_not_accepted = false
        EXCEPTION
            DISPLAY invalid input message
            SET input_not_accepted = true
        END
    ENDWHILE
    RETURN user_input value

CALL obtainUserInput RETURNING number1
CALL obtainUserInput RETURNING number2
COMPUTE multiplication as number1 * number2
PRINT multiplication message
IF number2 = 0 THEN
    PRINT division by 0 results to an undefined value
ELSE
    COMPUTE division as number1 / number2
    PRINT division message
END IF

```