import pytest
from restaurant_bill import bill_total, split_bill, table_wait

#Example test cases:
def test_dine_in_bill():
    assert bill_total("dine_in", 1000, 2, False) == 1155

def test_even_split():
    assert split_bill(1000, 4, 10) == 275

# ---- bill_total ----
def test_unknown_section_raises():
    with pytest.raises(ValueError, match="unknown section"):
        bill_total("bar", 1000, 2, False)

def test_negative_food_raises():
    with pytest.raises(ValueError, match="invalid order"):
        bill_total("dine_in", -1, 2, False)

def test_happy_hour_dine_in_discount():
    assert bill_total("dine_in", 1000, 2, True) == 924

def test_large_party_adds_service_charge():
    assert bill_total("dine_in", 1000, 8, False) == 1365

# ---- split_bill ----
def test_invalid_people_raises():
    with pytest.raises(ValueError, match="invalid people count"):
        split_bill(1000, 0, 10)

def test_invalid_tip_raises():
    with pytest.raises(ValueError, match="invalid tip"):
        split_bill(1000, 4, -5)

def test_uneven_split_rounds_up():
    assert split_bill(1000, 3, 0) == 334

# ---- table_wait ----
def test_table_wait_call_ahead():
    assert table_wait(13, 5, False) == "call ahead"

def test_table_wait_reservation_seats_now():
    assert table_wait(4, 0, True) == "seat now"

def test_table_wait_no_free_tables():
    assert table_wait(4, 0, False) == "waitlist"

def test_table_wait_large_party_few_tables():
    assert table_wait(7, 1, False) == "waitlist"

def test_table_wait_default_seats_now():
    assert table_wait(4, 3, False) == "seat now"
