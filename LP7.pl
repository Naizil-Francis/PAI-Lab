% Addition
add(X, Y, Result) :-
    Result is X + Y.

% Subtraction
subtract(X, Y, Result) :-
    Result is X - Y.

% Multiplication
multiply(X, Y, Result) :-
    Result is X * Y.

% Division
divide(X, Y, Result) :-
    Y =\= 0,  % Ensure Y is not zero to avoid division by zero
    Result is X / Y.

% Example queries:
% To add 5 and 3:
% ?- add(5, 3, Result).
%
% To subtract 7 from 10:
% ?- subtract(10, 7, Result).
%
% To multiply 4 by 6:
% ?- multiply(4, 6, Result).
%
% To divide 8 by 2:
% ?- divide(8, 2, Result).
%
% Note: In Prolog, you can run these queries in an interactive Prolog environment.

