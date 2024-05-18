
# Pseudocode 
Ask the user to input two numbers (num1 and num2) and perform addition (num1+num2) and subtraction (num1-num2) operation using the two numbers.

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
COMPUTE sum as number1 + number2
PRINT sum message
COMPUTE subtract as number1 - number2
PRINT subtract message
```