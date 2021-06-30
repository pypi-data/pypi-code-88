
import tongpo.res.cf.boyorgirl as t1

def test_1(capsys):
    input_values = ['xiaodao']

    def mock_input():
        return input_values.pop(0)
    t1.input = mock_input

    t1.main()

    out, err = capsys.readouterr()

    assert out == 'IGNORE HIM!\n'
    assert err == ''





