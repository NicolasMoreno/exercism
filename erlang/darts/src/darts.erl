-module(darts).
-import(math, [pow/2]).
-export([score/2]).


score(_X, _Y) -> 
    _ShotRadius = getRadius(_X, _Y),
    if 
        _ShotRadius == 0 -> 10;
        _ShotRadius =< 5 -> 5;
        _ShotRadius > 10 -> 0;
        ((_ShotRadius > 5) and (_ShotRadius =< 10)) -> 1
    end.

getRadius(_X, _Y) -> pow( ( pow(_X, 2) + pow(_Y, 2) ) , 0.5).