
import pytest
from mobile_data_plan import (
    overage_charge,
    recharge_allowed,
    validity_status
)


# 1. Branch tests for overage_charge()

def test_unknown_plan_branch():
    with pytest.raises(ValueError):
        overage_charge("gold", 5, False, False)


def test_negative_data_branch():
    with pytest.raises(ValueError):
        overage_charge("basic", -5, False, False)


def test_loyal_nonpremium_branch():
    assert overage_charge("standard", 6, False, True) == 0


def test_nonloyal_branch():
    assert overage_charge("basic", 3, False, False) == 15


def test_loyal_premium_branch():
    assert overage_charge("premium", 11, False, True) == 15


def test_no_extra_data_branch():
    assert overage_charge("standard", 5, False, False) == 0


def test_extra_data_branch():
    assert overage_charge("basic", 3, False, False) == 15


def test_roaming_branch():
    assert overage_charge("basic", 3, True, False) == 40


def test_non_roaming_branch():
    assert overage_charge("basic", 3, False, False) == 15


def test_extra_above_ten_nonroaming():
    assert overage_charge("basic", 13, False, False) == 275


def test_extra_above_ten_roaming():
    assert overage_charge("basic", 13, True, False) == 605


# 2. Branch tests for recharge_allowed()

def test_kyc_pending_true_allowed():
    assert recharge_allowed(200, 1, True) is True


def test_kyc_pending_true_rejected():
    assert recharge_allowed(201, 1, True) is False


def test_kyc_pending_false():
    assert recharge_allowed(500, 1, False) is True


def test_amount_above_2000():
    assert recharge_allowed(2001, 1, False) is False


def test_pending_recharges_within_limit():
    assert recharge_allowed(500, 2, False) is True


def test_pending_recharges_exceed_limit():
    assert recharge_allowed(500, 3, False) is False


# 3. Branch tests for validity_status()

def test_prepaid_branch():
    assert validity_status(0, True, False) == "active"


def test_postpaid_branch():
    assert validity_status(3, False, False) == "active"


def test_addon_branch():
    assert validity_status(2, True, True) == "active"


def test_without_addon_branch():
    assert validity_status(3, True, False) == "active"


def test_active_branch():
    assert validity_status(3, False, False) == "active"


def test_grace_branch():
    assert validity_status(2, False, False) == "grace"


def test_grace_boundary_branch():
    assert validity_status(-12, False, False) == "grace"


def test_expired_branch():
    assert validity_status(-13, False, False) == "expired"
