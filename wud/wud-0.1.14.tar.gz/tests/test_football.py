from wud.football import team_name_revise, get_hdc_result, get_hdc_return


def test_team_name_revise():
    assert team_name_revise('Chelsea FC', 'footballapi', 'livescore') == 'Chelsea'
    assert team_name_revise('Tottenham Hotspur', 'livescore', 'short') == 'Spurs'
    
    assert team_name_revise("Man Utd", 'short', 'livescore') == "Manchester United"
    
    assert team_name_revise("Nankatsu", 'footballapi', 'livescore') == "Nankatsu"
    
    
    
def test_get_hdc_result():
    assert get_hdc_result('0.5', 'home', '1', '0') == ('home', 1)
    assert get_hdc_result('0.25', 'home', '0', '0') == ('away', 0.5)
    assert get_hdc_result('0.75', 'home', '1', '0') == ('home', 0.5)
    assert get_hdc_result('0.75', 'home', '2', '0') == ('home', 1)
    assert get_hdc_result('0', 'home', '0', '0') == ('home', 0)
    assert get_hdc_result('1', 'home', '1', '0') == ('home', 0)
    assert get_hdc_result('1', 'home', '0', '0') == ('away', 1)

    assert get_hdc_result('0.5', 'away', '1', '0') == ('home', 1)
    assert get_hdc_result('0.25', 'away', '0', '0') == ('home', 0.5)
    assert get_hdc_result('0.75', 'away', '1', '0') == ('home', 1)
    assert get_hdc_result('0.75', 'away', '2', '0') == ('home', 1)
    assert get_hdc_result('0', 'away', '0', '0') == ('home', 0)
    assert get_hdc_result('1', 'away', '1', '0') == ('home', 1)
    assert get_hdc_result('1', 'away', '0', '0') == ('home', 1)    

def test_get_hdc_return():
    assert get_hdc_return('home', 1, 'home', '500') == 500
    assert get_hdc_return('home', 0.5, 'home', '500') == 250
    assert get_hdc_return('away', 0, 'home', '500') == 0
    assert get_hdc_return('home', 1,'away', '500') == -500
    assert get_hdc_return('away', 0.5, 'home', '500') == -250
    assert get_hdc_return('away', 0.5, 'minus', '200') == -200