
# Pseudocode 
Ask the user to input two numbers (num1 and num2) and perform multiplication (num1*num2) and division (num1/num2) operation using the two numbers.

######################################################
```
PROCEDURE obtainUserInput(input_prompt, allow_zero)
    SET input_not_accepted = true
    SET user_input = 0
    WHILE input_not_accepted is true
        BEGIN
            PRINT input_prompt
            READ input as Integer in user_input
            SET input_not_accepted = false
                IF allow_zero = false and user_input = 0 THEN
                    RAISE Value Exception
                END IF
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
COMPUTE division as number1 / number2
PRINT division message
```