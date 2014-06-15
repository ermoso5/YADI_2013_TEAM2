YADI - Yet Another Datalog Interpreter
================================================
                                        
What is YADI?

Yet Another Datalog Interpreter (YADI) is a tool which translates Datalog queries into SQL statements returning a set of tuples

A Datalog query against {R(A,B), S(B,C,D)} database looks like this:

    V(x,y) :- R(x,y) and S(y,_,_). 
    Q(x,y) :- S(x,y,z) and V(z,t) and t>=3.
    ?- Q(x,y).
    
where the two first lines define idb predicates and the third line provides the actual query, i.e. the idb of the result set.
Despite its multiple-rules form, the above Datalog query is a Conjunctive Query that can be translated into the following SQL statement:

    SELECT S2.B, S2.C 
    FROM R, S S1, S S2  
    WHERE R.B=S1.B AND R.A=S2.D AND S1.B>=3

This purpose of this project is to build a user friendly interface allowing users to define predicates and input query.
The query will be evaluated and the result will be displayed on the interface.
The program will catch errors and display them as well.



The team
------------------------------------

Collaborators of the project:
  * Qutiba  shaikh Elrd       
  * Zara Alaverdyan
  * Hussein Al-Natsheh
  * Tajalla Hashmi
  * Yue He
