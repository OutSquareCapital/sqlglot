"""sqlglot expressions - math, trigonometry, and bitwise functions."""

from __future__ import annotations

import typing as t

from sqlglot.expressions.core import Expression, Expr, ExprTyped, Func, AggFunc


# Trigonometric


class Acos(Expression, Func):
    pass


class Acosh(Expression, Func):
    pass


class Asin(Expression, Func):
    pass


class Asinh(Expression, Func):
    pass


class Atan(ExprTyped[Expr, t.Optional[Expr]], Func):
    arg_types = {"this": True, "expression": False}


class Atanh(Expression, Func):
    pass


class Atan2(ExprTyped[Expr, Expr], Func):
    arg_types = {"this": True, "expression": True}


class Cos(Expression, Func):
    pass


class Cosh(Expression, Func):
    pass


class Cot(Expression, Func):
    pass


class Coth(Expression, Func):
    pass


class Csc(Expression, Func):
    pass


class Csch(Expression, Func):
    pass


class Degrees(Expression, Func):
    pass


class Radians(Expression, Func):
    pass


class Sec(Expression, Func):
    pass


class Sech(Expression, Func):
    pass


class Sin(Expression, Func):
    pass


class Sinh(Expression, Func):
    pass


class Tan(Expression, Func):
    pass


class Tanh(Expression, Func):
    pass


# Geometric distance / similarity


class CosineDistance(ExprTyped[Expr, Expr], Func):
    arg_types = {"this": True, "expression": True}


class DotProduct(ExprTyped[Expr, Expr], Func):
    arg_types = {"this": True, "expression": True}


class EuclideanDistance(ExprTyped[Expr, Expr], Func):
    arg_types = {"this": True, "expression": True}


class JarowinklerSimilarity(ExprTyped[Expr, Expr], Func):
    arg_types = {
        "this": True,
        "expression": True,
        "case_insensitive": False,
        "integer_scale": False,
    }


class ManhattanDistance(ExprTyped[Expr, Expr], Func):
    arg_types = {"this": True, "expression": True}


# Basic arithmetic / math


class Abs(Expression, Func):
    pass


class Cbrt(Expression, Func):
    pass


class Ceil(ExprTyped[Expr, None], Func):
    arg_types = {"this": True, "decimals": False, "to": False}
    _sql_names = ["CEIL", "CEILING"]


class Exp(Expression, Func):
    pass


class Factorial(Expression, Func):
    pass


class Floor(ExprTyped[Expr, None], Func):
    arg_types = {"this": True, "decimals": False, "to": False}


class IsInf(Expression, Func):
    _sql_names = ["IS_INF", "ISINF"]


class IsNan(Expression, Func):
    _sql_names = ["IS_NAN", "ISNAN"]


class Ln(Expression, Func):
    pass


class Log(ExprTyped[Expr, t.Optional[Expr]], Func):
    arg_types = {"this": True, "expression": False}


class Pi(Expression, Func):
    arg_types = {}


class Round(ExprTyped[Expr, None], Func):
    arg_types = {
        "this": True,
        "decimals": False,
        "truncate": False,
        "casts_non_integer_decimals": False,
    }


class Sign(Expression, Func):
    _sql_names = ["SIGN", "SIGNUM"]


class Sqrt(Expression, Func):
    pass


class Trunc(ExprTyped[Expr, None], Func):
    arg_types = {"this": True, "decimals": False, "fractions_supported": False}
    _sql_names = ["TRUNC", "TRUNCATE"]


# Safe arithmetic


class SafeAdd(ExprTyped[Expr, Expr], Func):
    arg_types = {"this": True, "expression": True}


class SafeDivide(ExprTyped[Expr, Expr], Func):
    arg_types = {"this": True, "expression": True}


class SafeMultiply(ExprTyped[Expr, Expr], Func):
    arg_types = {"this": True, "expression": True}


class SafeNegate(Expression, Func):
    pass


class SafeSubtract(ExprTyped[Expr, Expr], Func):
    arg_types = {"this": True, "expression": True}


# Bitwise


class BitwiseAndAgg(Expression, AggFunc):
    pass


class BitwiseCount(Expression, Func):
    pass


class BitwiseOrAgg(Expression, AggFunc):
    pass


class BitwiseXorAgg(Expression, AggFunc):
    pass


class BitmapBitPosition(Expression, Func):
    pass


class BitmapBucketNumber(Expression, Func):
    pass


class BitmapConstructAgg(Expression, AggFunc):
    pass


class BitmapCount(Expression, Func):
    pass


class BitmapOrAgg(Expression, AggFunc):
    pass


class Booland(ExprTyped[Expr, Expr], Func):
    arg_types = {"this": True, "expression": True, "round_input": False}


class Boolnot(ExprTyped[Expr, None], Func):
    arg_types = {"this": True, "round_input": False}


class Boolor(ExprTyped[Expr, Expr], Func):
    arg_types = {"this": True, "expression": True, "round_input": False}


class BoolxorAgg(Expression, AggFunc):
    pass


class Getbit(ExprTyped[Expr, Expr], Func):
    _sql_names = ["GETBIT", "GET_BIT"]
    # zero_is_msb means the most significant bit is indexed 0
    arg_types = {"this": True, "expression": True, "zero_is_msb": False}
