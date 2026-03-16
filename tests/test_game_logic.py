from logic_utils import (
    attempts_left,
    check_guess,
    parse_guess,
    get_range_for_difficulty,
)


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_check_guess_with_string_secret_is_numeric():
    # Regression test: string secrets like "15" should still compare numerically.
    outcome, _ = check_guess(9, "15")
    assert outcome == "Too Low"


def test_parse_guess_accepts_float_strings():
    ok, value, err = parse_guess("9.0")
    assert ok is True
    assert value == 9
    assert err is None


def test_range_for_difficulty_is_consistent():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 50)
    assert get_range_for_difficulty("Hard") == (1, 200)


def test_attempts_left_decrements_on_first_guess():
    # Ensure remaining attempts reflect that one guess has already been used.
    assert attempts_left(7, 0) == 7
    assert attempts_left(7, 1) == 6
