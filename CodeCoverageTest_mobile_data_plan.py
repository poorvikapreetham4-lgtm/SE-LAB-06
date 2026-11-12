
import pytest
from mobile_data_plan import (
    overage_charge,
    recharge_allowed,
    validity_status
)


# 1. Tests for overage_charge()

def test_within_included_data():
    assert overage_charge("basic", 2, False, False) == 0


def test_loyal_customer_extra_data():
    assert overage_charge("standard", 6, False, True) == 0


def test_premium_loyal_customer():
    assert overage_charge("premium", 11, False, True) == 15


def test_non_roaming_overage():
    assert overage_charge("basic", 3, False, False) == 15


def test_roaming_overage():
    assert overage_charge("basic", 3, True, False) == 40


def test_large_non_roaming_overage():
    assert overage_charge("basic", 13, False, False) == 275


def test_large_roaming_overage():
    assert overage_charge("basic", 13, True, False) == 605


def test_unknown_plan():
    with pytest.raises(ValueError, match="unknown plan"):
        overage_charge("gold", 5, False, False)


def test_negative_data_usage():
    with pytest.raises(ValueError, match="invalid data usage"):
        overage_charge("basic", -1, False, False)


# 2. Tests for recharge_allowed()

def test_kyc_pending_allowed():
    assert recharge_allowed(200, 1, True) is True


def test_kyc_pending_limit_exceeded():
    assert recharge_allowed(201, 1, True) is False


def test_recharge_above_limit():
    assert recharge_allowed(2001, 1, False) is False


def test_recharge_allowed_with_pending_count():
    assert recharge_allowed(500, 1, False) is True


def test_recharge_not_allowed_with_many_pending():
    assert recharge_allowed(500, 3, False) is False


# 3. Tests for validity_status()

def test_prepaid_active():
    assert validity_status(0, True, False) == "active"


def test_postpaid_active():
    assert validity_status(3, False, False) == "active"


def test_addon_active():
    assert validity_status(2, True, True) == "active"


def test_grace_period():
    assert validity_status(2, False, False) == "grace"


def test_grace_period_boundary():
    assert validity_status(-12, False, False) == "grace"


def test_expired_plan():
    assert validity_status(-13, False, False) == "expired"
