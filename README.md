<h1> PLDC</h1>

<h2>Polynomial Laplace Dominion Converter</h2>

<h3>Introduction</h3>

 In today’s world, it is almost impossible to think that one can survive without computers or gadgets. They have become a tool for people of every age and profession. Computers have brought a revolution in almost every field, since medicine, business, technology, media, etc. An example of this is the electrical engineering field, where there are a lot of problems to be solved and a lot of room for improvement. One of the problems that we will try to solve is the calculations of the Laplace transform, since they are usually done manually. PLDC will focus on converting the Laplace transform domains of polynomial expressions from domain s to domain t and vice versa. We strike to be a very simple and intuitive programming language, without the hazards of learning a new syntax or behavior. Our goal is to provide the means to solve quickly and in a efficient way electric circuits that require the Laplace transform equation. 

<h3>Language Features</h3>

 PLDC will provide an easy format to use, where the user should input a polynomial equation and apply a command “Laplace” it receive the conversion in terms of time domain or s domain. Users will also be able to print the expressions and their results in the terminal window. We expect that the primary user for this language will be Electrical Engineering students, since they often have to use Laplace transforms.
 

<h3>Example of Program</h3>
```
//Create expression in t or s domain
    tExpressionName = 2t^4
    sExpressionName = 5s^3+1s

//Assign result of transform to variable
    result1 = laplace(tExpressionName)
    result2 = laplace(2t^4)
    result3 = laplace(sExpressionName)
    result4 = laplace sExpressionName
    result5 = laplace 5s^2-2s+s

//Display result in terminal
    show result1
    show “Result of expression in S domain is: ” result1
```
