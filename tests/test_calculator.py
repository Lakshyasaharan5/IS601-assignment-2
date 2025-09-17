import calculator

def test_repl_add_and_exit(monkeypatch, capsys):
    # fake user input: "add 2 3", then "exit"
    inputs = iter(["add 2 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator.repl()

    captured = capsys.readouterr()
    assert "5.0" in captured.out
    assert "Goodbye!" in captured.out


def test_repl_invalid_command(monkeypatch, capsys):
    # fake user input: "hello", then "exit"
    inputs = iter(["hello", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator.repl()

    captured = capsys.readouterr()
    assert "Unknown command" in captured.out


def test_repl_division_by_zero(monkeypatch, capsys):
    # fake user input: "div 5 0", then "exit"
    inputs = iter(["div 5 0", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator.repl()

    captured = capsys.readouterr()
    assert "Error: Division by zero" in captured.out
