from dni import DNI
import pytest

@pytest.mark.DNI
def test_out_Letter():
    assert "43470488" == DNI.out_Letter("43470488M")
    assert "12345678" == DNI.out_Letter("12345678W")

@pytest.mark.DNI
def test_Correct_Size():
    assert "43470488" == DNI.correct_size("43470488")
    assert False == DNI.correct_size("4347048")
    assert False == DNI.correct_size("434704888")

@pytest.mark.DNI
def test_transform_Int():
    assert 43470488 == DNI.transform_Int("43470488")
    assert 87654321 == DNI.transform_Int("87654321")

@pytest.mark.DNI
def test_resto_division():
    assert 0 == DNI.resto_division(00000000)
    assert 5 == DNI.resto_division(43470488)
    assert 10 == DNI.resto_division(87654321)

@pytest.mark.DNI
def test_letter_dni():
    assert "M" == DNI.letter_dni(5)
    assert "T" == DNI.letter_dni(0)
    assert "K" == DNI.letter_dni(21)

@pytest.mark.DNI
def test_compare_letters():
    assert True == DNI.compare_letters("M", "M")
    assert True == DNI.compare_letters("N", "N")
    assert False == DNI.compare_letters("A", "Q")





    

    