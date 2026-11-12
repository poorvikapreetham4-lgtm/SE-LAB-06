# SE Lab 06 – Code Coverage and Branch Coverage

## 1. Aim

To understand and implement code coverage and branch coverage using Python, Pytest, and Coverage.py. The objective is to measure test completeness, identify untested code paths, and achieve at least 90% code and branch coverage.

## 2. Objectives

- Understand the difference between line coverage and branch coverage.
- Measure test coverage using Python Coverage.py.
- Identify untested lines and decision branches.
- Write test cases covering normal conditions and edge cases.
- Achieve a minimum of 90% code coverage and branch coverage.

## 3. Technologies Used

- Python 3.x
- Pytest
- Coverage.py
- Visual Studio Code
- Git and GitHub

## 4. Project Description

This project focuses on testing a Mobile Data Plan application using Python. The application contains three main functions that handle mobile data charges, recharge eligibility, and plan validity.

Test cases are designed to verify different input conditions, decision branches, boundary values, and exceptional cases.

### Application Functions

**1. overage_charge()**

Calculates additional data usage charges based on:
- Selected mobile plan.
- Data usage.
- Roaming status.
- Customer loyalty status.

**2. recharge_allowed()**

Checks whether a mobile recharge is permitted based on:
- Recharge amount.
- Number of pending recharges.
- KYC verification status.

**3. validity_status()**

Determines the mobile plan status:
- Active
- Grace period
- Expired

## 5. Project Structure

```text
SE-Lab-06-Code-Coverage/
│
├── mobile_data_plan.py
├── test_mobile_data_plan.py
│
├── CodeCoverageTest_mobile_data_plan.py
├── BranchCoverageTest_mobile_data_plan.py
│
├── Coverage_Results.pdf
│
└── README.md
```

## 6. Installation

Install the required Python packages:

```bash
pip install pytest coverage
```

Verify the installation:

```bash
python -m coverage --version
python -m pytest --version
```

## 7. Code Coverage Testing

Code coverage measures how many statements or lines of the application are executed during testing.

Run the following commands:

```bash
python -m coverage erase

python -m coverage run -m pytest CodeCoverageTest_mobile_data_plan.py -v

python -m coverage report -m
```

### Code Coverage Result

- Total test cases: 20
- Passed test cases: 20
- Code coverage achieved: 100%

## 8. Branch Coverage Testing

Branch coverage measures whether all possible decision outcomes, such as True and False conditions, are tested.

Run the following commands:

```bash
python -m coverage erase

python -m coverage run --branch -m pytest BranchCoverageTest_mobile_data_plan.py -v

python -m coverage report -m
```

### Branch Coverage Result

- Total test cases: 25
- Passed test cases: 25
- Branch coverage achieved: 100%

## 9. Difference Between Code Coverage and Branch Coverage

| Code Coverage | Branch Coverage |
|---|---|
| Measures executed statements | Measures executed decision outcomes |
| Checks whether a line was executed | Checks whether both decision outcomes were tested |
| Focuses on statement execution | Focuses on conditional execution paths |

## 10. Test Results Summary

| Testing Type | Tests Passed | Coverage |
|---|---:|---:|
| Code Coverage | 20/20 | 100% |
| Branch Coverage | 25/25 | 100% |

Both testing approaches successfully achieved 100% coverage, exceeding the minimum requirement of 90%.

## 11. Output Screenshots

The terminal output screenshots for both testing approaches are included in the following PDF:

**File:** `Coverage_Results.pdf`

The PDF contains:

- Code Coverage execution and report.
- Branch Coverage execution and report.
- Test execution results and coverage percentages.

## 12. Learning Outcomes

- Understood the concepts of code coverage and branch coverage.
- Learned to use Pytest and Coverage.py for testing.
- Identified untested statements and decision branches.
- Practiced writing test cases for edge conditions.
- Successfully achieved 100% code coverage and 100% branch coverage.

## 13. Conclusion

This experiment demonstrates the importance of code coverage and branch coverage in software testing. Comprehensive test cases were developed for the Mobile Data Plan application to verify its functionality and decision-making conditions.

The experiment successfully achieved 100% code coverage and 100% branch coverage, demonstrating complete statement and branch execution for the measured application code.

---

**Software Engineering Laboratory – Lab 06**

**Topic:** Code Coverage and Branch Coverage
